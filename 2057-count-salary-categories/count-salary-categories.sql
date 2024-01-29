# Write your MySQL query statement below

WITH cte1 AS (
    SELECT 'Low Salary' AS category
    UNION
    SELECT 'Average Salary'
    UNION
    SELECT 'High Salary'
),
cte2 AS (
    SELECT
        account_id,
        IF(income < 20000, 'Low Salary', IF(income <= 50000, 'Average Salary', 'High Salary')) AS category
    FROM accounts
)
SELECT
    category,
    COUNT(account_id) AS accounts_count
FROM cte1
LEFT JOIN cte2
    USING (category)
GROUP BY category

