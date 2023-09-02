# Write your MySQL query statement below

SELECT customers.name as Customers
FROM customers
WHERE customers.id NOT IN 
(
    select customerid from orders
);

# SELECT
#     c.name as Customers
#     # c.id as cid,
#     # o.id as oid
# FROM Customers c
# LEFT JOIN Orders o
#     ON c.id = o.customerId
# WHERE o.id IS NULL;