select
    product_id,
    product_name,
    product_type,
    segment,
    active_flag
from {{ source('banking_raw','products') }}
