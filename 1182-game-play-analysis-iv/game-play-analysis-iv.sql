# Write your MySQL query statement below

WITH cte AS(
    SELECT 
        player_id,
        MIN(event_date) AS first_login
    FROM activity
    GROUP BY player_id
),
cte2 AS (
    SELECT 
        player_id,
        DATE_ADD(first_login, INTERVAL 1 DAY) AS next_date
    FROM cte
)
SELECT
ROUND((SELECT COUNT(DISTINCT player_id)
FROM activity
WHERE (player_id, event_date) IN (SELECT
player_id, next_date FROM cte2))/(SELECT COUNT(DISTINCT player_id) FROM activity), 2) AS fraction