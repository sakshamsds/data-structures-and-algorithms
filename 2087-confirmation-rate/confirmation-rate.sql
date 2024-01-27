# Write your MySQL query statement below

SELECT 
    user_id,
    ROUND(SUM(IF(action = 'confirmed', 1, 0))/COUNT(s.time_stamp), 2) AS confirmation_rate
FROM signups s
LEFT JOIN confirmations c
    USING (user_id)
GROUP BY user_id;
