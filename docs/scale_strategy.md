# Scale strategy

The portfolio uses a **development mode** and an **enterprise-scale mode**.

| Mode | Purpose | Approach |
|---|---|---|
| Sample | GitHub/demo | small CSV/Parquet files |
| Development | SQL/model testing | 100K–1M transactions |
| Large | performance testing | 10M transactions, chunked Parquet |
| Enterprise target | architecture demonstration | 100M+ transactions, partitioned Parquet |

The generator avoids creating one enormous in-memory DataFrame. Transactions are generated in chunks and written as separate Parquet parts. Analytical queries should filter by date and select only required columns. In a production warehouse, the equivalent strategy would be partitioning/clustering, incremental models and workload-appropriate compute.
