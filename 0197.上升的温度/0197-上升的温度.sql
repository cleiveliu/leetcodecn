# Write your MySQL query statement below
select distinct w2.Id 
from Weather w1, Weather w2
where to_days(w1.RecordDate) + 1 = to_days(w2.RecordDate)
and w1.Temperature < w2.Temperature
;