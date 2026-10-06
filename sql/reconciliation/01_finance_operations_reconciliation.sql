-- Ticket: Finance and Operations totals do not reconcile.
-- Aggregate payments to transaction grain first so one-to-many payment records
-- cannot multiply transaction values during the reconciliation.
WITH payment_by_transaction AS (
    SELECT
        transaction_id,
        currency,
        SUM(CASE WHEN payment_status = 'completed' THEN settlement_amount ELSE 0 END) AS settled_payment_value
    FROM payments
    GROUP BY transaction_id, currency
),
transaction_by_currency AS (
    SELECT
        transaction_id,
        currency,
        SUM(CASE WHEN status = 'completed' THEN amount ELSE 0 END) AS completed_transaction_value
    FROM transactions
    GROUP BY transaction_id, currency
)
SELECT
    t.currency,
    ROUND(SUM(t.completed_transaction_value), 2) AS completed_transaction_value,
    ROUND(SUM(COALESCE(p.settled_payment_value, 0)), 2) AS settled_payment_value,
    ROUND(SUM(t.completed_transaction_value) - SUM(COALESCE(p.settled_payment_value, 0)), 2) AS variance
FROM transaction_by_currency t
LEFT JOIN payment_by_transaction p
  ON t.transaction_id = p.transaction_id
 AND t.currency = p.currency
GROUP BY t.currency
ORDER BY ABS(variance) DESC;
