# Write your MySQL query statement below

-- SELECT IF(condition, true_result, false_result) AS alias_name
-- FROM table_name;


SELECT
    employee_id,
    IF(MOD(employee_id, 2) = 1 AND SUBSTRING(name, 1, 1) != 'M', salary, 0) AS bonus
FROM employees
ORDER BY employee_id