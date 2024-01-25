# Write your MySQL query statement below


WITH cte AS
(
    SELECT
        customer_number,
        COUNT(customer_number) AS num_orders
    FROM orders
    GROUP BY customer_number
)

SELECT customer_number
FROM cte
WHERE num_orders = (
    SELECT MAX(num_orders) FROM cte
);