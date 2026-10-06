-- Ticket: identify products and customer segments driving activity.
SELECT
  c.customer_segment,
  p.product_name,
  COUNT(DISTINCT a.customer_id) AS customers,
  COUNT(t.transaction_id) AS transactions,
  ROUND(SUM(CASE WHEN t.status='completed' THEN t.amount ELSE 0 END),2) AS completed_value
FROM customers c
JOIN accounts a ON c.customer_id=a.customer_id
JOIN products p ON a.product_id=p.product_id
LEFT JOIN transactions t ON a.account_id=t.account_id
GROUP BY 1,2
ORDER BY completed_value DESC;
