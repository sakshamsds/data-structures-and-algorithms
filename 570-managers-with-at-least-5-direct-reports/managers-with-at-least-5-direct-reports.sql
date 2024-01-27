# Write your MySQL query statement below

WITH cte AS (
    SELECT managerId
    FROM employee
    GROUP BY managerId
        HAVING COUNT(*) > 4
)
SELECT name
FROM cte
INNER JOIN employee e
    ON cte.managerId = e.id;
