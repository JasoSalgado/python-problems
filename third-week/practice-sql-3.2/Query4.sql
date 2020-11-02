-- List of employees ordered by name, dni, street, zip code, phone in two different ways
-- a) Employees that have phone only
SELECT name, Employees.dni, street, zipCode, phone 
FROM Employees, Addresses, Telephones
ORDER BY name



-- b) Employees that have phone as well as the ones do not
