with ranked as (
    select
        customer_id,
        customer_segment,
        region,
        onboarding_channel,
        customer_status,
        row_number() over (partition by customer_id order by customer_status, customer_segment) as rn
    from {{ source('banking_raw','customers') }}
    where customer_id is not null
)
select customer_id, customer_segment, region, onboarding_channel, customer_status
from ranked
where rn = 1
