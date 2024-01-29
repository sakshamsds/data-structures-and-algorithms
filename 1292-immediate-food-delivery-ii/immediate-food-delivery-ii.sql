# Write your MySQL query statement below

WITH cte AS (
    SELECT
        customer_id,
        MIN(order_date) AS order_date
    FROM delivery
    GROUP BY customer_id
),
cte2 AS (
    SELECT 
        customer_id,
        order_date,
        customer_pref_delivery_date
    FROM cte
    INNER JOIN delivery
        USING (customer_id, order_date)
)
SELECT
    ROUND(AVG(IF(order_date = customer_pref_delivery_date, 100, 0)), 2) AS immediate_percentage
FROM cte2;