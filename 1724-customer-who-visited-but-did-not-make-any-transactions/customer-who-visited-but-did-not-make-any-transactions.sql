# Write your MySQL query statement below

SELECT customer_id, COUNT(customer_id) as count_no_trans
FROM visits v
LEFT JOIN transactions t
    USING (visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id;