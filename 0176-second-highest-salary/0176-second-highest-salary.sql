# Write your MySQL query statement below
with cte as(
    select 
        id,
        salary,
        dense_rank() over(
            order by salary desc
        ) as rnk
    from Employee
)
select min(salary) as SecondHighestSalary
from cte
where rnk = 2