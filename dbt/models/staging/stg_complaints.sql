select complaint_id, customer_id, complaint_type, channel, severity, status, created_at, resolution_days
from {{ source('banking_raw','complaints') }}
