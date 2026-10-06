import argparse
import os
from pathlib import Path

import numpy as np
import pandas as pd


def rng(seed):
    return np.random.default_rng(seed)


def write_table(df: pd.DataFrame, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == ".parquet":
        df.to_parquet(path, index=False)
    else:
        df.to_csv(path, index=False)


def generate_dimensions(out: Path, customers: int, seed: int):
    r = rng(seed)
    n_customers = max(1000, customers)
    n_products = 8
    n_branches = 100
    accounts_n = max(n_customers, int(round(n_customers * 1.45)))

    products = pd.DataFrame({
        "product_id": [f"P{i:03d}" for i in range(1, n_products + 1)],
        "product_name": ["Current Account", "Savings Account", "Premium Current", "Student Account", "Credit Card", "Personal Loan", "Mortgage", "Business Account"],
        "product_type": ["deposit", "deposit", "deposit", "deposit", "card", "lending", "lending", "business"],
        "segment": ["mass", "mass", "affluent", "mass", "mass", "mass", "affluent", "business"],
        "active_flag": [1] * n_products,
    })

    branches = pd.DataFrame({
        "branch_id": [f"BR{i:04d}" for i in range(1, n_branches + 1)],
        "region": r.choice(["London", "Midlands", "North West", "North East", "South East", "South West", "Scotland", "Wales"], n_branches),
        "branch_type": r.choice(["branch", "hub", "digital"], n_branches, p=[0.65, 0.15, 0.20]),
    })

    customers_df = pd.DataFrame({
        "customer_id": [f"C{i:08d}" for i in range(1, n_customers + 1)],
        "date_of_birth": pd.to_datetime("1960-01-01") + pd.to_timedelta(r.integers(0, 21000, n_customers), unit="D"),
        "customer_segment": r.choice(["mass", "affluent", "premier", "student", "business"], n_customers, p=[0.52, 0.22, 0.10, 0.10, 0.06]),
        "region": r.choice(branches["region"], n_customers),
        "onboarding_channel": r.choice(["branch", "mobile", "web", "partner"], n_customers, p=[0.18, 0.45, 0.30, 0.07]),
        "customer_status": r.choice(["active", "dormant", "closed"], n_customers, p=[0.90, 0.06, 0.04]),
    })

    # Deterministic account ownership makes every generated transaction joinable.
    account_customer_idx = ((np.arange(accounts_n)) % n_customers) + 1
    accounts = pd.DataFrame({
        "account_id": [f"A{i:09d}" for i in range(1, accounts_n + 1)],
        "customer_id": [f"C{i:08d}" for i in account_customer_idx],
        "product_id": r.choice(products["product_id"], accounts_n, p=[0.30, 0.20, 0.08, 0.08, 0.12, 0.08, 0.06, 0.08]),
        "branch_id": r.choice(branches["branch_id"], accounts_n),
        "open_date": pd.to_datetime("2019-01-01") + pd.to_timedelta(r.integers(0, 2800, accounts_n), unit="D"),
        "account_status": r.choice(["open", "closed", "blocked"], accounts_n, p=[0.92, 0.05, 0.03]),
    })

    # One intentional duplicate raw customer record for DQ investigation.
    # The original customer IDs remain present so this defect does not create an
    # unrelated orphan-key problem in the generated transaction population.
    if len(customers_df) > 100:
        customers_df = pd.concat([customers_df, customers_df.iloc[[99]].copy()], ignore_index=True)

    write_table(customers_df, out / "customers.csv")
    write_table(accounts, out / "accounts.csv")
    write_table(products, out / "products.csv")
    write_table(branches, out / "branches.csv")
    return n_customers, accounts_n


def transaction_currency(ids):
    mod = ids % 100
    return np.where(mod < 78, "GBP", np.where(mod < 90, "EUR", "USD"))


def generate_transactions(out: Path, n: int, customers_n: int, accounts_n: int, seed: int, fmt: str, chunk: int):
    r = rng(seed + 1)
    if n <= 0:
        raise ValueError("--transactions must be greater than zero")
    if chunk <= 0:
        raise ValueError("--chunk-size must be greater than zero")

    if fmt == "parquet":
        parts_dir = out / "_parts"
        parts_dir.mkdir(parents=True, exist_ok=True)
        for old in parts_dir.glob("transactions_*.parquet"):
            old.unlink()
        manifest = []
    else:
        target = out / "transactions.csv"
        if target.exists():
            target.unlink()

    for start in range(0, n, chunk):
        m = min(chunk, n - start)
        ids = np.arange(start + 1, start + m + 1)
        account_idx = r.integers(1, accounts_n + 1, m)
        customer_idx = ((account_idx - 1) % customers_n) + 1

        df = pd.DataFrame({
            "transaction_id": [f"T{i:012d}" for i in ids],
            "customer_id": [f"C{x:08d}" for x in customer_idx],
            "account_id": [f"A{x:09d}" for x in account_idx],
            "transaction_ts": pd.Timestamp("2025-01-01") + pd.to_timedelta(r.integers(0, 639, m), unit="D") + pd.to_timedelta(r.integers(0, 86400, m), unit="s"),
            "transaction_type": r.choice(["purchase", "transfer", "cash_withdrawal", "direct_debit", "refund"], m, p=[0.45, 0.24, 0.10, 0.15, 0.06]),
            "channel": r.choice(["mobile", "web", "branch", "atm", "api"], m, p=[0.36, 0.25, 0.12, 0.15, 0.12]),
            "amount": np.round(r.lognormal(3.4, 1.05, m), 2),
            "currency": transaction_currency(ids),
            "status": r.choice(["completed", "failed", "pending", "reversed"], m, p=[0.88, 0.06, 0.03, 0.03]),
            "merchant_category": r.choice(["grocery", "travel", "retail", "utilities", "restaurant", "other"], m),
            "source_system": r.choice(["core_banking", "cards", "payments", "mobile"], m, p=[0.45, 0.22, 0.23, 0.10]),
        })

        # Controlled raw-source DQ issues: one missing customer, one duplicate ID, one negative amount.
        if start <= 100002 < start + m:
            df.loc[100002 - start, "customer_id"] = None
        if start <= 250006 < start + m:
            df.loc[250006 - start, "transaction_id"] = df.loc[250005 - start, "transaction_id"]
        if start <= 500008 < start + m:
            df.loc[500008 - start, "amount"] = -25.0

        if fmt == "parquet":
            part = parts_dir / f"transactions_{start // chunk:04d}.parquet"
            df.to_parquet(part, index=False)
            manifest.append(str(part.relative_to(out)))
        else:
            df.to_csv(out / "transactions.csv", index=False, mode="a", header=start == 0)

    if fmt == "parquet":
        pd.DataFrame({"part": manifest}).to_csv(out / "transactions_manifest.csv", index=False)


def generate_events(out: Path, customers_n: int, transaction_n: int, seed: int):
    r = rng(seed + 10)
    fraud_n = max(500, int(transaction_n * 0.05))
    fraud_tx = r.integers(1, transaction_n + 1, fraud_n)
    fraud = pd.DataFrame({
        "alert_id": [f"FA{i:09d}" for i in range(1, fraud_n + 1)],
        "transaction_id": [f"T{x:012d}" for x in fraud_tx],
        "alert_type": r.choice(["velocity", "location_anomaly", "high_value", "merchant_risk", "device_change"], fraud_n),
        "risk_score": np.round(r.beta(2, 3, fraud_n) * 100, 1),
        "alert_status": r.choice(["open", "investigating", "closed", "false_positive"], fraud_n, p=[0.22, 0.18, 0.48, 0.12]),
        "created_at": pd.Timestamp("2025-01-01") + pd.to_timedelta(r.integers(0, 639, fraud_n), unit="D"),
    })

    complaint_n = max(300, int(customers_n * 0.22))
    complaints = pd.DataFrame({
        "complaint_id": [f"CO{i:09d}" for i in range(1, complaint_n + 1)],
        "customer_id": [f"C{x:08d}" for x in r.integers(1, customers_n + 1, complaint_n)],
        "complaint_type": r.choice(["payment", "card", "branch", "digital", "fraud", "service"], complaint_n),
        "channel": r.choice(["phone", "web", "branch", "mobile"], complaint_n),
        "severity": r.choice(["low", "medium", "high"], complaint_n, p=[0.55, 0.35, 0.10]),
        "status": r.choice(["open", "investigating", "resolved"], complaint_n, p=[0.16, 0.18, 0.66]),
        "created_at": pd.Timestamp("2025-01-01") + pd.to_timedelta(r.integers(0, 639, complaint_n), unit="D"),
        "resolution_days": r.integers(1, 35, complaint_n),
    })

    payment_n = max(500, int(transaction_n * 0.40))
    payment_tx = r.integers(1, transaction_n + 1, payment_n)
    payments = pd.DataFrame({
        "payment_id": [f"PAY{i:010d}" for i in range(1, payment_n + 1)],
        "transaction_id": [f"T{x:012d}" for x in payment_tx],
        "currency": transaction_currency(payment_tx),
        "payment_type": r.choice(["faster_payment", "card", "direct_debit", "international"], payment_n, p=[0.40, 0.30, 0.20, 0.10]),
        "payment_status": r.choice(["completed", "failed", "pending", "returned"], payment_n, p=[0.89, 0.055, 0.025, 0.03]),
        "failure_reason": r.choice(["insufficient_funds", "beneficiary_invalid", "technical_error", "fraud_hold", "timeout", ""], payment_n, p=[0.18, 0.12, 0.10, 0.06, 0.06, 0.48]),
        "settlement_amount": np.round(r.lognormal(3.3, 1.0, payment_n), 2),
    })

    write_table(fraud, out / "fraud_alerts.csv")
    write_table(complaints, out / "complaints.csv")
    write_table(payments, out / "payments.csv")


def main():
    p = argparse.ArgumentParser(description="Scalable synthetic enterprise banking data generator")
    p.add_argument("--transactions", type=int, default=100_000)
    p.add_argument("--customers", type=int, default=None)
    p.add_argument("--output", default="data/generated")
    p.add_argument("--format", choices=["csv", "parquet"], default="parquet")
    p.add_argument("--chunk-size", type=int, default=1_000_000)
    p.add_argument("--seed", type=int, default=42)
    args = p.parse_args()

    customers = args.customers or max(1000, args.transactions // 20)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    customers_n, accounts_n = generate_dimensions(out, customers, args.seed)
    generate_transactions(out, args.transactions, customers_n, accounts_n, args.seed, args.format, args.chunk_size)
    generate_events(out, customers_n, args.transactions, args.seed)
    print(f"Generated banking environment: {args.transactions:,} transactions; {customers_n:,} customers; {accounts_n:,} accounts.")


if __name__ == "__main__":
    main()
