select user_id, concat(upper(substring(users.name,1,1)), lower(substring(users.name,2))) as name
from users
order by user_id