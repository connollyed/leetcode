SELECT MAX(x.num) as num
FROM 
    (
        SELECT num 
        FROM MyNumbers 
        GROUP BY num 
        HAVING COUNT(*) = 1
    ) as x;