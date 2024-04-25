# Write your MySQL query statement below

SELECT
    product_id,
    product_name
FROM product p
INNER JOIN SALES s
    USING(product_id)
GROUP BY product_id  
    HAVING MIN(sale_date) >= '2019-01-01' AND
        MAX(sale_date) <= '2019-03-31';
