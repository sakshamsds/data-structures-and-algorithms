# Write your MySQL query statement below

SELECT name
FROM salesPerson
WHERE name NOT IN (
    SELECT 
        s.name
    FROM salesperson s
    INNER JOIN orders o
        USING (sales_id)
    INNER JOIN company c
        USING (com_id)
    WHERE c.name = 'RED'
);