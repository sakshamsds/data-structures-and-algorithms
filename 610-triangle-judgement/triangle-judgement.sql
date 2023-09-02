# Write your MySQL query statement below

# sum of two sides should be greated than the third side
# a + b > c
# b + c > a
# c + a > b
# if else -> CASE WHEN condition THEN a ELSE b in SQL

# SELECT 
#     *, 
#     CASE 
#         WHEN x+y>z AND y+z>x AND z+x>y THEN 'Yes' 
#         ELSE 'No' 
#     END as triangle
# FROM triangle

SELECT *,
    IF (x+y>z AND y+z>x AND z+x>y, 'Yes', 'No') as triangle
FROM Triangle;