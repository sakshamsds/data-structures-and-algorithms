# Write your MySQL query statement below

SELECT 
    user_id,
    MAX(CASE WHEN YEAR(time_stamp) = 2020
                THEN time_stamp
             ELSE -1 
        END) AS last_stamp
FROM logins
GROUP BY user_id
    HAVING last_stamp > 0;