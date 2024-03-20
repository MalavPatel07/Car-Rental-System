CREATE DATABASE  IF NOT EXISTS `car_rental_system` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `car_rental_system`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: car_rental_system
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `billing_penalty`
--

DROP TABLE IF EXISTS `billing_penalty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `billing_penalty` (
  `ReservationID` int NOT NULL,
  `PenaltyID` int NOT NULL,
  KEY `ReservationID` (`ReservationID`),
  KEY `PenaltyID` (`PenaltyID`),
  CONSTRAINT `billing_penalty_ibfk_1` FOREIGN KEY (`ReservationID`) REFERENCES `car_reservation` (`ReservationID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `billing_penalty_ibfk_2` FOREIGN KEY (`PenaltyID`) REFERENCES `penalty` (`PenaltyID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `billing_penalty`
--

LOCK TABLES `billing_penalty` WRITE;
/*!40000 ALTER TABLE `billing_penalty` DISABLE KEYS */;
INSERT INTO `billing_penalty` VALUES (5,7),(15,13),(15,12),(15,5),(15,9),(15,22),(12,8),(3,8),(4,8),(5,10);
/*!40000 ALTER TABLE `billing_penalty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_category`
--

DROP TABLE IF EXISTS `car_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_category` (
  `CarCategoryID` int NOT NULL AUTO_INCREMENT,
  `CarCategoryType` varchar(45) NOT NULL,
  `SeatingCapacity` int NOT NULL,
  `CarFixedCost` float NOT NULL,
  PRIMARY KEY (`CarCategoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_category`
--

LOCK TABLES `car_category` WRITE;
/*!40000 ALTER TABLE `car_category` DISABLE KEYS */;
INSERT INTO `car_category` VALUES (1,'Sedan',5,50),(2,'SUV',7,70),(3,'Truck',3,80),(4,'Coupe',2,60),(5,'Hatchback',4,45),(6,'Convertible',2,75),(7,'Crossover',5,55),(8,'Compact',4,48),(9,'Electric',5,90),(10,'Luxury Sedan',4,120),(11,'Luxury SUV',6,150),(12,'Sports Car',2,100),(13,'Executive',5,130),(14,'Compact SUV',5,65),(15,'Van',8,80),(16,'Hybrid',5,85),(17,'Midsize',5,60),(18,'Full-size',6,70),(19,'Wagon',5,55),(20,'Minivan',7,75);
/*!40000 ALTER TABLE `car_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car_reservation`
--

DROP TABLE IF EXISTS `car_reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `car_reservation` (
  `ReservationID` int NOT NULL AUTO_INCREMENT,
  `CustomerID` int NOT NULL,
  `CarID` int NOT NULL,
  `InsuranceID` int NOT NULL,
  `DiscountID` int NOT NULL,
  `PickUpLocation` int NOT NULL,
  `DropoffLocation` int NOT NULL,
  `PickUpTime` datetime NOT NULL,
  `DropoffTime` datetime NOT NULL,
  `ActualDropoffTime` datetime DEFAULT NULL,
  `BillingDate` date NOT NULL,
  `TotalCost` float NOT NULL,
  PRIMARY KEY (`ReservationID`),
  KEY `CustomerID` (`CustomerID`),
  KEY `CarID` (`CarID`),
  KEY `PickUpLocation` (`PickUpLocation`),
  KEY `DropoffLocation` (`DropoffLocation`),
  KEY `InsuranceID` (`InsuranceID`),
  KEY `DiscountID` (`DiscountID`),
  CONSTRAINT `car_reservation_ibfk_1` FOREIGN KEY (`CustomerID`) REFERENCES `customers` (`CustomerID`),
  CONSTRAINT `car_reservation_ibfk_2` FOREIGN KEY (`CarID`) REFERENCES `cars` (`CarID`),
  CONSTRAINT `car_reservation_ibfk_3` FOREIGN KEY (`PickUpLocation`) REFERENCES `location` (`LocationID`),
  CONSTRAINT `car_reservation_ibfk_4` FOREIGN KEY (`DropoffLocation`) REFERENCES `location` (`LocationID`),
  CONSTRAINT `car_reservation_ibfk_5` FOREIGN KEY (`InsuranceID`) REFERENCES `insurance` (`InsuranceID`),
  CONSTRAINT `car_reservation_ibfk_6` FOREIGN KEY (`DiscountID`) REFERENCES `discount` (`DiscountID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_reservation`
--

LOCK TABLES `car_reservation` WRITE;
/*!40000 ALTER TABLE `car_reservation` DISABLE KEYS */;
INSERT INTO `car_reservation` VALUES (2,1,1,1,1,1,2,'2023-03-04 12:00:00','2023-03-05 12:00:00','2023-03-06 12:00:00','2023-03-04',157.5),(3,2,2,2,2,2,3,'2023-03-03 04:30:00','2023-04-04 10:30:00','2023-04-05 12:00:00','2023-03-03',297.55),(4,3,3,3,3,3,4,'2023-03-07 23:00:00','2023-03-09 01:00:00',NULL,'2023-03-07',160),(5,4,4,4,4,4,5,'2023-07-29 20:00:00','2023-08-01 01:30:00',NULL,'2023-07-29',150),(6,6,6,6,6,6,7,'2023-07-29 20:00:00','2023-08-01 01:30:00',NULL,'2023-07-29',240),(8,8,8,8,8,8,9,'2023-05-14 02:00:00','2023-05-15 01:30:00',NULL,'2023-05-14',70),(9,9,9,9,9,9,10,'2023-08-14 06:00:00','2023-08-16 01:30:00',NULL,'2023-08-14',160),(11,11,11,11,11,11,12,'2023-08-07 11:15:00','2023-08-08 23:15:00',NULL,'2023-08-07',70),(12,13,13,13,13,13,14,'2023-04-06 01:05:00','2023-04-07 23:59:00',NULL,'2023-04-06',50),(13,14,14,14,14,14,15,'2021-11-01 15:00:00','2021-11-02 15:00:00',NULL,'2021-11-01',70),(14,15,15,15,15,15,16,'2020-06-10 09:00:00','2020-06-12 15:00:00',NULL,'2020-06-10',160),(15,16,16,1,1,16,17,'2020-10-10 08:00:00','2020-10-12 12:00:00',NULL,'2020-10-10',100),(16,17,17,2,12,18,19,'2020-09-01 12:00:00','2020-09-02 12:00:00',NULL,'2020-09-01',70),(17,1,6,1,1,1,1,'2023-12-08 12:00:00','2023-12-09 12:00:00',NULL,'2023-12-08',80);
/*!40000 ALTER TABLE `car_reservation` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_CheckCarAvailability_BeforeInsert` BEFORE INSERT ON `car_reservation` FOR EACH ROW BEGIN
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
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_CheckDropOffTime_BeforeInsert` BEFORE INSERT ON `car_reservation` FOR EACH ROW BEGIN
    DECLARE result INT;
 
    SET result = fn_CheckDropOffTime(NEW.PickupTime, NEW.DropoffTime);
 
    IF result > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Pickup time should be greater than Dropoff time, please check the dates and times.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_insert_billing` BEFORE INSERT ON `car_reservation` FOR EACH ROW BEGIN
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
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_CheckDropOffTime_BeforeUpdate` BEFORE UPDATE ON `car_reservation` FOR EACH ROW BEGIN
    DECLARE result INT;
 
    SET result = fn_CheckDropOffTime(NEW.PickupTime, NEW.DropoffTime);
 
    IF result > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Pickup time should be greater than Dropoff time, please check the dates and times.';
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `UpdateBilling` AFTER UPDATE ON `car_reservation` FOR EACH ROW BEGIN
    DECLARE variableCost FLOAT;
    DECLARE totalCost FLOAT;
    
    IF NEW.ActualDropoffTime IS NOT NULL THEN
        SELECT CalculateCosts(NEW.ReservationID) INTO variableCost;
        SET totalCost = variableCost;
        -- You can store the calculated values in another table or log them as needed.
        -- Example: INSERT INTO BillingLog (ReservationID, VariableCost, TotalCost) VALUES (NEW.ReservationID, variableCost, totalCost);
    END IF;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `cars`
--

DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `CarID` int NOT NULL AUTO_INCREMENT,
  `CarBrand` varchar(45) NOT NULL,
  `CarType` varchar(45) NOT NULL,
  `CarCategoryID` int NOT NULL,
  `CarGarageID` int NOT NULL,
  `CarServiceType` varchar(255) NOT NULL,
  `ServiceDueDate` date NOT NULL,
  `CarLicensePlate` varchar(45) NOT NULL,
  `CarModel` varchar(45) NOT NULL,
  `CarModelYear` int NOT NULL,
  `CarAvailability` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`CarID`),
  KEY `CarCategoryID` (`CarCategoryID`),
  KEY `CarGarageID` (`CarGarageID`),
  CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`CarCategoryID`) REFERENCES `car_category` (`CarCategoryID`),
  CONSTRAINT `cars_ibfk_2` FOREIGN KEY (`CarGarageID`) REFERENCES `garage` (`GarageID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES (1,'Toyota','Sedan',1,1,'Regular','2023-06-01','ABC123','Camry',2022,1),(2,'Honda','SUV',2,1,'Premium','2023-05-15','XYZ456','CR-V',2023,1),(3,'Ford','Truck',3,2,'Heavy Duty','2023-07-10','DEF789','F-150',2021,1),(4,'Chevrolet','Coupe',1,1,'Sports','2023-08-20','GHI012','Camaro',2023,1),(5,'Nissan','Hatchback',2,2,'Economy','2023-04-30','JKL345','Versa',2022,0),(6,'BMW','Convertible',3,2,'Luxury','2023-09-05','MNO678','Z4',2022,1),(7,'Mercedes-Benz','Sedan',1,1,'Executive','2023-10-12','PQR901','E-Class',2023,1),(8,'Audi','SUV',2,2,'Premium','2023-11-25','STU234','Q5',2021,1),(9,'Hyundai','Crossover',3,2,'Regular','2023-12-15','VWX567','Tucson',2022,1),(10,'Kia','Sedan',1,2,'Economy','2023-04-15','YZA890','Forte',2021,1),(11,'Tesla','Electric',2,1,'Luxury','2023-05-28','BCD123','Model S',2022,1),(12,'Subaru','SUV',3,1,'Regular','2023-08-02','EFG456','Outback',2023,0),(13,'Mazda','Convertible',1,2,'Sports','2023-09-18','HIJ789','MX-5',2022,1),(14,'Volkswagen','Hatchback',2,2,'Economy','2023-10-30','KLM012','Golf',2021,1),(15,'Volvo','Sedan',3,1,'Executive','2023-11-08','NOP345','S60',2023,1),(16,'Jaguar','Coupe',1,1,'Luxury','2023-12-22','QRS678','F-Type',2022,1),(17,'Lexus','SUV',2,2,'Executive','2024-01-05','TUV901','RX',2023,1),(18,'Chrysler','Van',3,1,'Regular','2024-02-18','WXY234','Pacifica',2022,1),(19,'Buick','Sedan',1,2,'Premium','2024-03-03','ZAB567','Regal',2021,1),(20,'Acura','SUV',2,1,'Executive','2024-04-15','CDE890','MDX',2023,1);
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `CustomerID` int NOT NULL AUTO_INCREMENT,
  `PersonID` int NOT NULL,
  `UserName` varchar(45) NOT NULL,
  `Pass` varchar(255) NOT NULL,
  `DrivingLicense` varchar(255) NOT NULL,
  PRIMARY KEY (`CustomerID`),
  UNIQUE KEY `UserName` (`UserName`),
  KEY `PersonID` (`PersonID`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`PersonID`) REFERENCES `person` (`PersonID`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,2,'qwe','qwe','ABC456'),(2,3,'customer3_username','password3','DEF789'),(3,4,'customer4_username','password4','GHI012'),(4,5,'customer5_username','password5','GHJ012'),(5,6,'customer6_username','password6','JKL345'),(6,7,'customer7_username','password7','MNO678'),(7,8,'customer8_username','password8','PQR901'),(8,9,'customer9_username','password9','STU234'),(9,10,'customer10_username','password10','VWX567'),(10,11,'customer11_username','password11','VXX567'),(11,12,'customer12_username','password12','YZA890'),(12,13,'customer13_username','password13','DEF012'),(13,14,'customer14_username','password14','GHI345'),(14,15,'customer15_username','password15','GII345'),(15,16,'customer16_username','password16','JKL678'),(16,17,'customer17_username','password17','MNO901'),(17,18,'customer18_username','password18','PQR234'),(18,19,'customer19_username','password19','AQR244'),(19,20,'customer20_username','password20','PQS264');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount`
--

DROP TABLE IF EXISTS `discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount` (
  `DiscountID` int NOT NULL AUTO_INCREMENT,
  `DiscountName` varchar(45) NOT NULL,
  `DiscountValidity` date NOT NULL,
  `DiscountPercentage` float NOT NULL,
  PRIMARY KEY (`DiscountID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount`
--

LOCK TABLES `discount` WRITE;
/*!40000 ALTER TABLE `discount` DISABLE KEYS */;
INSERT INTO `discount` VALUES (1,'Summer Sale','2023-06-30',15),(2,'Back to School','2023-08-31',10),(3,'Early Bird Special','2023-09-15',20),(4,'Fall Clearance','2023-11-15',25),(5,'Winter Wonderland','2023-12-15',10),(6,'New Year, New You','2024-01-31',15),(7,'Spring Fling','2024-04-15',10),(8,'Memorial Day Weekend','2024-05-27',20),(9,'Independence Day','2024-07-04',15),(10,'Labor Day Sale','2024-09-02',10),(11,'Oktoberfest','2024-10-05',25),(12,'Black Friday','2024-11-29',30),(13,'Cyber Monday','2024-12-02',35),(14,'Valentine\'s Day','2025-02-14',15),(15,'St. Patrick\'s Day','2025-03-17',10);
/*!40000 ALTER TABLE `discount` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `EmployeeID` int NOT NULL AUTO_INCREMENT,
  `PersonID` int NOT NULL,
  `EmployeeDesignation` varchar(255) NOT NULL,
  `UserName` varchar(45) NOT NULL,
  `Pass` varchar(255) NOT NULL,
  PRIMARY KEY (`EmployeeID`),
  UNIQUE KEY `UserName` (`UserName`),
  KEY `PersonID` (`PersonID`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`PersonID`) REFERENCES `person` (`PersonID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,21,'Employee','employee1_username','password1'),(2,22,'Manager','employee2_username','password2'),(3,23,'Manager','manager1_username','password3'),(4,24,'Employee','employee3_username','password4'),(5,25,'CTO','cto_username','password5'),(6,26,'CEO','ceo_username','password6'),(7,27,'Marketing Lead','marketing_lead_username','password7'),(8,28,'Principal Engineer','engineer_username','password8'),(9,29,'HR','hr_username','password9'),(10,30,'Employee','employee4_username','password10');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `garage`
--

DROP TABLE IF EXISTS `garage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `garage` (
  `GarageID` int NOT NULL AUTO_INCREMENT,
  `GarageName` varchar(255) NOT NULL,
  `GarageLocationID` int NOT NULL,
  PRIMARY KEY (`GarageID`),
  KEY `GarageLocationID` (`GarageLocationID`),
  CONSTRAINT `garage_ibfk_1` FOREIGN KEY (`GarageLocationID`) REFERENCES `location` (`LocationID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `garage`
--

LOCK TABLES `garage` WRITE;
/*!40000 ALTER TABLE `garage` DISABLE KEYS */;
INSERT INTO `garage` VALUES (1,'ABC Auto Care',1),(2,'XYZ Car Services',2);
/*!40000 ALTER TABLE `garage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insurance`
--

DROP TABLE IF EXISTS `insurance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insurance` (
  `InsuranceID` int NOT NULL AUTO_INCREMENT,
  `InsuranceCompany` varchar(45) NOT NULL,
  `InsuranceType` varchar(45) NOT NULL,
  `InsuranceCost` float NOT NULL,
  PRIMARY KEY (`InsuranceID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insurance`
--

LOCK TABLES `insurance` WRITE;
/*!40000 ALTER TABLE `insurance` DISABLE KEYS */;
INSERT INTO `insurance` VALUES (1,'AllianzHaoran','Comprehensive',100),(2,'AIG','Collision',150.5),(3,'GEICO','Liability Only',75.75),(4,'State Farm','Comprehensive',125),(5,'Progressive','Personal Injury',90.25),(6,'Allstate','Comprehensive',120),(7,'Nationwide','Comprehensive',180.5),(8,'Farmers','Comprehensive',135.25),(9,'Liberty Mutual','Collision',110),(10,'Esurance','Personal Injury',100),(11,'Travelers','Comprehensive',140),(12,'USAA','Liability Only',65.5),(13,'Hartford','Comprehensive',155),(14,'MetLife','Personal Injury',95.75),(15,'Mercury','Comprehensive',110.5);
/*!40000 ALTER TABLE `insurance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `LocationID` int NOT NULL AUTO_INCREMENT,
  `Address` varchar(255) NOT NULL,
  `City` varchar(45) NOT NULL,
  `State` varchar(45) NOT NULL,
  `Country` varchar(45) NOT NULL,
  `ZipCode` int NOT NULL,
  PRIMARY KEY (`LocationID`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'2323 Main St','Dallas','TX','USA',75201),(2,'4545 Oak Ave','San Diego','CA','USA',92101),(3,'6767 Pine Rd','Philadelphia','PA','USA',19102),(4,'8989 Maple Blvd','Phoenix','AZ','USA',85004),(5,'111 Pine St','Portland','OR','USA',97204),(6,'222 Elm St','Denver','CO','USA',80202),(7,'333 Oak St','New Orleans','LA','USA',70112),(8,'444 Pine Ave','Nashville','TN','USA',37203),(9,'555 Maple St','Kansas City','MO','USA',64106),(10,'666 Oak Rd','Las Vegas','NV','USA',89109),(11,'777 Pine Blvd','Minneapolis','MN','USA',55401),(12,'888 Maple St','Detroit','MI','USA',48226),(13,'999 Oak St','Salt Lake City','UT','USA',84101),(14,'1212 Pine Ave','San Antonio','TX','USA',78205),(15,'1414 Maple St','Charlotte','NC','USA',28202),(16,'1616 Oak Rd','Indianapolis','IN','USA',46204),(17,'1818 Pine Blvd','Cincinnati','OH','USA',45202),(18,'2020 Maple St','Raleigh','NC','USA',27601),(19,'2222 Oak St','Tampa','FL','USA',33602);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `payment` (
  `PaymentID` int NOT NULL AUTO_INCREMENT,
  `PaymentType` varchar(45) NOT NULL,
  `TransactionID` varchar(255) NOT NULL,
  `PaymentAmount` float NOT NULL,
  `PaymentStatus` varchar(45) NOT NULL,
  `TransactionTime` datetime NOT NULL,
  `ReservationID` int NOT NULL,
  PRIMARY KEY (`PaymentID`),
  KEY `ReservationID` (`ReservationID`),
  CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`ReservationID`) REFERENCES `car_reservation` (`ReservationID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (19,'PayPal','23456',250,'Processed','2023-04-05 14:35:00',4),(20,'Debit Card','34567',128,'Pending','2023-04-04 15:00:00',13),(21,'Credit Card','12341',128,'Processed','2023-04-04 15:05:00',6),(23,'Venmo','56789',840.6,'Pending','2023-08-20 23:00:02',8),(24,'Credit Card','67890',753,'Processed','2023-12-31 20:00:30',9),(26,'Debit Card','89012',350,'Pending','2023-08-23 01:34:34',11),(27,'Venmo','12340',1182.99,'Failed','2023-04-11 20:36:47',8),(28,'PayPal','12342',225,'Processed','2023-03-02 22:10:27',13),(29,'Venmo','12343',525,'Pending','2023-02-09 12:11:02',14),(30,'Google Pay','12344',365,'Processed','2023-01-08 21:14:27',15),(31,'PayPal','12345',322,'Processed','2023-09-05 11:39:30',6),(33,'Debit Card','12348',345,'Processed','2023-10-11 04:10:20',2);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `penalty`
--

DROP TABLE IF EXISTS `penalty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `penalty` (
  `PenaltyID` int NOT NULL AUTO_INCREMENT,
  `PenaltyReason` varchar(255) NOT NULL,
  `PenaltyCost` int NOT NULL,
  PRIMARY KEY (`PenaltyID`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `penalty`
--

LOCK TABLES `penalty` WRITE;
/*!40000 ALTER TABLE `penalty` DISABLE KEYS */;
INSERT INTO `penalty` VALUES (1,'Late payment',100),(2,'Damaged property',500),(3,'Noise violation',200),(4,'Smoking in non-smoking area',300),(5,'Parking violation',150),(6,'Excessive trash',75),(7,'Unauthorized pet',250),(8,'Late dropoff penalty per hour',50),(9,'Damaged interior',25),(10,'Broken windshield',100),(11,'Scratched paint',75),(12,'Missing license plate',50),(13,'Flat tire',80),(14,'Damaged headlight',90),(15,'Broken side mirror',60),(16,'Dented door',110),(17,'Broken taillight',85),(18,'Damaged bumper',120),(19,'Broken rearview mirror',70),(20,'Cracked windshield',95),(21,'Missing side mirror',55),(22,'Broken headlight',100),(23,'Dented hood',125),(24,'Scratched windshield',80),(25,'Graffiti',400),(26,'Haoran Penalty',123);
/*!40000 ALTER TABLE `penalty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `person`
--

DROP TABLE IF EXISTS `person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `person` (
  `PersonID` int NOT NULL AUTO_INCREMENT,
  `PersonFName` varchar(45) NOT NULL,
  `PersonLName` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `PhoneNumber` bigint NOT NULL,
  `LocationID` int NOT NULL,
  `DOB` date NOT NULL,
  PRIMARY KEY (`PersonID`),
  UNIQUE KEY `Email` (`Email`),
  UNIQUE KEY `PhoneNumber` (`PhoneNumber`),
  KEY `LocationID` (`LocationID`),
  CONSTRAINT `person_ibfk_1` FOREIGN KEY (`LocationID`) REFERENCES `location` (`LocationID`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `person`
--

LOCK TABLES `person` WRITE;
/*!40000 ALTER TABLE `person` DISABLE KEYS */;
INSERT INTO `person` VALUES (1,'Ethan','Jones','Male','ethan.jones@drivenow.com',1324567890,1,'1995-04-03'),(2,'Sophia','Smith','Female','sophia.smith@gmail.com',1234567891,2,'1994-06-15'),(3,'Jackson','Taylor','Male','jackson.taylor@hotmail.com',3456789012,3,'1993-07-11'),(4,'Mia','Brown','Female','mia.brown@outlook.com',4567890123,4,'1997-09-02'),(5,'Aiden','Garcia','Male','aiden.garcia@gmail.com',5678901234,5,'1998-11-23'),(6,'Chloe','Lee','Female','chloe.lee@yahoo.com',6789012345,6,'2000-02-14'),(7,'Caleb','Wilson','Male','caleb.wilson@outlook.com',7890123456,7,'2001-03-10'),(8,'Avery','Miller','Female','avery.miller@gmail.com',8901234567,8,'2002-05-18'),(9,'Evelyn','Davis','Female','evelyn.davis@outlook.com',9012345678,9,'2003-06-22'),(10,'William','Clark','Male','william.clark@yahoo.com',1011121314,10,'2004-08-12'),(11,'Oliver','Johnson','Male','oliver.johnson@drivenow.com',1213141516,11,'2005-10-27'),(12,'Isabella','Anderson','Female','isabella.anderson@gmail.com',1314151617,12,'2006-12-31'),(13,'Noah','Martin','Male','noah.martin@outlook.com',1415161718,13,'1998-07-11'),(14,'Emma','Taylor','Female','emma.taylor@yahoo.com',1516171819,14,'1999-09-02'),(15,'Liam','White','Male','liam.white@drivenow.com',1617181920,15,'2000-11-09'),(16,'Aria','Jackson','Female','aria.jackson@gmail.com',1718192021,16,'2002-02-14'),(17,'Ethan','Lee','Male','ethan.lee@outlook.com',1819202122,17,'2003-04-05'),(18,'Zoe','Scott','Female','zoe.scott@yahoo.com',1920212223,18,'2004-06-15'),(19,'Harsh','Vora','Male','harsh@gmail.com',6171231234,9,'1997-08-25'),(20,'Malav','Patel','Male','malav.patel@gmail.com',6171231235,9,'1999-02-28'),(21,'Haoran','Xu','Male','xu@drivenow.com',6171231236,9,'1999-03-25'),(22,'Shreyansh','Patel','Male','shreyansh.patel@gmail.com',6171231237,9,'1998-05-02'),(23,'Vidhan','Pal','Male','vidhan.pal@yahoo.com',6171231238,9,'2000-08-20'),(24,'John','Doe','Male','john.doe@drivenow.com',6171231239,15,'1990-08-25'),(25,'Jacob','Garcia','Male','jacob.garcia@drivenow.com',2021222324,19,'2005-08-25'),(26,'Emma','Smith','Female','emma.smith@drivenow.com',9876543210,2,'1990-08-15'),(27,'Liam','Johnson','Male','liam.johnson@drivenow.com',6543219870,3,'1988-11-22'),(28,'Olivia','Brown','Female','olivia.brown@drivenow.com',1234567890,4,'1992-05-10'),(29,'Noah','Davis','Male','noah.davis@drivenow.com',9871236540,5,'1993-09-18'),(30,'Ava','Martinez','Female','ava.martinez@drivenow.com',4567990123,6,'1997-02-28'),(31,'William','Taylor','Male','william.taylor@drivenow.com',7892123456,7,'1991-07-14'),(32,'Will','Tay','Male','wil.tay@servicenow.com',8892123456,7,'1991-08-14');
/*!40000 ALTER TABLE `person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'car_rental_system'
--
/*!50003 DROP FUNCTION IF EXISTS `CalculateCosts` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `CalculateCosts`(m_reservationID INT) RETURNS float
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `CalculatePenaltyAmount` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `CalculatePenaltyAmount`(m_reservationID INT) RETURNS float
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `CheckAgeRequirement` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `CheckAgeRequirement`(m_personID INT) RETURNS tinyint(1)
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `fn_CheckDropOffTime` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `fn_CheckDropOffTime`(
    PickupTime DATETIME,
    DropoffTime DATETIME
) RETURNS int
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `AddInsurance` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddInsurance`(IN insuranceCompany VARCHAR(45), IN insuranceType VARCHAR(45), IN insuranceCost FLOAT)
BEGIN
	INSERT INTO Insurance (InsuranceCompany, InsuranceType, InsuranceCost) VALUES (insuranceCompany, insuranceType, insuranceCost);
    SELECT CONCAT('Insurance record added successfully.') AS Message;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `CancelReservation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `CancelReservation`(IN m_reservationID INT)
BEGIN
    DELETE FROM Car_Reservation WHERE ReservationID = m_reservationID; 
    SELECT 'Reservation cancelled successfully.' AS Message;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `CreateDiscount` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `CreateDiscount`(IN m_discountName VARCHAR(45), IN m_discountValidity DATE, IN m_discountPercentage FLOAT)
BEGIN
    INSERT INTO Discount (DiscountName, DiscountValidity, DiscountPercentage)
    VALUES (m_discountName, m_discountValidity, m_discountPercentage);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `DeleteCar` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `DeleteCar`(IN p_car_id INT)
BEGIN
    -- Delete the car based on the provided car_id
    DELETE FROM cars WHERE CarID = p_car_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `DeleteDiscount` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `DeleteDiscount`(IN m_discountID INT)
BEGIN
    DELETE FROM Discount WHERE DiscountID = m_discountID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `DeleteInsurance` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `DeleteInsurance`(IN m_insuranceID INT)
BEGIN
    DELETE FROM Insurance WHERE InsuranceID = m_insuranceID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `DeletePenalty` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `DeletePenalty`(IN p_PenaltyID INT)
BEGIN
    DELETE FROM Penalty WHERE PenaltyID = p_PenaltyID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetAllAvailableCars` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetAllAvailableCars`()
BEGIN
    SELECT c.CarBrand,c.CarType,c.CarModel,cc.CarFixedCost AS CarCost
    
    FROM Cars c
    JOIN
		Car_Category cc ON c.CarCategoryID = cc.CarCategoryID
    WHERE CarAvailability = 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetAllCars` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetAllCars`()
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetAllInsurances` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetAllInsurances`()
BEGIN
    SELECT * FROM Insurance;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetAllReservations` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetAllReservations`()
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetCustomerInfo` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetCustomerInfo`()
BEGIN
    Select CustomerID, PersonFName, PersonLName, Email, PhoneNumber, DrivingLicense 
    From Customers 
    Join Person
    ON Customers.PersonID = Person.PersonID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetInsuranceByID` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetInsuranceByID`(IN m_insuranceID INT)
BEGIN
    SELECT * FROM Insurance WHERE InsuranceID = m_insuranceID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetPenalty` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetPenalty`(IN p_PenaltyID INT)
BEGIN
    SELECT * FROM Penalty WHERE PenaltyID = p_PenaltyID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `GetReservationDetails` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetReservationDetails`(IN reservationID INT)
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `InsertBillingPenalty` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertBillingPenalty`(IN p_ReservationID INT,IN p_PenaltyID INT)
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `InsertPenalty` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `InsertPenalty`(IN p_PenaltyReason VARCHAR(255), IN p_PenaltyCost INT)
BEGIN
    INSERT INTO Penalty (PenaltyReason, PenaltyCost)
    VALUES (p_PenaltyReason, p_PenaltyCost);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `LocationBasedAnalytics` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `LocationBasedAnalytics`()
BEGIN
    -- Generate analytics based on location
    SELECT
        l.City,
        COUNT(cr.ReservationID) AS ReservationCount,
        SUM(cr.TotalCost) AS TotalRevenue
    FROM Car_Reservation cr
    INNER JOIN Location l ON cr.PickUpLocation = l.LocationID
    GROUP BY l.City;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `maintainupdatecar` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `maintainupdatecar`(in m2_carID int, IN m2_serviceType VARCHAR(255),m2_Datechange date)
begin
	UPDATE Cars
    SET ServiceDueDate = m2_Datechange,CarServiceType=m2_serviceType
    WHERE CarID = m2_carID;
    SELECT 'Car maintenance information updated successfully.' AS Message;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `PayBill` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `PayBill`(IN reservationID INT, IN paymentType VARCHAR(45), IN transactionID VARCHAR(255), IN paymentAmount FLOAT, IN paymentStatus VARCHAR(45), IN transactionTime DATETIME)
BEGIN
    -- Perform payment processing and update related tables
    INSERT INTO Payment (PaymentType, TransactionID, PaymentAmount, PaymentStatus, TransactionTime, ReservationID)
    VALUES (paymentType, transactionID, paymentAmount, paymentStatus, transactionTime, reservationID);
 
    SELECT 'Payment processed successfully.' AS Message;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `PopularCarCategories` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `PopularCarCategories`()
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ReadAllDiscounts` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ReadAllDiscounts`()
BEGIN
    SELECT * FROM Discount;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ReadDiscountByID` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ReadDiscountByID`(IN m_discountID INT)
BEGIN
    SELECT * FROM Discount WHERE DiscountID = m_discountID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ReserveCar` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ReserveCar`(IN customerID INT, IN carID INT, IN insuranceID INT, IN discountID INT, IN pickUpLocation INT, IN dropOffLocation INT, IN pickUpTime DATETIME, IN dropOffTime DATETIME)
BEGIN
    -- Perform necessary operations to reserve a car
    INSERT INTO Car_Reservation (CustomerID, CarID, InsuranceID, DiscountID, PickUpLocation, DropoffLocation, PickUpTime, DropoffTime, ActualDropoffTime, BillingDate, TotalCost)
    VALUES (customerID, carID, insuranceID, discountID, pickUpLocation, dropOffLocation, pickUpTime, dropOffTime, NULL, NULL, 0);
 
    SELECT 'Car reserved successfully.' AS Message;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `ToggleCarsAvailability` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `ToggleCarsAvailability`(IN checkDate DATE)
BEGIN
    UPDATE Cars
    SET CarAvailability = CASE
        WHEN checkDate >= ServiceDueDate THEN 0
        ELSE 1
    END;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateActualDropoffTime` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateActualDropoffTime`(IN m_reservationID INT, IN m_actualDropoffTime DATETIME)
BEGIN
    UPDATE Car_Reservation
    SET ActualDropoffTime = m_actualDropoffTime
    WHERE ReservationID = m_reservationID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateCarDetails` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateCarDetails`(
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateCustomerInformation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateCustomerInformation`(IN m_personID INT, IN newEmail VARCHAR(45), IN newPhoneNumber BIGINT)
BEGIN
    -- Update customer information
    UPDATE Person
    SET PhoneNumber = newPhoneNumber, Email = newEmail
    WHERE PersonID = m_personID;

    SELECT 'Customer information updated successfully.' AS Message;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateDiscount` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateDiscount`(IN m_discountID INT, IN newDiscountName VARCHAR(45), IN newDiscountValidity DATE, IN newDiscountPercentage FLOAT)
BEGIN
    UPDATE Discount
    SET
        DiscountName = newDiscountName,
        DiscountValidity = newDiscountValidity,
        DiscountPercentage = newDiscountPercentage
    WHERE
        DiscountID = m_discountID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateInsurance` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateInsurance`(IN m_insuranceID INT, IN newInsuranceCompany VARCHAR(45), IN newInsuranceType VARCHAR(45), IN newInsuranceCost FLOAT)
BEGIN
    UPDATE Insurance
    SET
        InsuranceCompany = newInsuranceCompany,
        InsuranceType = newInsuranceType,
        InsuranceCost = newInsuranceCost
    WHERE
        InsuranceID = m_insuranceID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdatePenalty` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdatePenalty`(IN p_PenaltyID INT, IN p_PenaltyReason VARCHAR(255), IN p_PenaltyCost INT)
BEGIN
    UPDATE Penalty
    SET PenaltyReason = p_PenaltyReason,
        PenaltyCost = p_PenaltyCost
    WHERE PenaltyID = p_PenaltyID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateReservation` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateReservation`(IN m_reservationID INT, IN newPickUpLocation INT, IN newDropOffLocation INT, IN newPickUpTime DATETIME, IN newDropOffTime DATETIME)
BEGIN
    -- Perform necessary operations to update a reservation
    UPDATE Car_Reservation
    SET PickUpLocation = newPickUpLocation,
        DropoffLocation = newDropOffLocation,
        PickUpTime = newPickUpTime,
        DropoffTime = newDropOffTime
    WHERE ReservationID = m_reservationID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `UpdateTotalCost` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateTotalCost`(m_reservationID INT, newTotalCost FLOAT)
BEGIN
    -- Update the TotalCost in Car_Reservation table
    UPDATE Car_Reservation
    SET TotalCost = newTotalCost
    WHERE ReservationID = m_reservationID;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-08 21:08:52
