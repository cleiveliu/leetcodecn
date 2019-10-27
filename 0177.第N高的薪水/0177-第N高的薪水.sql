CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  set N = N -1;
  RETURN (
      # Write your MySQL query statement below.
      select ifnull((select distinct Salary
                    from Employee
                    order by Salary Desc
                    limit N,1)
                   ,null)
      as SecondHighestSalary
      
  );
END