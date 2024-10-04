# Write your MySQL query statement below

# cA intersection cB NOT in cC

WITH cAB AS (
    SELECT
        DISTINCT customer_id
    FROM orders
    WHERE product_name = 'A'

    INTERSECT

    SELECT
        DISTINCT customer_id
    FROM orders
    WHERE product_name = 'B'
),
cABnotC AS (
    SELECT
        customer_id
    FROM cAB 
    WHERE customer_id NOT IN (
        SELECT
            DISTINCT customer_id
        FROM orders
        WHERE product_name = 'C'
    )
)

SELECT 
    customer_id,
    customer_name
FROM customers
INNER JOIN cABnotC
    USING(customer_id)
ORDER BY customer_id;
