-- Given the the schema presented below find two actors who cast together the most and list titles of only those movies they were casting together. 
-- Order the result set alphabetically by the movie title.

select count(*) from (select * 
from actor as a 
  join film_actor as fa 
  on a.actor_id = fa.actor_id
  join film as f 
  on fa.film_id = f.film_id) as x