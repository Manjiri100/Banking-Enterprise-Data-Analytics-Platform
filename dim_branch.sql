select
    branch_id,
    region,
    branch_type
from {{ source('banking_raw','branches') }}
