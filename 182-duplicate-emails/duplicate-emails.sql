# Write your MySQL query statement below

# use group by having count > 1

SELECT email as Email
FROM Person
GROUP BY email
    HAVING COUNT(email) > 1;
