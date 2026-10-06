-- Core data-quality gate. Run against the raw/source layer before trusted MI.
SELECT 'duplicate_transaction_id' AS check_name, COUNT(*) AS failures
FROM (SELECT transaction_id FROM transactions GROUP BY transaction_id HAVING COUNT(*) > 1) d
UNION ALL
SELECT 'duplicate_customer_id', COUNT(*)
FROM (SELECT customer_id FROM customers GROUP BY customer_id HAVING COUNT(*) > 1) d
UNION ALL
SELECT 'missing_transaction_customer_id', COUNT(*) FROM transactions WHERE customer_id IS NULL
UNION ALL
SELECT 'negative_transaction_amount', COUNT(*) FROM transactions WHERE amount < 0
UNION ALL
SELECT 'orphan_transaction_customer', COUNT(*)
FROM transactions t LEFT JOIN customers c USING(customer_id)
WHERE t.customer_id IS NOT NULL AND c.customer_id IS NULL
UNION ALL
SELECT 'orphan_account_customer', COUNT(*)
FROM accounts a LEFT JOIN customers c USING(customer_id)
WHERE c.customer_id IS NULL;
