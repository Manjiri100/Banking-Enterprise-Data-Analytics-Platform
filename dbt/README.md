# dbt layer

The dbt layer demonstrates a controlled ELT pattern:

`raw sources → staging → intermediate → analytical marts`

## Run locally with DuckDB

From the repository root:

```bash
python dbt/load_sample_data.py
cd dbt
dbt debug --profiles-dir .
dbt build --profiles-dir .
```

The loader creates the `raw` schema from the representative CSV files. The staging layer then removes/isolates the deliberately introduced raw-source quality defects before the curated models are tested.

For the 100M+ transaction target, the portfolio architecture would use an incremental fact model and warehouse-native partitioning/clustering rather than materialising the entire fact repeatedly.
