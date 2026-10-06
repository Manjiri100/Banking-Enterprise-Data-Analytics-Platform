select alert_id, transaction_id, alert_type, risk_score, alert_status, created_at
from {{ source('banking_raw','fraud_alerts') }}
