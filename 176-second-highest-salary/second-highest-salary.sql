# Write your MySQL query statement below

# find max, then select highest which is not max

SELECT MAX(salary) as SecondHighestSalary
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee);
# WHERE salary NOT IN (SELECT MAX(salary) FROM employee);