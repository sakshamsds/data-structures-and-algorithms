# Write your MySQL query statement below

WITH cte AS (
    SELECT 
        customer_number,
        COUNT(*) AS num_orders
    FROM orders
    GROUP BY customer_number
)
SELECT customer_number
FROM cte
WHERE num_orders = (SELECT MAX(num_orders)
                    FROM cte);

-- SELECT 
--     customer_number
-- FROM orders
-- GROUP BY customer_number
-- ORDER BY COUNT(*) DESC
-- LIMIT 1;
