# Write your MySQL query statement below

SELECT customer_id, COUNT(*) as count_no_trans
FROM visits v
LEFT JOIN transactions t
    ON v.visit_id = t.visit_id 
    WHERE transaction_id IS NULL
    GROUP BY customer_id;