# Write your MySQL query statement below
select firstName, lastName, city, state
from Person 
left join Address
ON Person.personId = Address.personId;

-- left join - for rows not on left side we put NULL