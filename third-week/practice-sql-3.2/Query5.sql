-- List of employees that that shows name, dni, street, population, province and zip code ordered by name
SELECT name, Employees.dni, street, population, province, ZipCodes.zipCode
FROM Employees, Addresses, ZipCodes
ORDER BY name