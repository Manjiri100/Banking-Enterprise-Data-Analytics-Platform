select
    account_id,
    customer_id,
    product_id,
    branch_id,
    open_date,
    account_status
from {{ ref('stg_accounts') }}
