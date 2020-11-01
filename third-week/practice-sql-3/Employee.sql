CREATE TABLE Employee(
	idEmployee varchar(8) NOT NULL,
	name varchar(30) NOT NULL,
	lastName varchar(30) NOT NULL,
	idDept int NOT NULL,
	PRIMARY KEY(idEmployee),
	FOREIGN KEY(idDept) REFERENCES Department(idDept)
)
