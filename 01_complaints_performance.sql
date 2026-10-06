SELECT
  complaint_type,
  severity,
  COUNT(*) AS complaints,
  ROUND(AVG(resolution_days),1) AS avg_resolution_days,
  SUM(CASE WHEN status <> 'resolved' THEN 1 ELSE 0 END) AS unresolved
FROM complaints
GROUP BY 1,2
ORDER BY unresolved DESC, avg_resolution_days DESC;
