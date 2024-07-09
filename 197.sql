-- Write your PostgreSQL query statement below
select w2.id
from Weather as w1, Weather as w2
where 
w1.temperature < w2.temperature
and
w2.recordDate - w1.recordDate = 1;