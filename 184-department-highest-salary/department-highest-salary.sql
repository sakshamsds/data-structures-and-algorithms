# Write your MySQL query statement below

WITH SalaryRanks AS (
    SELECT
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        RANK() OVER(PARTITION BY e.departmentId ORDER BY e.salary DESC) AS r
    FROM employee e
    INNER JOIN department d
        ON e.departmentId = d.id
)

SELECT 
    Department,
    Employee,
    Salary
FROM SalaryRanks
WHERE r = 1;