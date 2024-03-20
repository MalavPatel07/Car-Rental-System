-- drop function CheckAgeRequirement;

-- Function to check the age
DELIMITER //
 
CREATE FUNCTION CheckAgeRequirement(m_personID INT)
RETURNS BOOLEAN
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE age INT;
 
    SELECT TIMESTAMPDIFF(YEAR, DOB, CURDATE()) INTO age
    FROM Person
    WHERE PersonID = m_personID;
    IF age < 18 THEN
        RETURN 0;
    ELSE
        RETURN 1;
    END IF;
END //
 
DELIMITER ;

-- select * from person;

-- INSERT INTO Person (PersonFName, PersonLName, Gender, Email, PhoneNumber, LocationID, DOB)
-- VALUES
-- ('Malav', 'Young', 'Male', 'young.malav@drivenow.com', 1324567800, 1, '2023-04-03');

-- select CheckAgeRequirement(1);
 
 
-- Function to check the drop-off time
DELIMITER //
 
CREATE FUNCTION fn_CheckDropOffTime
(
    PickupTime DATETIME,
    DropoffTime DATETIME
)
RETURNS INT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE result INT;
 
    IF (PickupTime > DropoffTime) THEN
        SET result = 1;
    ELSE
        SET result = 0;
    END IF;
 
    RETURN result;
END //
 
DELIMITER ;
 
 
 -- drop function CalculatePenaltyAmount;
-- Function to calculate penalty amount for a given reservation ID
DELIMITER //
CREATE FUNCTION CalculatePenaltyAmount(m_reservationID INT)
RETURNS FLOAT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE totalPenalty FLOAT;

    -- Initialize totalPenalty to 0
    SET totalPenalty = 0;

    -- Check if there is any penalty attached to the reservation in Billing_Penalty
    SELECT COALESCE(SUM(P.PenaltyCost), 0) INTO totalPenalty
    FROM Billing_Penalty BP
    INNER JOIN Penalty P ON BP.PenaltyID = P.PenaltyID
    WHERE BP.ReservationID = m_reservationID;

    -- Check if the totalPenalty is not NULL (no penalty attached)
    IF totalPenalty IS NOT NULL THEN
        -- Add the penaltyCost for each penalty reason
        SELECT COALESCE(SUM(PenaltyCost), 0) INTO totalPenalty
        FROM Penalty
        WHERE PenaltyID IN (SELECT PenaltyID FROM Billing_Penalty WHERE ReservationID = m_reservationID);
    END IF;

    RETURN totalPenalty;
END //
DELIMITER ;

 
 
 
 -- drop function CalculateCosts;
DELIMITER //
CREATE FUNCTION CalculateCosts(m_reservationID INT)
RETURNS FLOAT
READS SQL DATA
DETERMINISTIC
BEGIN
    DECLARE insuranceCost FLOAT;
    DECLARE discountPercentage FLOAT;
    DECLARE penaltyAmount FLOAT;
    DECLARE fixedCost FLOAT;
    DECLARE taxes FLOAT;
    DECLARE variableCost FLOAT;
    DECLARE totalCost FLOAT;
    DECLARE discountAmount FLOAT;

    SELECT i.InsuranceCost, d.DiscountPercentage, ck.CarFixedCost
    INTO insuranceCost, discountPercentage, fixedCost
    FROM Car_Reservation cr
    INNER JOIN Insurance i ON cr.InsuranceID = i.InsuranceID
    INNER JOIN Discount d ON cr.DiscountID = d.DiscountID
    INNER JOIN Cars b ON cr.CarId = b.CarId
    INNER JOIN Car_category ck ON ck.CarCategoryID = b.CarCategoryID
    WHERE cr.ReservationID = m_reservationID
    LIMIT 1;

    SET penaltyAmount = CalculatePenaltyAmount(m_reservationID);
    SET variableCost = insuranceCost + penaltyAmount;
    SET discountAmount = (discountPercentage / 100) * (fixedCost + variableCost);
    SET taxes = 0.2 * (fixedCost + variableCost);
    SET totalCost = fixedCost + variableCost + taxes - discountAmount;

    RETURN totalCost;
END //
DELIMITER ;

-- select CalculateCosts(16);

 
-- Trigger to check car availability before insert
DELIMITER //
 
CREATE TRIGGER tr_CheckCarAvailability_BeforeInsert
BEFORE INSERT
ON Car_Reservation
FOR EACH ROW
BEGIN
    DECLARE carCount INT;
    SELECT COUNT(*) INTO carCount
    FROM Cars
    WHERE CarID = NEW.CarID
      AND CarID IN (
        SELECT CarID
        FROM Car_Reservation
        WHERE ReservationID <> NEW.ReservationID
          AND (
            (NEW.PickupTime BETWEEN PickupTime AND DropoffTime)
            OR (NEW.DropoffTime BETWEEN PickupTime AND DropoffTime)
            OR (PickupTime BETWEEN NEW.PickupTime AND NEW.DropoffTime)
            OR (DropoffTime BETWEEN NEW.PickupTime AND NEW.DropoffTime)
          )
    );
 
    IF carCount > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Car is not available for reservation within the selected time period.';
    END IF;
END //
 
 
DELIMITER ;



 
 
-- Trigger to check drop-off time before insert
DELIMITER //
 
CREATE TRIGGER tr_CheckDropOffTime_BeforeInsert
BEFORE INSERT
ON Car_Reservation
FOR EACH ROW
BEGIN
    DECLARE result INT;
 
    SET result = fn_CheckDropOffTime(NEW.PickupTime, NEW.DropoffTime);
 
    IF result > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Pickup time should be greater than Dropoff time, please check the dates and times.';
    END IF;
END //
 
DELIMITER ;
 
-- Trigger to check drop-off time before update
DELIMITER //
 
CREATE TRIGGER tr_CheckDropOffTime_BeforeUpdate
BEFORE UPDATE
ON Car_Reservation
FOR EACH ROW
BEGIN
    DECLARE result INT;
 
    SET result = fn_CheckDropOffTime(NEW.PickupTime, NEW.DropoffTime);
 
    IF result > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Pickup time should be greater than Dropoff time, please check the dates and times.';
    END IF;
END //
 
DELIMITER ;
 
-- Trigger to insert data into billing table
DELIMITER //
CREATE TRIGGER tr_insert_billing
BEFORE INSERT
ON Car_Reservation
FOR EACH ROW
BEGIN
    DECLARE carFixedCost FLOAT;
    DECLARE noOfDays INT;
 
    SELECT c.CarFixedCost INTO carFixedCost
    FROM Car_Category c
    INNER JOIN Cars car ON c.CarCategoryID = car.CarCategoryID
    WHERE car.CarID = NEW.CarID;
 
    SET noOfDays = DATEDIFF(NEW.DropoffTime, NEW.PickupTime);
 
    IF noOfDays = 0 THEN
        SET noOfDays = 1;
    END IF;
 
    SET NEW.BillingDate = NEW.PickupTime;
    SET NEW.TotalCost = carFixedCost * noOfDays;
END //
DELIMITER ;
 
 
--  drop trigger UpdateBilling;
 
 
 DELIMITER //
CREATE TRIGGER UpdateBilling
AFTER UPDATE
ON Car_Reservation
FOR EACH ROW
BEGIN
    DECLARE variableCost FLOAT;
    DECLARE totalCost FLOAT;
    
    IF NEW.ActualDropoffTime IS NOT NULL THEN
        SELECT CalculateCosts(NEW.ReservationID) INTO variableCost;
        SET totalCost = variableCost;
        -- You can store the calculated values in another table or log them as needed.
        -- Example: INSERT INTO BillingLog (ReservationID, VariableCost, TotalCost) VALUES (NEW.ReservationID, variableCost, totalCost);
    END IF;
END //
DELIMITER ;

