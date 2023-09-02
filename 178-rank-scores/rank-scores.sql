# # Write your MySQL query statement below

# SELECT score
# FROM scores
# ORDER BY score DESC;

# RANK would produce gaps
# DENSE_RANK doesn't produce rank

SELECT 
  score,
  DENSE_RANK() OVER (ORDER BY score DESC) as "Rank"
  # RANK() OVER (ORDER BY score DESC) as "Rank"
FROM scores;