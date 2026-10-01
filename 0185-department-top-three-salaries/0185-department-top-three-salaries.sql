# Write your MySQL query statement below
with topSalary as(
    select *,
    dense_rank() over(
        partition by departmentId
        order by salary desc
    ) as top_salary
    from Employee
)
select 
    d.name as Department,
    tp.name as Employee,
    tp.salary as Salary
from Department d
join topSalary tp
on d.id = tp.departmentId
where tp.top_salary <= 3