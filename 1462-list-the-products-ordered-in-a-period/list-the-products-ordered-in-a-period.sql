# Write your MySQL query statement below

SELECT
    product_name,
    feb_units as unit
FROM (
    SELECT 
        product_id,
        SUM(unit) as feb_units
    FROM orders
    WHERE MONTH(order_date) = 2
            AND YEAR(order_date) = 2020
    GROUP BY product_id
        HAVING feb_units >= 100
) cte
INNER JOIN products
    USING (product_id);