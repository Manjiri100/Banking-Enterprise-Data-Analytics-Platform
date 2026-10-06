import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest


def run_generator(tmp_path, fmt):
    out = tmp_path / f"generated_{fmt}"
    subprocess.run([
        sys.executable, "generator/generate_bank_data.py",
        "--transactions", "2000",
        "--customers", "1000",
        "--output", str(out),
        "--format", fmt,
        "--chunk-size", "500",
    ], check=True)
    return out


def test_generator_creates_expected_tables(tmp_path):
    out = run_generator(tmp_path, "csv")
    for name in ["customers.csv", "accounts.csv", "products.csv", "branches.csv", "payments.csv", "fraud_alerts.csv", "complaints.csv", "transactions.csv"]:
        assert (out / name).exists()

    customers = pd.read_csv(out / "customers.csv")
    accounts = pd.read_csv(out / "accounts.csv")
    tx = pd.read_csv(out / "transactions.csv")
    payments = pd.read_csv(out / "payments.csv")

    assert {"transaction_id", "customer_id", "account_id", "amount", "status"}.issubset(tx.columns)
    assert len(tx) == 2000
    assert tx["account_id"].isin(accounts["account_id"]).all()
    assert tx["customer_id"].dropna().isin(customers["customer_id"]).all()
    assert payments["transaction_id"].isin(tx["transaction_id"]).all()


def test_generator_supports_partitioned_parquet(tmp_path):
    pytest.importorskip("pyarrow")
    out = run_generator(tmp_path, "parquet")
    parts = sorted((out / "_parts").glob("transactions_*.parquet"))
    assert len(parts) == 4
    tx = pd.concat([pd.read_parquet(p) for p in parts], ignore_index=True)
    assert len(tx) == 2000
    assert (out / "transactions_manifest.csv").exists()
