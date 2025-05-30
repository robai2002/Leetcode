# Write your MySQL query statement below
SELECT q1.person_name 
FROM Queue AS q1 INNER JOIN Queue AS q2
ON q1.turn >=q2.turn
group by q1.turn 
having sum(q2.weight)<=1000
order by sum(q2.weight) DESC 
LIMIT 1