# sql sucks
select distinct a.Num as ConsecutiveNums
from Logs a,Logs b,Logs c
where a.Num = b.Num and b.Num = c.Num and a.Id + 1 = b.Id and b.Id + 1 = c.Id
;
