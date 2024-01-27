# Write your MySQL query statement below

SELECT 
    m.name
FROM employee e
INNER JOIN employee m
    ON e.managerId = m.id
GROUP BY m.id
    HAVING COUNT(m.id) > 4;

-- WITH cte AS (
--     SELECT managerId
--     FROM employee
--     GROUP BY managerId
--         HAVING COUNT(*) > 4
-- )
-- SELECT name
-- FROM cte
-- INNER JOIN employee e
--     ON cte.managerId = e.id;
