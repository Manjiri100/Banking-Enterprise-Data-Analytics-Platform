-- Ticket: prioritise fraud alerts for investigation.
SELECT
  fa.alert_type,
  fa.alert_status,
  COUNT(*) AS alerts,
  ROUND(AVG(fa.risk_score),1) AS avg_risk_score,
  SUM(CASE WHEN fa.risk_score >= 75 THEN 1 ELSE 0 END) AS high_risk_alerts
FROM fraud_alerts fa
GROUP BY 1,2
ORDER BY high_risk_alerts DESC;
