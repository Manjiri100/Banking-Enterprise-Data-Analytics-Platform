# Data dictionary

| Table | Purpose | Grain |
|---|---|---|
| customers | Customer master | one row per customer |
| accounts | Account/product relationship | one row per account |
| products | Product catalogue | one row per product |
| branches | Branch/region dimension | one row per branch |
| transactions | Core financial activity | one row per transaction |
| payments | Payment processing events | one row per payment |
| fraud_alerts | Risk/fraud monitoring events | one row per alert |
| complaints | Customer-service cases | one row per complaint |

Important analytical keys include `customer_id`, `account_id`, `product_id`, `transaction_id` and `payment_id`. The `payments` table carries `currency` so reconciliation can be performed within currency rather than mixing GBP, EUR and USD.

The project intentionally introduces controlled data-quality defects so that the analyst must identify and quantify them before trusting the outputs.
