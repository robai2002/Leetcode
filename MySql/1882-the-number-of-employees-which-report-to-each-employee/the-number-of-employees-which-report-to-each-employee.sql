# Write your MySQL query statement below
SELECT employee_id,
        name,
        N.reports_count,
        ROUND(N.total_age/N.reports_count) AS average_age
FROM (
    SELECT reports_to,count(DISTINCT employee_id) as reports_count,
     SUM(age) as total_age
     FROM Employees 
     GROUP BY reports_to
) AS N
INNER JOIN Employees 
ON N.reports_to = Employees.employee_id
ORDER BY Employees.employee_id