-- Write your PostgreSQL query statement below

select p.project_id, round(avg(experience_years),2) as average_years
from project as p, employee as e
where p.employee_id = e.employee_id 
group by p.project_id
order by p.project_id
