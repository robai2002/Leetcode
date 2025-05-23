# Write your MySQL query statement below
SELECT unique_id,name 
From  EmployeeUNI RIGHT JOIN Employees 
ON Employees.id = EmployeeUNI.id

