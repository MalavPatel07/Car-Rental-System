use car_rental_system;
 
-- drop procedure CancelReservation;
-- used by customer and employee
DELIMITER //
 
CREATE PROCEDURE CancelReservation(IN m_reservationID INT)
BEGIN
    DELETE FROM Car_Reservation WHERE ReservationID = m_reservationID; 
    SELECT 'Reservation cancelled successfully.' AS Message;
END //
 
DELIMITER ;
 
-- Call the CancelReservation stored procedure
-- CALL CancelReservation(33);

select * from car_reservation;

-- drop procedure GetAllReservations;

DELIMITER //

CREATE PROCEDURE GetAllReservations()
BEGIN
    SELECT
        cr.ReservationID,
        cr.CustomerID,
        c.CarBrand,
        c.CarType,
        i.InsuranceCompany AS Insurance,
        d.DiscountName AS DiscountName,
        
        pl.Address AS PickUpLocation,
       
        dl.Address AS DropoffLocation,
        cr.PickUpTime,
        cr.DropoffTime,
        cr.ActualDropoffTime,
        cr.BillingDate,
        cr.TotalCost
    FROM
        Car_Reservation cr
    JOIN
        Cars c ON cr.CarID = c.CarID
	JOIN
		Insurance i ON cr.InsuranceID = i.InsuranceID
	JOIN
		Discount d ON cr.DiscountID = d.DiscountID 
    JOIN
        Location pl ON cr.PickUpLocation = pl.LocationID
    JOIN
        Location dl ON cr.DropoffLocation = dl.LocationID;
END //

DELIMITER ;


-- CALL GetAllReservations();


 
-- used by customer and employee
DELIMITER //
 
CREATE PROCEDURE GetReservationDetails(IN reservationID INT)
BEGIN
    -- Retrieve detailed information about a specific reservation
    SELECT
        cr.ReservationID,
        c.CarBrand,
        c.CarType,
        cr.PickUpTime,
        cr.DropoffTime,
        cr.ActualDropoffTime
    FROM Car_Reservation cr
    INNER JOIN Cars c ON cr.CarID = c.CarID
    WHERE cr.ReservationID = reservationID;
END //
 
DELIMITER ;

-- CALL GetReservationDetails(16) 

-- Drop Procedure UpdateCustomerInformation;
-- used by customer
DELIMITER //

CREATE PROCEDURE UpdateCustomerInformation(IN m_personID INT, IN newEmail VARCHAR(45), IN newPhoneNumber BIGINT)
BEGIN
    -- Update customer information
    UPDATE Person
    SET PhoneNumber = newPhoneNumber, Email = newEmail
    WHERE PersonID = m_personID;

    SELECT 'Customer information updated successfully.' AS Message;
END //

DELIMITER ;

-- CALL UpdateCustomerInformation(3, 'abc@xyz.com', 12345678);

-- used by employee
DELIMITER //
 
CREATE PROCEDURE LocationBasedAnalytics()
BEGIN
    -- Generate analytics based on location
    SELECT
        l.City,
        COUNT(cr.ReservationID) AS ReservationCount,
        SUM(cr.TotalCost) AS TotalRevenue
    FROM Car_Reservation cr
    INNER JOIN Location l ON cr.PickUpLocation = l.LocationID
    GROUP BY l.City;
END //
 
DELIMITER ;
 
-- call LocationBasedAnalytics 

-- used by employee
DELIMITER //
 
CREATE PROCEDURE PopularCarCategories()
BEGIN
    -- Identify the most popular car categories based on reservations
    SELECT
        cc.CarCategoryType,
        COUNT(cr.ReservationID) AS ReservationCount
    FROM Car_Reservation cr
    INNER JOIN Cars c ON cr.CarID = c.CarID
    INNER JOIN Car_Category cc ON c.CarCategoryID = cc.CarCategoryID
    GROUP BY cc.CarCategoryType
    ORDER BY ReservationCount DESC;
END //
 
DELIMITER ;

-- call PopularCarCategories
 
-- used by Employee
DELIMITER //
 
CREATE PROCEDURE AddInsurance(IN insuranceCompany VARCHAR(45), IN insuranceType VARCHAR(45), IN insuranceCost FLOAT)
BEGIN
	INSERT INTO Insurance (InsuranceCompany, InsuranceType, InsuranceCost) VALUES (insuranceCompany, insuranceType, insuranceCost);
    SELECT CONCAT('Insurance record added successfully.') AS Message;
END //
 
DELIMITER ;
 
-- call AddInsurance('malav','full',230)

DELIMITER //
CREATE PROCEDURE GetAllInsurances()
BEGIN
    SELECT * FROM Insurance;
END //
 
-- CALL GetAllInsurances;
 
-- Read a specific Insurance by ID
DELIMITER //
CREATE PROCEDURE GetInsuranceByID(IN m_insuranceID INT)
BEGIN
    SELECT * FROM Insurance WHERE InsuranceID = m_insuranceID;
END //
--  
-- CALL GetInsuranceByID(2);
 

-- Update an Insurance
DELIMITER //
CREATE PROCEDURE UpdateInsurance(IN m_insuranceID INT, IN newInsuranceCompany VARCHAR(45), IN newInsuranceType VARCHAR(45), IN newInsuranceCost FLOAT)
BEGIN
    UPDATE Insurance
    SET
        InsuranceCompany = newInsuranceCompany,
        InsuranceType = newInsuranceType,
        InsuranceCost = newInsuranceCost
    WHERE
        InsuranceID = m_insuranceID;
END //
-- CALL UpdateInsurance(2,'AAA','Full',120)
 
-- Drop PROCEDURE DeleteInsurance;
DELIMITER //
-- Delete an Insurance
CREATE PROCEDURE DeleteInsurance(IN m_insuranceID INT)
BEGIN
    DELETE FROM Insurance WHERE InsuranceID = m_insuranceID;
END //

-- call DeleteInsurance(2);


-- CRUD for penalty

DELIMITER //

CREATE PROCEDURE InsertPenalty(IN p_PenaltyReason VARCHAR(255), IN p_PenaltyCost INT)
BEGIN
    INSERT INTO Penalty (PenaltyReason, PenaltyCost)
    VALUES (p_PenaltyReason, p_PenaltyCost);
END //
DELIMITER ;
 
-- CALL InsertPenalty('Late Payment Malav', 50);
 
DELIMITER //

CREATE PROCEDURE GetPenalty(IN p_PenaltyID INT)
BEGIN
    SELECT * FROM Penalty WHERE PenaltyID = p_PenaltyID;
END //
DELIMITER ;
 
-- CALL GetPenalty(26);
 
DELIMITER //

CREATE PROCEDURE UpdatePenalty(IN p_PenaltyID INT, IN p_PenaltyReason VARCHAR(255), IN p_PenaltyCost INT)
BEGIN
    UPDATE Penalty
    SET PenaltyReason = p_PenaltyReason,
        PenaltyCost = p_PenaltyCost
    WHERE PenaltyID = p_PenaltyID;
END //
DELIMITER ;
 
-- CALL UpdatePenalty(26, 'Late Payment Shiv', 75);
 
 
DELIMITER //

CREATE PROCEDURE DeletePenalty(IN p_PenaltyID INT)
BEGIN
    DELETE FROM Penalty WHERE PenaltyID = p_PenaltyID;
END //

DELIMITER ;
 
-- CALL DeletePenalty(26);

-- used by customer and employee
DELIMITER //

CREATE PROCEDURE ReserveCar(IN customerID INT, IN carID INT, IN insuranceID INT, IN discountID INT, IN pickUpLocation INT, IN dropOffLocation INT, IN pickUpTime DATETIME, IN dropOffTime DATETIME)
BEGIN
    -- Perform necessary operations to reserve a car
    INSERT INTO Car_Reservation (CustomerID, CarID, InsuranceID, DiscountID, PickUpLocation, DropoffLocation, PickUpTime, DropoffTime, ActualDropoffTime, BillingDate, TotalCost)
    VALUES (customerID, carID, insuranceID, discountID, pickUpLocation, dropOffLocation, pickUpTime, dropOffTime, NULL, NULL, 0);
 
    SELECT 'Car reserved successfully.' AS Message;
END //
 
DELIMITER ;
 
-- call ReserveCar(1, 1, 1, 1, 1, 2, '2022-03-04 12:00:00', '2022-03-05 12:00:00')


DELIMITER //

CREATE PROCEDURE UpdateReservation(IN m_reservationID INT, IN newPickUpLocation INT, IN newDropOffLocation INT, IN newPickUpTime DATETIME, IN newDropOffTime DATETIME)
BEGIN
    -- Perform necessary operations to update a reservation
    UPDATE Car_Reservation
    SET PickUpLocation = newPickUpLocation,
        DropoffLocation = newDropOffLocation,
        PickUpTime = newPickUpTime,
        DropoffTime = newDropOffTime
    WHERE ReservationID = m_reservationID;
END //

DELIMITER ;

-- CALL UpdateReservation(1, 3, 4, '2022-03-04 14:00:00', '2022-03-05 14:00:00');


DELIMITER // 
CREATE PROCEDURE InsertBillingPenalty(IN p_ReservationID INT,IN p_PenaltyID INT)

BEGIN
    DECLARE reservationExists INT;
    DECLARE penaltyExists INT;
    
    -- Check if ReservationID exists
    SELECT COUNT(*) INTO reservationExists 
    FROM Car_Reservation
    WHERE ReservationID = p_ReservationID;
 
    -- Check if PenaltyID exists
    SELECT COUNT(*) INTO penaltyExists
    FROM Penalty
    WHERE PenaltyID = p_PenaltyID;
 
    -- If ReservationID or PenaltyID does not exist, raise an error
    IF reservationExists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: ReservationID does not exist';
    END IF;

    IF penaltyExists = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Error: PenaltyID does not exist';
    END IF;
 
    -- If both ReservationID and PenaltyID exist, perform the insertion
    INSERT INTO Billing_Penalty (ReservationID, PenaltyID) VALUES (p_ReservationID, p_PenaltyID);
END //
 
DELIMITER ;


-- call InsertBillingPenalty(18,1);

 
-- used by customer
DELIMITER //
 
CREATE PROCEDURE PayBill(IN reservationID INT, IN paymentType VARCHAR(45), IN transactionID VARCHAR(255), IN paymentAmount FLOAT, IN paymentStatus VARCHAR(45), IN transactionTime DATETIME)
BEGIN
    -- Perform payment processing and update related tables
    INSERT INTO Payment (PaymentType, TransactionID, PaymentAmount, PaymentStatus, TransactionTime, ReservationID)
    VALUES (paymentType, transactionID, paymentAmount, paymentStatus, transactionTime, reservationID);
 
    SELECT 'Payment processed successfully.' AS Message;
END //
 
DELIMITER ;
 
-- call PayBill(2, 'UPI', 14348, 345, 'Processed', '2023-10-11 4:10:20');
 
### Employee Actions:
 
 
 -- Maintain a Car Procedure for Employees:
 
Delimiter //
Create procedure maintainupdatecar(in m2_carID int, IN m2_serviceType VARCHAR(255),m2_Datechange date)
begin
	UPDATE Cars
    SET ServiceDueDate = m2_Datechange,CarServiceType=m2_serviceType
    WHERE CarID = m2_carID;
    SELECT 'Car maintenance information updated successfully.' AS Message;
end // 
DELIMITER ;

-- call maintainupdatecar(2,'normal','2022-04-05');
 
 
-- following all will be called by employee
-- Create a new discount

DELIMITER //
CREATE PROCEDURE CreateDiscount(IN m_discountName VARCHAR(45), IN m_discountValidity DATE, IN m_discountPercentage FLOAT)
BEGIN
    INSERT INTO Discount (DiscountName, DiscountValidity, DiscountPercentage)
    VALUES (m_discountName, m_discountValidity, m_discountPercentage);
END //
 
-- CALL CreateDiscount('MALAV','2023-06-30 18:00:00',200.0);
 

DELIMITER //
CREATE PROCEDURE ReadAllDiscounts()
BEGIN
    SELECT * FROM Discount;
END //
 
-- CALL ReadAllDiscounts;
 
-- Read a specific discount by ID
DELIMITER //
CREATE PROCEDURE ReadDiscountByID(IN m_discountID INT)
BEGIN
    SELECT * FROM Discount WHERE DiscountID = m_discountID;
END //
 
-- CALL ReadDiscountByID(2);
 
 
-- Update a discount
DELIMITER //
CREATE PROCEDURE UpdateDiscount(IN m_discountID INT, IN newDiscountName VARCHAR(45), IN newDiscountValidity DATE, IN newDiscountPercentage FLOAT)
BEGIN
    UPDATE Discount
    SET
        DiscountName = newDiscountName,
        DiscountValidity = newDiscountValidity,
        DiscountPercentage = newDiscountPercentage
    WHERE
        DiscountID = m_discountID;
END //
-- CALL UpdateDiscount(2,'Back to Malav','2023-09-15 09:00:00',12.0)
 
DELIMITER //
-- Delete a discount
CREATE PROCEDURE DeleteDiscount(IN m_discountID INT)
BEGIN
    DELETE FROM Discount WHERE DiscountID = m_discountID;
END //

-- call DeleteDiscount(16);

 
-- Drop PROCEDURE UpdateActualDropoffTime;
-- called by employee to checkin the car
DELIMITER //
 
CREATE PROCEDURE UpdateActualDropoffTime(IN m_reservationID INT, IN m_actualDropoffTime DATETIME)
BEGIN
    UPDATE Car_Reservation
    SET ActualDropoffTime = m_actualDropoffTime
    WHERE ReservationID = m_reservationID;
END //
 
DELIMITER ;

-- call UpdateActualDropoffTime(1, '2022-03-05 15:00:00');

SET SQL_SAFE_UPDATES = 0;
-- Drop PROCEDURE ToggleCarsAvailability;
DELIMITER //
-- used by employee
CREATE PROCEDURE ToggleCarsAvailability(IN checkDate DATE)
BEGIN
    UPDATE Cars
    SET CarAvailability = CASE
        WHEN checkDate >= ServiceDueDate THEN 0
        ELSE 1
    END;
END //

-- call ToggleCarsAvailability('2023-06-01');
Select * from cars;

use car_rental_system;
Drop PROCEDURE GetAllAvailableCars;
-- used by customer
DELIMITER //
 
CREATE PROCEDURE GetAllAvailableCars()
BEGIN
    SELECT c.CarBrand,c.CarType,c.CarModel,cc.CarFixedCost AS CarCost
    
    FROM Cars c
    JOIN
		Car_Category cc ON c.CarCategoryID = cc.CarCategoryID
    WHERE CarAvailability = 1;
END //
 
DELIMITER ;

-- call GetAllAvailableCars;

 

-- update car details
DELIMITER //
CREATE PROCEDURE UpdateCarDetails(
    IN p_CarID INT,
    IN p_CarBrand VARCHAR(45),
    IN p_CarType VARCHAR(45),
    IN p_CarCategoryID INT,
    IN p_CarGarageID INT,
    IN p_CarServiceType VARCHAR(255),
    IN p_ServiceDueDate DATE,
    IN p_CarLicensePlate VARCHAR(45),
    IN p_CarModel VARCHAR(45),
    IN p_CarModelYear INT,
    IN p_CarAvailability BOOLEAN
)
BEGIN
    UPDATE Cars
    SET
        CarBrand = p_CarBrand,
        CarType = p_CarType,
        CarCategoryID = p_CarCategoryID,
        CarGarageID = p_CarGarageID,
        CarServiceType = p_CarServiceType,
        ServiceDueDate = p_ServiceDueDate,
        CarLicensePlate = p_CarLicensePlate,
        CarModel = p_CarModel,
        CarModelYear = p_CarModelYear,
        CarAvailability = p_CarAvailability
    WHERE
        CarID = p_CarID;
END //
DELIMITER ;
 
select * from cars;
 
-- drop procedure DeleteCar;
DELIMITER //
CREATE PROCEDURE DeleteCar(IN p_car_id INT)
BEGIN
    -- Delete the car based on the provided car_id
    DELETE FROM cars WHERE CarID = p_car_id;
END //
DELIMITER ;

-- drop procedure UpdateTotalCost;
DELIMITER //
 
CREATE PROCEDURE UpdateTotalCost(m_reservationID INT, newTotalCost FLOAT)
BEGIN
    -- Update the TotalCost in Car_Reservation table
    UPDATE Car_Reservation
    SET TotalCost = newTotalCost
    WHERE ReservationID = m_reservationID;
END //
 
DELIMITER ;
 
-- CALL UpdateTotalCost(16, 157.5);
select * from cars;

select * from customers;


DELIMITER //
CREATE PROCEDURE GetCustomerInfo()
BEGIN
    Select CustomerID, PersonFName, PersonLName, Email, PhoneNumber, DrivingLicense 
    From Customers 
    Join Person
    ON Customers.PersonID = Person.PersonID;
END //
DELIMITER ;

-- call GetCustomerInfo();

select * from discount;
select * from billing_penalty;


-- drop procedure GetAllCars;

DELIMITER //
CREATE PROCEDURE GetAllCars()
BEGIN
    SELECT
        c.CarID,
        c.CarBrand,
        c.CarType,
        cc.CarFixedCost AS CarCost,
        g.GarageName AS CarGarage,
        c.CarServiceType,
        c.ServiceDueDate,
        c.CarLicensePlate,
        c.CarModel,
        c.CarModelYear,
        c.CarAvailability
    FROM
        Cars c
    JOIN
        Car_Category cc ON c.CarCategoryID = cc.CarCategoryID
    JOIN
        Garage g ON c.CarGarageID = g.GarageID;
END //

DELIMITER ;

-- call GetAllCars();


