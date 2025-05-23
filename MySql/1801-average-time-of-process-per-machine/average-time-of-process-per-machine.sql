# Write your MySQL query statement below
SELECT 
    e.machine_id,  
    ROUND(e.P - s.N, 3) AS processing_time
FROM (
    SELECT machine_id,AVG(timestamp) as P
    FROM Activity 
    WHERE activity_type = "end"
    GROUP BY machine_id
) AS e INNER JOIN 
(
    SELECT machine_id,AVG(timestamp) AS N
    FROM Activity 
    WHERE activity_type = "start"
    GROUP BY machine_id 
) as s
ON e.machine_id = s.machine_id  
