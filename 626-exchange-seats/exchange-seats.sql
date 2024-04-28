# Write your MySQL query statement below

WITH cte AS (
    SELECT
        *,
        LEAD(id) OVER(ORDER BY id) AS next_id,
        LAG(id) OVER(ORDER BY id) AS prev_id
    FROM seat
)

SELECT
    CASE 
        WHEN id % 2 = 0 THEN prev_id
        WHEN id % 2 = 1 THEN IF(next_id IS NOT NULL, next_id, id)
    END AS id,
    student
FROM cte
ORDER BY id;