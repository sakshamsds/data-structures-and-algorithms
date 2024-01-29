# Write your MySQL query statement below

WITH cte AS (
    SELECT 
        customer_id,
        COUNT(DISTINCT product_key) AS nums
    FROM customer
    GROUP BY customer_id
)
SELECT
    customer_id
FROM cte
WHERE nums = (SELECT COUNT(DISTINCT product_key) FROM product)