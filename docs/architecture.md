# Architecture

```text
Customers / Accounts / Products / Branches
Payments / Transactions / Fraud / Complaints
                    │
                    ▼
              Raw / source layer
                    │
          profiling + DQ controls
                    │
             SQL / Python ELT
                    │
                    ▼
              dbt transformations
          staging → intermediate → marts
                    │
                    ▼
           Curated analytical model
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
      Power BI          LLM analyst assistant
```

The architecture deliberately separates operational-style source data from governed analytical outputs. KPI definitions belong in the curated model, not in ad-hoc dashboard formulas.
