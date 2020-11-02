-- List of employees that shows name, dni, street, population, province, zip code and phone ordered by name
SELECT name, Employees.dni, street, population, province, ZipCodes.zipCode, phone
FROM Employees, Addresses, ZipCodes, Telephones
ORDER BY name