# Write your MySQL query statement below
SELECT
   N.reports_to as employee_id,
   E.name as name,
   N.reports_count as reports_count,
   N.average_age as average_age

FROM (
    SELECT reports_to,count(*) as reports_count,
    round(avg(age)) as average_age
    from Employees 
    group by reports_to
) as N
inner join employees as E
on N.reports_to = E.employee_id
order by employee_id