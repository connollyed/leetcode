-- Write your PostgreSQL query statement below

select Products.product_name, sum(Orders.unit) as unit
from Products, Orders
where date_part('month', order_date) = 2 and date_part('year', order_date ) = 2020
and Products.product_id = Orders.product_id
group by Products.product_name, Orders.product_id
having sum(Orders.unit) >= 100



-- Using Join was faster
select Products.product_name, sum(Orders.unit) as unit
from Products join Orders
on Products.product_id = Orders.product_id
where date_part('month', order_date) = 2 and date_part('year', order_date ) = 2020
group by Products.product_name, Orders.product_id
having sum(Orders.unit) >= 100