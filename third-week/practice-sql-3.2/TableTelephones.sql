CREATE TABLE Telephones(
	dni varchar(9) REFERENCES Employees(dni),
	phone varchar(9) NOT NULL,
	PRIMARY KEY (dni, phone)
)