# Write your MySQL query statement below

WITH deptRank AS (
    SELECT 
        *,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS r
    FROM employee       
)

-- SELECT * FROM deptRank;
SELECT 
    dep.name AS Department,
    dr.name AS Employee,
    salary AS Salary
FROM deptRank dr
INNER JOIN department dep
    ON dr.departmentId = dep.id
WHERE r <= 3;