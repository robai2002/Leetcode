# Write your MySQL query statement below
SELECT  
    contest_id,
    round(100*(count(*))/(SELECT COUNT(user_id) FROM Users),2) as percentage
    from Register
    group by contest_id
    order by percentage DESC,contest_id
