# Write your MySQL query statement below

# common table expression, more efficient than subquery

WITH cte AS
(SELECT 
  customer_number,
  COUNT(customer_number) as num_orders
FROM orders
GROUP BY customer_number)

SELECT customer_number
FROM cte
WHERE num_orders = (SELECT MAX(num_orders) FROM cte)


# SELECT 
#   customer_number
#   # COUNT(customer_number) as num_orders
# FROM orders
# GROUP BY customer_number
# ORDER BY COUNT(customer_number) DESC
# LIMIT 1;