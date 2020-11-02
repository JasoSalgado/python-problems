CREATE TABLE Addresses(
	dni varchar(9) REFERENCES Employees(dni),
	street varchar(50),
	zipCode varchar(5) REFERENCES ZipCodes(zipCode),
	PRIMARY KEY(dni, street, zipCode)
)