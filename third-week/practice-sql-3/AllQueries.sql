--Getting employee´s name and last name
SELECT name, lastName FROM Employee

-- Getting employee´s last name without repeat
SELECT DISTINCT lastName FROM Employee

-- Getting all data from employees where employee´s last name is López
SELECT * FROM Employee WHERE lastName = 'López'

-- Getting all data where employee´ last name is 'López' and Pérez
SELECT * FROM Employee WHERE lastName = 'López' AND lastName = 'Pérez'

-- Getting all data from employees that work in the department 1 or 3 order by name alphabetically
SELECT * FROM Employee WHERE idDept = 1 or idDept = 3 ORDER BY name ASC

-- Getting employee´s name and last name which name starts with 'H'
SELECT * FROM Employee WHERE name LIKE 'H%'

-- Getting department data which budget is between $50,000 and $70,000
SELECT * FROM Department WHERE budget BETWEEN 50000 AND 70000

-- Getting employees´ id, name and last name that work in the accounting department
SELECT * FROM Employee WHERE idDept = 3  

-- Getting name and last name, as well as the department´s name of each employee that works in the company
SELECT name, lastName, deptName FROM Employee, Department

-- Generate the following views:
-- a) A view denominated Employee with all data from the Employees´ department
CREATE VIEW Employees AS 
SELECT * FROM Department

-- A view denominated Pérez with all employees´ last name 'Pérez'
CREATE VIEW Perez AS 
SELECT lastName FROM Employee WHERE lastName = 'Pérez'

-- A view denominated Big_budgets with departments that have at least a 50,000 budget
CREATE VIEW Big_budget AS
SELECT budget FROM Department WHERE budget >= 50000