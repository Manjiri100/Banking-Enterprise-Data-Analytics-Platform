-- Ticket: payment failures have increased. Identify channel/type/reason drivers.
SELECT
  p.payment_type,
  p.failure_reason,
  COUNT(*) AS payment_count,
  SUM(CASE WHEN p.payment_status='failed' THEN 1 ELSE 0 END) AS failed_payments,
  ROUND(100.0 * SUM(CASE WHEN p.payment_status='failed' THEN 1 ELSE 0 END) / COUNT(*),2) AS failure_rate_pct
FROM payments p
GROUP BY 1,2
ORDER BY failure_rate_pct DESC, failed_payments DESC;
