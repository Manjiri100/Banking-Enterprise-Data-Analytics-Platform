# Governed LLM analyst assistant

## Use case

A manager asks: **“Why did payment failures increase last month?”**

The assistant should:

1. classify the question;
2. map it to approved KPI definitions;
3. identify permitted datasets and fields;
4. generate candidate SQL;
5. run validation checks;
6. execute the query in a read-only analytical environment;
7. inspect the result for data-quality anomalies;
8. explain the finding with evidence;
9. suggest the next investigation.

## Guardrails

- synthetic portfolio data only;
- read-only analytical access;
- no autonomous credit, fraud, lending or customer decisions;
- KPI definitions come from the governed semantic model;
- SQL and findings require human review before operational use;
- sensitive data should be masked or excluded.
