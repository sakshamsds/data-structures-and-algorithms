# Write your MySQL query statement below

DELETE p2
FROM person p1
INNER JOIN person p2
    ON p1.email = p2.email
        AND p2.id > p1.id;