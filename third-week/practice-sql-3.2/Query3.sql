-- List employees that shows name, street and zip code ordered by zip code and dni of two different ways
SELECT name, street, zipCode FROM Employees, Addresses 
WHERE Employees.dni = Addresses.dni ORDER BY zipCode, name
