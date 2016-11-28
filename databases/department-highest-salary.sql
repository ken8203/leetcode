# Write your MySQL query statement below
select Department.Name as Department, Employee.Name as Employee, Employee.Salary as Salary
from Department
inner join Employee on Department.Id=Employee.DepartmentId
where Employee.Salary in (select Max(Salary) from Employee e where e.DepartmentId=Employee.DepartmentId)
