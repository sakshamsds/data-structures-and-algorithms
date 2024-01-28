# Write your MySQL query statement below

SELECT 
    q1.person_name
    -- SUM(q2.weight)
FROM queue q1
JOIN queue q2
    ON q1.turn >= q2.turn
GROUP BY q1.turn
    HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1;