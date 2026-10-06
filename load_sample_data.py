"""Load the repository's sample CSV sources into a local DuckDB raw schema."""
from pathlib import Path

import duckdb

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "data" / "sample"
DB = ROOT / "banking.duckdb"
TABLES = ["customers", "accounts", "products", "branches", "transactions", "payments", "fraud_alerts", "complaints"]


def main():
    con = duckdb.connect(str(DB))
    con.execute("create schema if not exists raw")
    for table in TABLES:
        path = (SAMPLE / f"{table}.csv").as_posix()
        con.execute(f'create or replace table raw."{table}" as select * from read_csv_auto(?, header=true)', [path])
        count = con.execute(f'select count(*) from raw."{table}"').fetchone()[0]
        print(f"raw.{table}: {count:,} rows")
    con.close()
    print(f"Loaded sample sources into {DB}")


if __name__ == "__main__":
    main()
