# Write your MySQL query statement below

SELECT 
    e.name as Employee
FROM 
    employee as e,
    employee as m
WHERE 
    e.managerid = m.id
    AND e.salary > m.salary

# SELECT 
#     e2.name as Employee
#     # e1.salary as e_salary,
#     # e2.salary as m_salary,
#     # e1.name as e_name,
#     # e2.name as m_name
# FROM employee e1
# INNER JOIN employee e2
#     ON e1.id = e2.managerid
# WHERE e1.salary < e2.salary