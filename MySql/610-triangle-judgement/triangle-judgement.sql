# Write your MySQL query statement below
SELECT *,
      IF(x+y+z>GREATEST(x,y,z)*2,"Yes","No") AS triangle
FROM Triangle