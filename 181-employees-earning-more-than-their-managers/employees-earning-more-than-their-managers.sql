# Write your MySQL query statement below

# SELECT 
#     e.name as Employee
# FROM 
#     employee as e,
#     employee as m
# WHERE 
#     e.managerid = m.id
#     AND e.salary > m.salary

SELECT e1.name as Employee
FROM Employee as e1            # need to give alias for self join
INNER JOIN Employee as e2
    ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;


# INNER JOIN, records in both the tables
# LEFT JOIN, records in left + intersection
# we don't neet left join for above, means manager is not present