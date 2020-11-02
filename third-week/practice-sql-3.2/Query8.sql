-- Undo the last query (prove that data are the same as the original table).
UPDATE Employees 
SET wage = wage/10
WHERE wage <= 1900
