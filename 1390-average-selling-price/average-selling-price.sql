# Write your MySQL query statement below

# SELECT u.product_id, start_date, end_date, purchase_date, price, units
# SELECT u.product_id, ROUND(AVG(price/units), 2) as average_price
SELECT u.product_id, ROUND(SUM(units*price)/SUM(units), 2) as average_price
FROM unitssold u
INNER JOIN prices p
    ON u.product_id = p.product_id
WHERE purchase_date BETWEEN start_date AND end_date
GROUP BY u.product_id;
    