# Write your MySQL query statement below

SELECT 
    product_name,
    SUM(unit) as unit
FROM products
INNER JOIN orders
    USING (product_id)
WHERE YEAR(order_date) = 2020 
    AND MONTH(order_date) = 2
GROUP BY product_id
    HAVING SUM(unit) >= 100;