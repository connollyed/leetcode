-- Write your PostgreSQL query statement below

delete from person where

id in 
(
    select p1.id
    from person as p1, person as p2
    where p1.email = p2.email and p1.id > p2.id and p1.id != p2.id
)