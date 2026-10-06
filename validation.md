# Version 2 validation record

The repository was checked for code correctness, file structure and generator behaviour before packaging.

## Automated checks

- Generator help command runs successfully.
- CSV generation test passes.
- Generated transactions use valid account/customer keys apart from the deliberate raw-source defects.
- Payment transaction IDs resolve to generated transaction IDs.
- Controlled raw-source data-quality issues are present in the sample data for investigation.
- The Parquet test is configured to run when the declared `pyarrow` dependency is installed; the current execution environment did not have that optional engine available.

## Design checks

- Raw data contains deliberate quality issues; dbt staging removes/isolates those issues before curated marts.
- Reconciliation aggregates payments to transaction grain before comparing values.
- The transaction generator is chunked so 100M+ records do not require one giant in-memory DataFrame.
- The repository contains representative data rather than committing an enterprise-scale dataset.

## Portfolio integrity

All datasets are synthetic. The project is a portfolio simulation and must not be described as professional work performed for a real bank.
