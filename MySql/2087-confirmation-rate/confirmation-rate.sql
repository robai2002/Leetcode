# Write your MySQL query statement below
SELECT Signups.user_id,IFNULL(ROUND(SUM(action = "confirmed")/COUNT(*),2),0.00) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations
ON Confirmations.user_id = Signups.user_id
GROUP BY user_id
