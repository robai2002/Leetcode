# Write your MySQL query statement below
select distinct visited_on, amount,average_amount
from ( select a.visited_on as visited_on,sum(b.amount) as amount, round(sum(b.amount)/7,2) as average_amount
from customer a join customer b 
on a.visited_on>=b.visited_on
where datediff(a.visited_on,b.visited_on)<=6
group by a.visited_on,a.name) as t1
having datediff(visited_on,(select min(visited_on) from customer order by visited_on asc))>=6