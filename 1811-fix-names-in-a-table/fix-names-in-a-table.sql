# Write your MySQL query statement below

SELECT 
    user_id,
    -- CONCAT(UPPER(LEFT(name, 1)), LOWER(RIGHT(name, LENGTH(name) - 1))) as name
    CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2, LENGTH(name)))) as name
FROM users
ORDER BY user_id;