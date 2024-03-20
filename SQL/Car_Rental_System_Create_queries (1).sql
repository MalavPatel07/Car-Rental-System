-- ------ FINAL
 
DROP database if exists Car_Rental_System;
CREATE DATABASE Car_Rental_System;
USE Car_Rental_System;

-- --- -----------------------------LEVEL 1 :-------------------------

-- --LOCATION----
DROP TABLE IF EXISTS Location;
CREATE TABLE Location(
 
	LocationID int auto_increment NOT NULL,
 
	Address varchar(255) NOT NULL,
 
	City varchar(45) NOT NULL,
 
	State varchar(45) NOT NULL,
 
	Country varchar(45) NOT NULL,
 
	ZipCode int NOT NULL,
 
    primary key (LocationID)
 
);
ALTER TABLE Location AUTO_INCREMENT = 1;

-- --PERSON----
DROP TABLE IF EXISTS Person;
CREATE TABLE Person (
 
	PersonID int NOT NULL auto_increment,
 
	PersonFName varchar(45) NOT NULL,
 
	PersonLName varchar(45) NOT NULL,
 
	Gender varchar(45) NOT NULL,
 
	Email varchar(45) NOT NULL UNIQUE,
 
	PhoneNumber bigint NOT NULL UNIQUE,
 
    LocationID int NOT NULL,
 
	foreign key (LocationID) REFERENCES Location(LocationID),
 
	DOB date NOT NULL,
 
    primary key (PersonID)
 
);
ALTER TABLE Person AUTO_INCREMENT = 1;
-- DISCOUNT---
DROP TABLE IF EXISTS Discount;
CREATE TABLE Discount(
 
	DiscountID int auto_increment NOT NULL,
 
	DiscountName varchar(45) NOT NULL,
 
	DiscountValidity date NOT NULL,
 
	DiscountPercentage float NOT NULL,
 
    primary key (DiscountID)
 
);
ALTER TABLE Discount AUTO_INCREMENT = 1;
-- INSURANCE----
DROP TABLE IF EXISTS Insurance;
CREATE TABLE Insurance(
 
	InsuranceID int auto_increment NOT NULL,
 
	InsuranceCompany varchar(45) NOT NULL,
 
	InsuranceType varchar(45) NOT NULL,
 
	InsuranceCost float NOT NULL,
 
    primary key (InsuranceID)
 
);
ALTER TABLE Insurance AUTO_INCREMENT = 1;

  -- PENALTY---
DROP TABLE IF EXISTS Penalty;
CREATE TABLE Penalty(
 
	PenaltyID int auto_increment NOT NULL,
 
	PenaltyReason varchar(255) NOT NULL,
 
	PenaltyCost int NOT NULL,
 
    primary key(PenaltyID)
 
);
ALTER TABLE Penalty AUTO_INCREMENT = 1;
-- --- -----------------------------LEVEL 2 :-------------------------

-- --EMPLOYEE---
DROP TABLE IF EXISTS Employee;
CREATE TABLE Employee (
 
  EmployeeID int auto_increment NOT NULL,
 
  PersonID int NOT NULL,
 
  foreign key (PersonID) REFERENCES Person(PersonID),
 
  EmployeeDesignation varchar(255) NOT NULL,
  UserName VARCHAR(45) NOT NULL UNIQUE,
  Pass VARCHAR(255) NOT NULL,
 
  primary key (EmployeeID)
 
);
ALTER TABLE Employee AUTO_INCREMENT = 1;

-- CUSTOMERS ---
DROP TABLE IF exists Customers;
CREATE TABLE Customers (
 
    CustomerID int auto_increment NOT NULL,

    PersonID int NOT NULL,
 
    UserName VARCHAR(45) NOT NULL UNIQUE,
	Pass VARCHAR(255) NOT NULL,
 
    PRIMARY KEY (CustomerID),
 
    FOREIGN KEY (PersonID) REFERENCES Person(PersonID),
 
 
    DrivingLicense varchar(255) NOT NULL
 
);
ALTER TABLE Customers AUTO_INCREMENT = 1;

 
-- GARAGE---
DROP TABLE IF EXISTS Garage;
CREATE TABLE Garage(
 
    GarageID int NOT NULL auto_increment PRIMARY KEY,
 
    GarageName varchar(255) NOT NULL,
 
    GarageLocationID int NOT NULL,
 
    FOREIGN KEY (GarageLocationID) REFERENCES Location(LocationID)
 
);
ALTER TABLE Garage AUTO_INCREMENT = 1;

-- Car Category---
DROP TABLE IF EXISTS Car_Category;
CREATE TABLE Car_Category(
 
	CarCategoryID int auto_increment NOT NULL PRIMARY KEY,
 
	CarCategoryType varchar(45) NOT NULL,
 
	SeatingCapacity int NOT NULL,
 
	CarFixedCost float NOT NULL
 
);
ALTER TABLE Car_Category AUTO_INCREMENT = 1;

-- --CARS---
DROP TABLE IF EXISTS Cars;
CREATE TABLE Cars(
 
  CarID int NOT NULL auto_increment,
 
  CarBrand varchar(45) NOT NULL,
 
  CarType varchar(45) NOT NULL,
 
  CarCategoryID int NOT NULL,
 
  CarGarageID int NOT NULL,
 
  CarServiceType varchar(255) NOT NULL,
 
  ServiceDueDate date NOT NULL,
 
  CarLicensePlate varchar(45) NOT NULL,
 
  CarModel varchar(45) NOT NULL,
 
  CarModelYear int NOT NULL,
  CarAvailability boolean,
 
  primary key (CarID),
 
  Foreign key (CarCategoryID) REFERENCES Car_Category(CarCategoryID),
 
  Foreign key (CarGarageID) REFERENCES Garage(GarageID) 
);
ALTER TABLE Cars AUTO_INCREMENT = 1;

 
-- - -------------------------------LEVEL 3 :-------------------------
-- -CAR_RESERVATION---
 
DROP TABLE IF EXISTS Car_Reservation;
 
CREATE TABLE Car_Reservation(
 
  ReservationID int NOT NULL auto_increment,
 
  CustomerID int NOT NULL,
 
  CarID int NOT NULL ,
 
  InsuranceID int NOT NULL,
 
  DiscountID int NOT NULL ,
 
  PickUpLocation int NOT NULL ,
 
  DropoffLocation int NOT NULL,
 
  PickUpTime datetime NOT NULL,
 
  DropoffTime datetime NOT NULL,
 
  ActualDropoffTime datetime NULL,
 
  BillingDate date NOT NULL,
 
  TotalCost float NOT NULL,
 
  primary key (ReservationID),
 
  foreign key (CustomerID) REFERENCES Customers(CustomerID),
 
  foreign key (CarID) REFERENCES Cars(CarID),
 
  foreign key (PickUpLocation) REFERENCES Location(LocationID),
 
  foreign key (DropoffLocation)  REFERENCES Location(LocationID),
 
  foreign key (InsuranceID) REFERENCES Insurance(InsuranceID),
 
  foreign key (DiscountID) REFERENCES Discount(DiscountID)
 
  );
  ALTER TABLE Car_Reservation AUTO_INCREMENT = 1;
-- --------------------------------LEVEL 5 :-------------------------
 

-- BILLING_PENALTY----
DROP TABLE IF EXISTS Billing_Penalty;
CREATE TABLE Billing_Penalty(
 
	ReservationID int NOT NULL,
 
	PenaltyID int NOT NULL,
 
    foreign key(ReservationID) REFERENCES Car_Reservation(ReservationID) ON DELETE CASCADE ON UPDATE CASCADE,
 
    foreign key(PenaltyID) REFERENCES Penalty(PenaltyID)
 
);

-- -PAYMENT---
DROP TABLE IF EXISTS Payment;
CREATE TABLE Payment(
 
	PaymentID int auto_increment NOT NULL,
 
	PaymentType varchar(45) NOT NULL,
 
	TransactionID varchar(255) NOT NULL,
 
	PaymentAmount float NOT NULL,
 
	PaymentStatus varchar(45) NOT NULL,
 
	TransactionTime datetime NOT NULL,
 
    primary key (PaymentID),
 
	ReservationID int NOT NULL ,
 
    foreign key(ReservationID) REFERENCES Car_Reservation(ReservationID) ON DELETE CASCADE ON UPDATE CASCADE
 
);
ALTER TABLE Payment AUTO_INCREMENT = 1;