# Write your MySQL query statement below

SELECT
    employee_id
FROM employees
LEFT JOIN salaries
    USING (employee_id)
WHERE salary IS NULL
UNION
SELECT
    employee_id
FROM salaries
LEFT JOIN employees
    USING (employee_id)
WHERE name IS NULL
ORDER BY employee_id;