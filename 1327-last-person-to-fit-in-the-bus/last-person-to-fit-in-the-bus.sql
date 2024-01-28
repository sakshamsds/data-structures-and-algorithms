# Write your MySQL query statement below

WITH cte AS (
    SELECT
        person_name,
        SUM(weight) OVER(ORDER BY turn) as total_weight
    FROM queue
)
SELECT 
    person_name
    -- total_weight
FROM cte
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;