# Write your MySQL query statement below

# calculate the running weight using window function

WITH cte AS (
    SELECT 
        *,
        SUM(weight) OVER(ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total
    FROM queue
)
SELECT person_name
FROM cte
WHERE total <= 1000
ORDER BY total DESC
LIMIT 1;