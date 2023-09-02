# # Write your MySQL query statement below

# SELECT score
# FROM scores
# ORDER BY score DESC;

# RANK would produce gaps
# DENSE_RANK doesn't produce rank

# SELECT 
#   score,
#   DENSE_RANK() OVER (ORDER BY score DESC) as "Rank"
#   # RANK() OVER (ORDER BY score DESC) as "Rank"
# FROM scores;

# count score greater than current

SELECT
  score,
  (SELECT COUNT(DISTINCT score) FROM scores WHERE org_s.score <= score) as 'rank'
FROM scores org_s
ORDER BY score DESC;