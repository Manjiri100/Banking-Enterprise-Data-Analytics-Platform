select payment_id, transaction_id, payment_type, payment_status, failure_reason, settlement_amount
from {{ source('banking_raw','payments') }}
