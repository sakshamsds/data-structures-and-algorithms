# Write your MySQL query statement below

SELECT 
    e2.name as Employee
    # e1.salary as e_salary,
    # e2.salary as m_salary,
    # e1.name as e_name,
    # e2.name as m_name
FROM employee e1
INNER JOIN employee e2
    ON e1.id = e2.managerid
WHERE e1.salary < e2.salary