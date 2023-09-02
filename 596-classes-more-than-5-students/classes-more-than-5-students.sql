# Write your MySQL query statement below

SELECT class
FROM courses
GROUP BY class
    HAVING COUNT(student) >= 5

# HAVING is used when we are filtering based on an aggregate value i.e. COUNT(student)
# WHERE is used to filter where filtering is not based on an aggregate value