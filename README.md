# Power BI semantic model

## Model

Recommended star schema:

- **FactTransactions** — transaction grain
- **FactPayments** — payment grain
- **DimCustomer** — customer grain
- **DimAccount** — account grain
- **DimProduct** — product grain
- **DimBranch** — branch grain
- **DimDate** — calendar grain

Avoid many-to-many relationships between core facts. Use conformed dimensions and explicit measures.

## Dashboard pages

### 1. Executive Overview
- Transaction volume
- Completed value
- Payment failure rate
- Active customers
- High-risk alert count
- Complaint backlog

### 2. Payments & Operations
- Failure rate by payment type/channel
- Failure reason trend
- Returned/pending payments
- Operational hotspots

### 3. Fraud & Risk
- Alerts by risk band
- High-risk alerts
- Alert status and false positives
- Transaction context for investigation

### 4. Customer & Product
- Customers by segment
- Product penetration
- Activity by channel
- Completed transaction value

### 5. Data Quality & Reconciliation
- Duplicate IDs
- Missing keys
- Negative/invalid values
- Finance-vs-operations variance
- Source-system completeness

## Design principle

Every KPI should have one documented definition and one governed source. Dashboard visuals should answer a business question rather than exist only to demonstrate chart types.
