with cte as(
    select
        name,
        salary,
        departmentId,
        dense_rank() over(partition by departmentId order by salary desc) as rnk
    from Employee
)
select 
    d.name as Department,
    c.name as Employee,
    c.salary
from cte c
join department d
on c.departmentId = d.id
where rnk = 1;