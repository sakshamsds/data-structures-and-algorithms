# Write your MySQL query statement below

SELECT
    query_name,
    ROUND(AVG(rating/position), 2) as quality,
    ROUND(AVG(CASE 
                    WHEN rating < 3
                        THEN 1
                    ELSE 0
                END) * 100, 2) as poor_query_percentage
FROM queries
GROUP BY query_name
    HAVING query_name IS NOT NULL;