# Write your MySQL query statement below


SELECT student_id, student_name, subject_name, COUNT(e.student_id) as attended_exams
FROM students st
CROSS JOIN subjects su
LEFT JOIN examinations e
    USING (student_id, subject_name)
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name;