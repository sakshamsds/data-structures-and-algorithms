DELETE FROM person
WHERE id NOT IN (
    SELECT id FROM (
        SELECT 
            MIN(id) as id
        FROM person
        GROUP BY email
    ) AS subquery
);
