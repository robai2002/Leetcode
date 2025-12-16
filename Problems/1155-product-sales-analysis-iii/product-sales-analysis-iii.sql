# Write your MySQL query statement below
SELECT M.product_id,
      M.first_year,
      Sales.quantity,
      Sales.price
FROM (
    SELECT product_id,
    min(year) AS first_year 
    FROM Sales
     GROUP BY product_id
     ) AS M
LEFT JOIN Sales 
ON Sales.product_id = M.product_id AND M.first_year = Sales.year
