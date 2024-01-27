# Write your MySQL query statement below

SELECT 
    unique_id,
    name
FROM employees e
LEFT JOIN employeeUNI
    USING (id);
