# Write your MySQL query statement below

# Solution 1
# find max, then select highest which is not max

# SELECT MAX(salary) as SecondHighestSalary
# FROM employee
# WHERE salary < (SELECT MAX(salary) FROM employee);
# # WHERE salary NOT IN (SELECT MAX(salary) FROM employee); # max return null by definition

# Solution 2, fix for no entry by using subquery

SELECT ( 
  SELECT DISTINCT salary
  FROM employee
  ORDER BY salary DESC
  LIMIT 1 OFFSET 1
) as SecondHighestSalary;

