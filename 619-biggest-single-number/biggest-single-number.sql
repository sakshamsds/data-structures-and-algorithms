# Write your MySQL query statement below

# SELECT MAX(num) as num
# FROM (
#     SELECT num
#     FROM mynumbers
#     GROUP BY num
#         HAVING COUNT(num) = 1
# ) mynum;

WITH cte AS
(
    SELECT num
    FROM mynumbers
    GROUP BY num
        HAVING COUNT(num) = 1
)

# SELECT MAX(num) as num FROM cte;
SELECT 
    CASE 
        WHEN COUNT(num) > 0
            THEN MAX(num)
            ELSE NULL
    END as num
FROM cte;