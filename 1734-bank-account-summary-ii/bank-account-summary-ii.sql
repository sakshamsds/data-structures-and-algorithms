# Write your MySQL query statement below

WITH cte AS
(
    SELECT u.name as NAME, SUM(t.amount) as BALANCE
    FROM users u
    INNER JOIN transactions t
        ON u.account = t.account
    GROUP BY u.account
)

SELECT * FROM cte WHERE balance > 10000;