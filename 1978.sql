-- Write your PostgreSQL query statement below

select employee_id 
from Employees 
where manager_id in 
    (select manager_id from Employees where manager_id is not null
    except 
    select employee_id from Employees) 

and salary < 30000
order by employee_id


-- Alot faster
-- did the first solution because in where clause I was
-- writing is not in

select employee_id 
from Employees 
where manager_id not in (select employee_id from Employees)
and salary < 30000
order by employee_id