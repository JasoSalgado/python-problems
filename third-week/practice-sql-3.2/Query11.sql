-- List of average wage and number of employees by population ordered by population
SELECT COUNT(*), AVG(wage), population
FROM Employees, ZipCodes
GROUP BY population
ORDER BY population