# Write your MySQL query statement below

SELECT 
  customer_number
  # COUNT(customer_number) as num_orders
FROM orders
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1;