# Write your MySQL query statement below
select S.user_id,
IFNULL(ROUND(SUM(action = "confirmed")/COUNT(*),2),0.00) AS confirmation_rate
from Signups as S 
left join Confirmations as C
on S.user_id = C.user_id
group by user_id