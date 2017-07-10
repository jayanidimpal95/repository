
--1
select count(*) from customers

--2
select distinct city from customers

--3
select distinct count(state) from customers

--4
select Customer_id, LOWER(First_Name), UPPER(Last_Name)
from customers
where Customer_id BETWEEN 80 and 150

--5
select Last_Name,LEN( Last_Name)
from customers
where LEN( Last_Name)>9

--6
select State, City , COUNT(*)
FROM customers
group by State, City 

--7
select s.sector_id, max(monthly_payment)
from sectors s, packages p 
where s.sector_id=p.sector_id
group by s.sector_id


--8
select First_Name, Last_Name,monthly_discount,
case
	when monthly_discount>=0 and monthly_discount<=10 then 'A'
	when monthly_discount>=11 and monthly_discount<=20 then 'B'
	when monthly_discount>=21 and monthly_discount<=30 then 'C'
	else 'D'
end
from customers

--9
select * from (
select First_Name, Birth_Date,DATEDIFF(YEAR,Birth_Date,GETDATE()) as age
from customers
)a
where age>50

--10
select * 
from customers
where Join_Date< '01-01-2007'

--11
select Customer_Id,First_Name,State,City,pack_id 
from customers
where pack_id not IN ('27','10','3')

--12
select First_Name,Join_date,monthly_discount,pack_id
from customers
where Last_Name NOT LIKE '%a%'
order by pack_id

--13
select *
from customers
where ( State = 'New York' and monthly_discount BETWEEN 30 AND 40 ) or
(pack_id not IN ('8','19','30') and Join_Date< '01-01-2007')

--14
select First_Name,Last_name, c.pack_id, speed
from customers c, packages p
where c.pack_id=p.pack_id

--15
select First_Name,Last_name, c.pack_id, speed
from customers c, packages p
where c.pack_id=p.pack_id 
and p.pack_id IN ('22','27')
order by Last_name

--16
select Last_name, First_Name, Join_Date
from customers
where monthly_discount<
(select monthly_discount
from customers
where Customer_Id=103
)

--17
select First_Name,Last_name,  Join_Date
from customers
where Join_Date>
(select Join_Date
from customers
where Customer_Id=540)

--18
select First_Name, monthly_discount, p.pack_id, main_phone_num, secondary_phone_num
from customers c, sectors s, packages p
where c.pack_id=p.pack_id and p.sector_id=s.sector_id
and s.sector_name='Business' 

--19
select pack_id, speed, strt_date
from packages
where YEAR(strt_date)=(
select YEAR(strt_date)
from packages
where pack_id=7
)

