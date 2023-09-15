# Write your MySQL query statement below

SELECT 
    u.name,
    CASE
        WHEN SUM(r.distance) IS NOT NULL
            THEN SUM(r.distance)
        ELSE 0
    END as travelled_distance
FROM users u
LEFT JOIN rides r
    ON u.id = r.user_id
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name