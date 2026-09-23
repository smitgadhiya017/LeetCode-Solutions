# Write your MySQL query statement below
select person_name
from Queue q1
where (
    select sum(q2.weight)
    from Queue q2
    where q2.turn <= q1.turn
) <= 1000
order by q1.turn desc
limit 1
