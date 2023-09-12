# Write your MySQL query statement below

# group by numbers, have one with single instance, get largest

SELECT MAX(num) as num
FROM (
    SELECT num
    FROM mynumbers
    GROUP BY num
        HAVING COUNT(num) = 1
) cte


