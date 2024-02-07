# Write your MySQL query statement below

WITH cte AS (
    SELECT
        product_id,
        MAX(change_date) as change_date
    FROM products
    WHERE DATEDIFF(change_date, '2019-08-16') <= 0
    GROUP BY product_id
)
SELECT 
    product_id,
    10 AS price
FROM products
WHERE product_id NOT IN (
    SELECT product_id FROM cte
)
UNION
SELECT
    product_id,
    new_price AS price
FROM cte
INNER JOIN products
    USING (product_id, change_date);