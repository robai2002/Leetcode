# Write your MySQL query statement below
SELECT product_name, 
       SUM(unit) AS unit
FROM Products INNER JOIN Orders 
ON Products.product_id = Orders.product_id
WHERE MONTH(order_date) =2 AND YEAR(order_date) = 2020
GROUP BY product_name
HAVING unit >=100