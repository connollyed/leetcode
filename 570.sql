-- Write your PostgreSQL query statement below
select e1.name
from Employee as e1 left join Employee as e2 on e1.id = e2.managerId
group by e2.managerId, e1.name
having count(e2.managerId) >= 5