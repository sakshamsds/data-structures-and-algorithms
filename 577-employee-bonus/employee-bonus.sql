# Write your MySQL query statement below

SELECT name, bonus
FROM employee e
LEFT JOIN bonus b
    USING (empId)
WHERE bonus IS NULL 
    OR bonus < 1000;