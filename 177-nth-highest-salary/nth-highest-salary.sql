CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      # Write your MySQL query statement below.
    #    SELECT (
            SELECT DISTINCT salary
            FROM employee
            ORDER BY salary DESC
            LIMIT 1 OFFSET N
        # ) 
  );
END

# cannot use any calculation in return block


# SELECT (
#     SELECT *
#     FROM employee
#     ORDER BY salary DESC
#     LIMIT 1 OFFSET N
# ) 