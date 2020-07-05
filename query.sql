SELECT Country, count(*) as NotOrdered FROM Customers C left join Orders O on C.CustomerID = O.CustomerID where O.CustomerID is NULL
  Group By Country;


SELECT ProductID, count(Quantity) OrderedQuantity FROM Orders natural join OrderDetails Group By OrderID order by OrderID;


select round(avg(BirthDate)) AverageBirthDate from Employees;


select City, Country, count(*) NomberCustomers from Customers group by City, Country having count(*) > 3;