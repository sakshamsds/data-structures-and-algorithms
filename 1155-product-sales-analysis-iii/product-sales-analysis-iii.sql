# Write your MySQL query statement below

WITH cte AS (
    SELECT 
        product_id,
        MIN(year) AS year
    FROM sales
    GROUP BY product_id
)
SELECT 
    product_id,
    year AS first_year,
    quantity,
    price
FROM cte
INNER JOIN sales s
    USING (product_id, year);