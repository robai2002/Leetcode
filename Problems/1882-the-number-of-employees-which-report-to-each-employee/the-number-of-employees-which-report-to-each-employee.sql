# Write your MySQL query statement below
SELECT
    E1.reports_to as employee_id,
    E2.name as name,
    count(*) as reports_count,
    round(avg(E1.age)) as average_age

 from Employees as E1
 inner join Employees as E2
 on E1.reports_to = E2.employee_id 
 group by E1.reports_to
 order by employee_id