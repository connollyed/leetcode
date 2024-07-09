select sell_date, count(distinct(product)) as num_sold, string_agg(distinct(product),',') as products
from activities
group by sell_date