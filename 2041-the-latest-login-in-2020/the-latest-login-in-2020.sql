# Write your MySQL query statement below

SELECT 
    DISTINCT user_id,
    FIRST_VALUE(time_stamp) OVER(PARTITION BY user_id ORDER BY time_stamp DESC)  AS last_stamp
FROM logins
WHERE YEAR(time_stamp) = 2020;

-- SELECT
--     user_id,
--     MAX(time_stamp) as last_stamp
-- FROM logins
-- WHERE YEAR(time_stamp) = 2020
-- GROUP BY user_id;

-- SELECT 
--     user_id,
--     MAX(CASE WHEN YEAR(time_stamp) = 2020
--                 THEN time_stamp
--              ELSE -1 
--         END) AS last_stamp
-- FROM logins
-- GROUP BY user_id
--     HAVING last_stamp > 0;