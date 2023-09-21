# Write your MySQL query statement below

WITH cte AS(
  SELECT *
  FROM students
  CROSS JOIN subjects
)
# SELECT * FROM cte;

SELECT 
  cte.student_id,
  cte.student_name,
  cte.subject_name,
  COUNT(e.subject_name) as attended_exams
FROM cte
LEFT JOIN examinations e
  ON cte.student_id = e.student_id
    AND cte.subject_name = e.subject_name
GROUP BY cte.student_id, cte.subject_name
ORDER BY cte.student_id, cte.subject_name


