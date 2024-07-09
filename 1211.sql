SELECT q1.query_name,
       ROUND(SUM(CAST(q1.rating AS numeric) / CAST(q1.position AS numeric)) / COUNT(*)::numeric, 2) AS quality,
       ROUND(SUM(CASE WHEN q1.rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS poor_query_percentage
FROM Queries AS q1
WHERE
q1.query_name is not null
GROUP BY q1.query_name;