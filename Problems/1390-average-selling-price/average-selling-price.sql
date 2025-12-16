select P.product_id,IFNULL(round(sum(U.units*P.price)/sum(U.units),2),0.00) as average_price
from UnitsSold as U
right join Prices as P
on U.product_id = P.product_id and U.purchase_date between P.start_date and P.end_date 
group by 
P.product_id
