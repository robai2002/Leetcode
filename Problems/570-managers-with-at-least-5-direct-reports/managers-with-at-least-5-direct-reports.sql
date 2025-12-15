# Write your MySQL query statement below
SELECT M.name 
FROM employee AS E
INNER JOIN employee AS M
ON E.managerId = M.id 
GROUP BY E.managerId
HAVING COUNT(E.id) >= 5
