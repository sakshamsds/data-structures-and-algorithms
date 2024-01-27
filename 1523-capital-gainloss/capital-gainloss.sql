# Write your MySQL query statement below

WITH buyCTE AS (
    SELECT 
        stock_name,
        SUM(price) AS buy
    FROM stocks
    WHERE operation = 'Buy'
    GROUP BY stock_name
), sellCTE AS (
    SELECT
        stock_name,
        SUM(price) AS sell
    FROM stocks
    WHERE operation = 'Sell'
    GROUP BY stock_name
)
SELECT 
    stock_name,
    sell - buy AS capital_gain_loss
FROM buyCTE
INNER JOIN sellCTE
    USING(stock_name);