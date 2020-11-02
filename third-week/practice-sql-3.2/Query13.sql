-- Add domain integrity restrictions with validity rules (wage must be between 0 and 120.000)
SELECT wage FROM Employees
WHERE wage BETWEEN 0 AND 120000