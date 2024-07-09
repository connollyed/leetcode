-- Write your PostgreSQL query statement below

select * from users
where mail ~ '^[a-zA-Z](\w|\d|\.|_|-)*@leetcode(\.)com$'