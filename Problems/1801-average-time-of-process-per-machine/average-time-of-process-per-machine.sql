# Write your MySQL query statement below
select x.machine_id,Round(y.z - x.z,3) as processing_time from
(
    select machine_id,AVG(timestamp) as z from Activity 
    where activity_type = "start"
    group by machine_id
) as x
inner join 
(
    select machine_id,AVG(timestamp)  as z from Activity 
    where activity_type = "end"
    group by machine_id
) as y
on x.machine_id = y.machine_id