# 🏦 Banking Enterprise Data & Analytics Platform

## 📌 About the Project

This project is an enterprise-style banking analytics platform designed to demonstrate how data analysts can transform large, complex, and potentially inconsistent banking data into trusted business intelligence.

The solution brings together customer, account, transaction, payment, fraud, complaint, product, and branch data to support data quality investigation, operational monitoring, reconciliation, customer analytics, fraud analysis, and executive reporting.

It combines **SQL, Python, Power BI, dbt, data quality controls, scalable data generation, and LLM-assisted investigation** to demonstrate an end-to-end analytics workflow.

---

## 🚀 Project Overview

Modern banking organisations operate across multiple systems and data sources, creating challenges around data consistency, reporting accuracy, operational visibility, fraud monitoring, and regulatory controls.

This project simulates an enterprise banking environment where analysts are required to investigate business problems across interconnected datasets and produce reliable, decision-ready insights.

The platform follows an end-to-end workflow:

**Raw Data → Data Profiling → Data Quality → SQL Investigation → Transformation → Reconciliation → Analytics → Power BI → LLM-Assisted Investigation → Business Decision**

The project is designed to demonstrate not only dashboard development, but the broader analytical process required to turn complex banking data into trusted information.

---

## 🏢 Business Problems Addressed

The platform addresses common banking analytics challenges including:

* Payment failures and operational exceptions
* Finance vs operations reconciliation
* Customer growth and account activity
* Fraud-alert investigation and prioritisation
* Data-quality issues across critical banking entities
* Customer complaints and operational performance
* Product and branch performance
* KPI consistency across reporting layers
* Manual reporting and investigation effort
* Data governance and validation requirements

---

## 🎯 What the Project Answers

The platform is designed to answer questions such as:

### 💳 Payments

* Which payment methods have the highest failure rates?
* Are failures concentrated in particular regions, products, or channels?
* Which failure reasons require operational attention?
* Are payment failures increasing over time?

### 💰 Reconciliation

* Do finance and operational transaction totals agree?
* Where are discrepancies occurring?
* Which records cannot be reconciled?
* What controls should be applied before reporting?

### 👥 Customers

* How is the customer base changing?
* Which products are driving customer growth?
* Which customer segments are most active?
* Where are opportunities for customer retention or growth?

### 🚨 Fraud

* Which fraud alerts have the highest risk indicators?
* Are alerts concentrated around particular transaction types or channels?
* Which cases should be prioritised for investigation?
* What patterns could indicate unusual activity?

### 🧹 Data Quality

* Are there duplicate records?
* Which critical fields are missing?
* Are there orphaned account, transaction, or customer records?
* Are values valid according to defined business rules?
* Can the data be trusted for downstream reporting?

### 📞 Complaints

* Which complaint categories are most common?
* Which products or branches generate the highest complaint volumes?
* How quickly are complaints being resolved?
* Where are operational improvements required?

---

## 📈 Enterprise-Scale Design

The project is designed to demonstrate scalable analytical thinking rather than relying only on a small static dataset.

| Environment       |    Approximate Scale | Purpose                           |
| ----------------- | -------------------: | --------------------------------- |
| Sample            |      5K transactions | Exploration and demonstration     |
| Development       | 100K–1M transactions | Development and testing           |
| Large             |     10M transactions | Performance and scale testing     |
| Enterprise Target |   100M+ transactions | Large-scale processing capability |

The project includes a reproducible data generator so the environment can be expanded without storing large generated datasets in the GitHub repository.

### 🔄 Big-Data Capability Flow

**Sample Data**

↓

**Data Profiling**

↓

**Scalable Data Generator**

↓

**1M → 10M → 100M+ Transactions**

↓

**Partitioned Parquet / CSV**

↓

**SQL / DuckDB Processing**

↓

**Incremental dbt Transformations**

↓

**Analytical Marts**

↓

**Power BI / Business Reporting**

This demonstrates the ability to design for scale while keeping the GitHub repository lightweight and reproducible.

---

## 🗂️ Data Environment

The simulated banking environment contains interconnected datasets covering major banking entities.

| Dataset      | Purpose                                             |
| ------------ | --------------------------------------------------- |
| Customers    | Customer demographics and customer-level attributes |
| Accounts     | Customer accounts and account relationships         |
| Products     | Banking products and product classifications        |
| Branches     | Branch and regional information                     |
| Transactions | Core transaction activity                           |
| Payments     | Payment-level operational information               |
| Fraud Alerts | Suspicious activity and investigation indicators    |
| Complaints   | Customer complaints and resolution information      |

Sample data is included in:

`data/sample/`

Large generated datasets are intentionally excluded from GitHub and can be recreated using the supplied generator.

---

## 🧹 Controlled Data Quality Problems

The project deliberately incorporates realistic data-quality challenges so that the analysis demonstrates investigation rather than simply reporting clean data.

Examples include:

* Duplicate records
* Missing customer attributes
* Missing mandatory fields
* Invalid values
* Orphan records
* Inconsistent identifiers
* Referential-integrity issues
* Transaction/payment inconsistencies
* Reconciliation differences
* Potentially unreliable reporting fields

The objective is to identify these problems, quantify their impact, and establish whether the data is suitable for downstream analysis.

---

## 🔍 Analytical Workflow

### 1. Data Profiling

Initial profiling is performed to understand:

* Row counts
* Column structures
* Missing values
* Duplicate records
* Data types
* Value distributions
* Referential relationships
* Potential anomalies

---

### 2. Data Quality Investigation

SQL-based checks are used to identify issues affecting critical banking datasets.

Examples include:

* Duplicate customers
* Missing account information
* Invalid transaction values
* Orphaned transactions
* Invalid payment relationships
* Missing fraud-alert identifiers
* Complaint-data inconsistencies

The objective is to distinguish **data-quality problems from genuine business behaviour**.

---

### 3. Payment Failure Investigation

Payment data is analysed to identify:

* Failure rates
* Failure reasons
* Payment-method performance
* Channel performance
* Regional patterns
* Product-level differences
* Time-based trends

The analysis supports operational teams in identifying where payment performance requires attention.

---

### 4. Finance vs Operations Reconciliation

The reconciliation workflow compares financial and operational views of transaction activity.

The analysis identifies:

* Matching records
* Missing records
* Amount discrepancies
* Count discrepancies
* Unmatched transactions
* Reconciliation rates

This demonstrates how analysts can create controls around financial reporting rather than assuming that two systems agree.

---

### 5. Customer & Product Analytics

Customer and account data is used to analyse:

* Customer growth
* Product adoption
* Account activity
* Customer segments
* Product performance
* Regional trends

The objective is to connect customer behaviour with product and business performance.

---

### 6. Fraud Analytics

Fraud-alert data is investigated alongside transaction information to identify:

* High-risk transactions
* Alert volumes
* Risk patterns
* Fraud concentrations
* Transaction characteristics associated with alerts
* Investigation priorities

The analysis is intended to support analyst-led investigation rather than replace human decision-making.

---

### 7. Complaints & Operations Analytics

Complaint data is analysed to understand:

* Complaint volumes
* Complaint categories
* Product-level complaint patterns
* Branch/region trends
* Resolution performance
* Operational pressure points

This allows business teams to identify recurring service and operational problems.

---

## 🧮 SQL Analytics

SQL is used as a primary investigation and analytical tool throughout the project.

The repository contains dedicated SQL areas for:

* Customer analytics
* Data quality
* Fraud analytics
* Operations
* Payments
* Reconciliation

Examples of analytical techniques include:

* Aggregations
* Joins
* CTEs
* Window functions
* Conditional logic
* Exception identification
* Duplicate detection
* Reconciliation logic
* KPI calculations
* Trend analysis

The SQL layer is designed around **business questions**, rather than isolated technical exercises.

---

## 🐍 Python Data Processing

Python is used to support:

* Data profiling
* Dataset generation
* Validation
* Scalable data creation
* Analytical preparation
* Reproducible workflows

The project includes a scalable banking-data generator capable of producing progressively larger transaction environments.

Example:

```bash
python generator/generate_bank_data.py --transactions 100000 --seed 42 --format csv --chunk-size 25000
```

For larger-scale testing:

```bash
python generator/generate_bank_data.py --transactions 10000000 --seed 42 --format parquet --chunk-size 1000000
```

The generator is designed to avoid requiring large datasets to be stored in the repository.

---

## 🔄 dbt Transformation Layer

dbt is used to demonstrate structured transformation and analytical modelling.

The project contains:

* Staging models
* Intermediate transformations
* Dimension models
* Fact models
* Source definitions
* Schema tests
* Reusable analytical models

The transformation layer separates raw source data from business-ready analytical datasets.

This supports:

* Reproducibility
* Testing
* Data lineage
* Modular transformations
* Consistent business logic
* Maintainable analytical models

---

## 📊 Power BI Analytics

Power BI is used as the business-facing reporting layer.

The analytical model is designed to provide visibility into:

* Customer performance
* Transaction activity
* Payment failures
* Fraud alerts
* Complaints
* Reconciliation
* Data-quality indicators

The dashboard layer is intended to translate detailed analytical investigation into information that business stakeholders can use for monitoring and decision-making.

Key measures and definitions are documented separately in:

`powerbi/measures.dax`

and

`powerbi/metric_definitions.md`

---

## 🤖 LLM-Assisted Analyst Investigation

The project also demonstrates how an **LLM-assisted analytics workflow** could support analysts working with complex banking data.

The concept is designed around a human-in-the-loop model:

**Business Question**

↓

**LLM Interprets Investigation Request**

↓

**Relevant Data / SQL Logic Identified**

↓

**Analytical Result**

↓

**Analyst Validates Result**

↓

**Business Conclusion**

The LLM is treated as an analytical assistant rather than an autonomous decision-maker.

Potential use cases include:

* Explaining KPI movements
* Summarising data-quality issues
* Supporting investigation queries
* Identifying unusual patterns
* Generating investigation hypotheses
* Summarising analytical findings

Human validation remains an essential control for financial, risk, fraud, and regulatory use cases.

---

## 🎫 Business Investigation Tickets

The repository contains six business-style investigation tickets:

| Ticket                    | Business Problem                                 |
| ------------------------- | ------------------------------------------------ |
| `01_payment_failures.md`  | Investigate payment failure patterns             |
| `02_reconciliation.md`    | Investigate finance vs operations discrepancies  |
| `03_customer_growth.md`   | Analyse customer growth and product activity     |
| `04_fraud_triage.md`      | Prioritise fraud investigation                   |
| `05_data_quality_gate.md` | Determine whether data is suitable for reporting |
| `06_complaints.md`        | Analyse complaint and operational performance    |

These tickets demonstrate how technical analysis can be connected directly to business requirements.

---

## 💡 Business Impact

The platform is designed to demonstrate how analytics can:

* Improve confidence in management reporting
* Identify data-quality issues before they affect decisions
* Reduce manual investigation and reporting effort
* Improve visibility into payment failures
* Support fraud and risk investigation
* Strengthen finance and operations reconciliation
* Identify customer and product opportunities
* Improve complaint and operational monitoring
* Create consistent KPI definitions
* Establish reusable analytical workflows

---

## 🧠 Skills Demonstrated

### Data Analytics

* SQL
* Python
* Data Profiling
* Data Quality
* Data Validation
* Reconciliation
* Root-Cause Analysis
* Business Analysis

### Business Intelligence

* Power BI
* KPI Development
* Data Modelling
* Dashboard Design
* Business Storytelling
* Performance Analysis

### Data Engineering / Modern Analytics

* dbt
* DuckDB
* Parquet
* Incremental Processing
* Scalable Data Generation
* Data Transformation
* Analytical Data Modelling

### Banking Analytics

* Payments Analytics
* Fraud Analytics
* Customer Analytics
* Financial Reconciliation
* Operational Analytics
* Complaints Analytics
* Data Governance

### AI

* LLM-assisted investigation
* GenAI analytical workflows
* Human-in-the-loop validation

---

## 📁 Repository Structure

```text
banking-enterprise-data-analytics-v2/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── business-tickets/
│   ├── 01_payment_failures.md
│   ├── 02_reconciliation.md
│   ├── 03_customer_growth.md
│   ├── 04_fraud_triage.md
│   ├── 05_data_quality_gate.md
│   └── 06_complaints.md
│
├── data/
│   └── sample/
│       ├── accounts.csv
│       ├── branches.csv
│       ├── complaints.csv
│       ├── customers.csv
│       ├── fraud_alerts.csv
│       ├── payments.csv
│       ├── products.csv
│       └── transactions.csv
│
├── dbt/
│   ├── models/
│   │   ├── staging/
│   │   ├── intermediate/
│   │   └── marts/
│   ├── tests/
│   ├── dbt_project.yml
│   └── profiles.yml.example
│
├── docs/
│   ├── architecture.md
│   ├── business_outcomes.md
│   ├── data_dictionary.md
│   ├── portfolio_story.md
│   ├── scale_strategy.md
│   └── validation.md
│
├── generator/
│   └── generate_bank_data.py
│
├── llm/
│   └── analyst_assistant.md
│
├── powerbi/
│   ├── measures.dax
│   ├── metric_definitions.md
│   └── README.md
│
├── python/
│   └── profile_transactions.py
│
├── sql/
│   ├── customer_analytics/
│   ├── data_quality/
│   ├── fraud/
│   ├── operations/
│   ├── payments/
│   └── reconciliation/
│
├── tests/
│   └── test_generator.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## ⚡ Quick Start

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Generate a development dataset:

```bash
python generator/generate_bank_data.py --transactions 100000 --seed 42 --format csv --chunk-size 25000
```

Generate a larger Parquet environment:

```bash
python generator/generate_bank_data.py --transactions 10000000 --seed 42 --format parquet --chunk-size 1000000
```

Run the test suite:

```bash
pytest -q
```

Load the sample data into the analytical environment:

```bash
python dbt/load_sample_data.py
```

Run dbt:

```bash
cd dbt
dbt debug --profiles-dir .
dbt build --profiles-dir .
```

---

## 🧪 Validation & Testing

The project includes automated validation to support reproducible analytical workflows.

Testing covers areas such as:

* Generated dataset structure
* Expected record relationships
* Data-quality conditions
* Transformation logic
* Analytical model validation

Run:

```bash
pytest -q
```

The project also includes CI configuration under:

`.github/workflows/ci.yml`

---

## 📚 Documentation

Additional documentation is available in the `docs/` directory, including:

* Architecture
* Business outcomes
* Data dictionary
* Portfolio story
* Scale strategy
* Validation approach

These documents provide additional context for recruiters and technical reviewers who want to understand how the platform was designed.

---

## 📷 Project Preview

**Enterprise Banking Data & Analytics Platform**

*Project architecture, analytical workflow, business KPIs, data quality, reconciliation, fraud analytics and LLM-assisted investigation.*

<img width="1024" height="687" alt="image" src="https://github.com/user-attachments/assets/0208ea92-feae-4d6d-8e60-7f24fa3cb41f" />

## 📁 Project Summary

This project demonstrates an end-to-end approach to enterprise banking analytics, combining business problem-solving with SQL investigation, Python processing, data-quality controls, reconciliation, dbt transformation, Power BI reporting, scalable data generation, and LLM-assisted analytical investigation.

The project uses **synthetic data** and is designed as a reproducible portfolio environment. The 100M+ transaction capability represents an **enterprise-scale project target and technical design capability**, not data handled in prior employment.

The focus is on demonstrating how a data analyst can move from **business problem → complex data → investigation → validation → trusted metrics → analytical insight → business decision**.

