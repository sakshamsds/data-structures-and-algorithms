# Write your MySQL query statement below

SELECT 
    name,
    SUM(amount) AS balance
FROM users u
INNER JOIN transactions
    USING (account)
GROUP BY account
    HAVING balance > 10000;