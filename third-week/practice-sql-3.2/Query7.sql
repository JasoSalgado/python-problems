-- Increase in 10 % the employees´ wage. The wage must not exceed in any case 1.900
Update Employees
SET wage = wage*10
WHERE wage <= 1900