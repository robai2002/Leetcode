# Write your MySQL query statement below
SELECT teacher_id,COUNT(DISTINCT subject_id) AS CNT
FROM Teacher 
GROUP BY Teacher_id
ORDER BY CNT