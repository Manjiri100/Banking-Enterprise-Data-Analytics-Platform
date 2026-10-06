select distinct customer_id, customer_segment, region, onboarding_channel, customer_status
from {{ ref('stg_customers') }}
