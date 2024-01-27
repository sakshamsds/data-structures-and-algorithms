# Write your MySQL query statement below

SELECT 
    contest_id,
    ROUND(COUNT(contest_id)/(SELECT COUNT(*) FROM users) * 100, 2) AS percentage
FROM register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;