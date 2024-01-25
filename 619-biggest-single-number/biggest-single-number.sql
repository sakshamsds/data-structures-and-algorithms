# Write your MySQL query statement below


SELECT 
    MAX(num) as num
FROM (SELECT *
    FROM mynumbers
    GROUP BY num
        HAVING COUNT(num) = 1) single_num;