-- # Write your MySQL query statement below

SELECT 
    a1.machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
FROM activity a1
INNER JOIN activity a2
    ON a1.activity_type = 'start' 
        AND a2.activity_type = 'end'
        AND a1.machine_id = a2.machine_id 
GROUP BY machine_id;

-- WITH cte1 AS (
--     SELECT 
--         machine_id,
--         SUM(timestamp)/COUNT(timestamp) AS start_time
--     FROM activity
--     WHERE activity_type = 'start'
--     GROUP BY machine_id
-- ), cte2 AS (
--     SELECT
--         machine_id,
--         SUM(timestamp)/COUNT(timestamp) AS end_time
--     FROM activity
--     WHERE activity_type = 'end'
--     GROUP BY machine_id
-- )
-- SELECT 
--     machine_id,
--     ROUND(end_time - start_time, 3) AS processing_time
-- FROM cte1
-- INNER JOIN cte2
--     USING (machine_id);
