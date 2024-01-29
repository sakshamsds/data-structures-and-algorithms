# Write your MySQL query statement below

WITH cte1 AS (
    SELECT 
        machine_id,
        SUM(timestamp)/COUNT(timestamp) AS start_time
    FROM activity
    WHERE activity_type = 'start'
    GROUP BY machine_id
), cte2 AS (
    SELECT
        machine_id,
        SUM(timestamp)/COUNT(timestamp) AS end_time
    FROM activity
    WHERE activity_type = 'end'
    GROUP BY machine_id
)
SELECT 
    machine_id,
    ROUND(end_time - start_time, 3) AS processing_time
FROM cte1
INNER JOIN cte2
    USING (machine_id);
