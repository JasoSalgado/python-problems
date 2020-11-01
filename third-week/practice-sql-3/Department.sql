CREATE TABLE Department(
	idDept int NOT NULL identity(1,1) PRIMARY KEY,
	deptName varchar(30) NOT NULL,
	budget money NOT NULL
)
