# Write your MySQL query statement below
# wanna do left join

SELECT eu.unique_id, e.name
FROM employees e
LEFT JOIN employeeuni eu
    ON e.id = eu.id;