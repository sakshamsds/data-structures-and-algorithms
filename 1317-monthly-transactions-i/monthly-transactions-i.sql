# Write your MySQL query statement below

SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    -- trans_date,
    -- YEAR(trans_date) AS year,
    -- MONTH(trans_date) AS month,
    country,
    COUNT(state) AS trans_count,
    SUM(IF(state = 'approved', 1, 0)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM transactions
GROUP BY YEAR(trans_date), MONTH(trans_date), country;