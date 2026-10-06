select
  t.transaction_id, t.transaction_ts, t.transaction_type, t.channel, t.amount, t.currency,
  t.status, t.merchant_category, t.source_system,
  c.customer_segment, c.region,
  a.product_id, a.branch_id
from {{ ref('stg_transactions') }} t
left join {{ ref('stg_customers') }} c on t.customer_id=c.customer_id
left join {{ ref('stg_accounts') }} a on t.account_id=a.account_id
