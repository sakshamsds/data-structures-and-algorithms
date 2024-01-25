# Write your MySQL query statement below

WITH cte AS (
    SELECT *
    FROM students
    CROSS JOIN subjects
),
cte2 as (
    SELECT 
        student_id,
        subject_name,
        COUNT(subject_name) AS attended_exams
    FROM examinations
    GROUP BY student_id, subject_name
)
SELECT 
    cte.student_id,
    cte.student_name,
    cte.subject_name,
    CASE WHEN attended_exams IS NULL
            THEN 0
         ELSE attended_exams
    END as attended_exams
FROM cte
LEFT JOIN cte2
    USING (student_id, subject_name)
ORDER BY student_id, subject_name;