# Write your MySQL query statement below

SELECT name
FROM (
    SELECT
        e2.id,
        e2.name,
        COUNT(*) as c
    FROM employee e1
    LEFT JOIN employee e2
        ON e1.managerId = e2.id
    GROUP BY e2.id
) AS subtable
WHERE c > 4
    AND id IS NOT NULL;
