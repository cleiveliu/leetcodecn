select ifnull((select distinct Salary 
               from Employee
               order by Salary Desc
               limit 1,1)
                ,null)
as SecondHighestSalary;