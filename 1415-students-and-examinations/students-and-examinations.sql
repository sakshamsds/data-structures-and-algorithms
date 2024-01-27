# Write your MySQL query statement below

WITH cte AS (
    SELECT *
    FROM students
    CROSS JOIN subjects
),
cte2 AS (
    SELECT 
        *,
        COUNT(*) AS attended_exams
    FROM examinations e
    GROUP BY student_id, subject_name
)

SELECT 
    cte.student_id,
    cte.student_name,
    cte.subject_name,
    CASE WHEN attended_exams IS NULL
            THEN 0
         ELSE attended_exams
    END AS attended_exams
FROM cte
LEFT JOIN cte2
    ON cte.student_id = cte2.student_id
    AND cte.subject_name = cte2.subject_name
ORDER BY cte.student_id, cte.subject_name;