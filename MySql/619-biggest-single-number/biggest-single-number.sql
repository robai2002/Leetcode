# Write your MySQL query statement below
SELECT MAX(NUM) AS num 
FROM (
    SELECT num AS NUM 
    FROM MyNumbers 
    GROUP BY num 
    HAVING COUNT(*) = 1
) AS unique_nums;