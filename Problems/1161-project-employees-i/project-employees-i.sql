# Write your MySQL query statement below
SELECT 
    P.project_id,
    IFNULL(round(avg(experience_years),2),0.00) as average_years
FROM 
    Project as P 
LEFT JOIN 
    Employee as E
on 
   P.employee_id = E.employee_id
GROUP BY 
      project_id 