# Write your MySQL query statement below

SELECT 
    query_name,
    ROUND(AVG(rating/position), 2) quality,
    ROUND(SUM(rating < 3)/count(query_name) * 100, 2) as poor_query_percentage
FROM queries
GROUP BY query_name
    HAVING query_name IS NOT NULL;