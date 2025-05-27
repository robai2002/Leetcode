# Write your MySQL query statement below
select e.employee_id,
        e.name,
        count(e2.reports_to) as reports_count,
        round(avg(e2.age),0) as average_age
from employees e 
inner join employees e2 
on e.employee_id=e2.reports_to
group by e.employee_id,e.name
order by e.employee_id