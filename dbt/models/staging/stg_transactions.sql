with ranked as (
    select
        transaction_id,
        customer_id,
        account_id,
        transaction_ts,
        transaction_type,
        channel,
        amount,
        currency,
        status,
        merchant_category,
        source_system,
        row_number() over (partition by transaction_id order by transaction_ts desc) as rn
    from {{ source('banking_raw','transactions') }}
    where amount >= 0
      and customer_id is not null
)
select
    transaction_id,
    customer_id,
    account_id,
    transaction_ts,
    transaction_type,
    channel,
    amount,
    currency,
    status,
    merchant_category,
    source_system
from ranked
where rn = 1
