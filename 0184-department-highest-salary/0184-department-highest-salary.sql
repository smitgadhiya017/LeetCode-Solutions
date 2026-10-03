with Highest_salary as(
    select *,
    dense_rank() over(
        partition by departmentId
        order by salary desc
    ) as rnk
    from Employee
)
select 
    d.name as Department,
    h.name as Employee,
    h.salary as Salary
from Department d
join Highest_salary h
on d.id = h.departmentId
where rnk = 1