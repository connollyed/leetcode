
select distinct(author_id) as id
from Views as A
where
author_id = viewer_id
order by id;