import mysql.connector
from db_connection import create_db_connection, close_db_connection
from datetime import datetime
import random


def execute_query(connection, query, values, success_message):
    """Generic function to execute a given SQL query with values."""
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
        print(success_message)
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def create_new_location(connection, address, city, state, country, zipcode):
    """Create a new location in the Location table."""
    query = "INSERT INTO Location (Address, City, State, Country, ZipCode) VALUES (%s, %s, %s, %s, %s)"
    values = (address, city, state, country, zipcode)
    execute_query(connection, query, values, "Location added successfully")


def create_new_person(connection, fname, lname, gender, email, phone, location_id, dob):
    """Create a new person in the Person table."""
    query = """
    INSERT INTO Person (PersonFName, PersonLName, Gender, Email, PhoneNumber, LocationID, DOB) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (fname, lname, gender, email, phone, location_id, dob)
    execute_query(connection, query, values, "Person added successfully")


# def create_new_employee(connection, person_id, designation):
#     """Create a new employee in the Employee table."""
#     query = "INSERT INTO Employee (PersonID, EmployeeDesignation) VALUES (%s, %s)"
#     values = (person_id, designation)
#     execute_query(connection, query, values, "Employee added successfully")


def create_new_customer(connection, person_id, driving_license):
    """Create a new customer in the Customers table."""
    query = "INSERT INTO Customers (PersonID, DrivingLicense) VALUES (%s, %s)"
    values = (person_id, driving_license)
    execute_query(connection, query, values, "Customer added successfully")


def create_new_car(connection, brand, type, category_id, garage_id, service_type, service_due_date, license_plate,
                   model, model_year, availability):
    """Create a new car in the Cars table."""
    query = """
    INSERT INTO Cars (CarBrand, CarType, CarCategoryID, CarGarageID, CarServiceType, ServiceDueDate, CarLicensePlate, CarModel, CarModelYear, CarAvailability) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
    brand, type, category_id, garage_id, service_type, service_due_date, license_plate, model, model_year, availability)
    execute_query(connection, query, values, "Car added successfully")


def create_new_car_reservation(connection, customer_id, car_id, insurance_id, discount_id, pickup_location,
                               dropoff_location, pickup_time, dropoff_time):
    """Create a new car reservation in the Car_Reservation table."""
    # query = """
    # INSERT INTO Car_Reservation (CustomerID, CarID, InsuranceID, DiscountID, PickUpLocation, DropoffLocation, PickUpTime, DropoffTime, BillingDate, TotalCost) 
    # VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    # """
    # values = (
    # customer_id, car_id, insurance_id, discount_id, pickup_location, dropoff_location, pickup_time, dropoff_time,
    # billing_date, total_cost)
    cursor = connection.cursor()
    cursor.callproc('ReserveCar', [customer_id, car_id, insurance_id, discount_id, pickup_location,
                                       dropoff_location, pickup_time, dropoff_time])
    connection.commit()
    cursor.close()
    # execute_query(connection, query, values, "Car reservation added successfully")


def create_new_discount(connection, discount_name, validity, percentage):
    """Create a new discount in the Discount table."""
    query = "INSERT INTO Discount (DiscountName, DiscountValidity, DiscountPercentage) VALUES (%s, %s, %s)"
    values = (discount_name, validity, percentage)
    execute_query(connection, query, values, "Discount added successfully")


# def create_new_insurance(connection, company, insurance_type, cost):
#     """Create a new insurance in the Insurance table."""
#     query = "INSERT INTO Insurance (InsuranceCompany, InsuranceType, InsuranceCost) VALUES (%s, %s, %s)"
#     values = (company, insurance_type, cost)
#     execute_query(connection, query, values, "Insurance added successfully")


def create_new_penalty(connection, reason, cost):
    """Create a new penalty in the Penalty table."""
    query = "INSERT INTO Penalty (PenaltyReason, PenaltyCost) VALUES (%s, %s)"
    values = (reason, cost)
    execute_query(connection, query, values, "Penalty added successfully")


def create_new_payment(connection, payment_type, amount, reservation_id):
    """Create a new payment in the Payment table."""
    query = """
    INSERT INTO Payment (PaymentType, TransactionID, PaymentAmount, PaymentStatus, TransactionTime, ReservationID) 
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    print(payment_type)
    print(amount)
    print(reservation_id)
    values = (payment_type,random.randint(10000,99999) , amount,'Processed',datetime.now().strftime("%Y-%m-%d %H:%M:%S") , reservation_id)
    execute_query(connection, query, values, "Payment added successfully")


# def create_new_garage(connection, garage_name, location_id):
#     """Create a new garage in the Garage table."""
#     query = "INSERT INTO Garage (GarageName, GarageLocationID) VALUES (%s, %s)"
#     values = (garage_name, location_id)
#     execute_query(connection, query, values, "Garage added successfully")


# def create_new_car_category(connection, category_type, seating_capacity, fixed_cost):
#     """Create a new car category in the Car_Category table."""
#     query = "INSERT INTO Car_Category (CarCategoryType, SeatingCapacity, CarFixedCost) VALUES (%s, %s, %s)"
#     values = (category_type, seating_capacity, fixed_cost)
#     execute_query(connection, query, values, "Car category added successfully")


# def call_stored_procedure(connection, procedure_name, parameters):
#     """Generic function to call a stored procedure."""
#     cursor = connection.cursor()
#     try:
#         cursor.callproc(procedure_name, parameters)
#         results = []
#         for result in cursor.stored_results():
#             results.append(result.fetchall())
#         return results
#     except mysql.connector.Error as e:
#         print(f"Error: {e}")
#     finally:
#         cursor.close()


# def add_insurance(connection, insurance_company, insurance_type, insurance_cost):
#     """Call the AddInsurance stored procedure."""
#     return call_stored_procedure(connection, 'AddInsurance', [insurance_company, insurance_type, insurance_cost])


# def create_discount(connection, discount_name, discount_validity, discount_percentage):
#     """Call the CreateDiscount stored procedure."""
#     return call_stored_procedure(connection, 'CreateDiscount', [discount_name, discount_validity, discount_percentage])


# def insert_penalty(connection, penalty_reason, penalty_cost):
#     """Call the InsertPenalty stored procedure."""
#     return call_stored_procedure(connection, 'InsertPenalty', [penalty_reason, penalty_cost])


# def reserve_car(connection, customer_id, car_id, insurance_id, discount_id, pick_up_location, drop_off_location,
#                 pick_up_time, drop_off_time):
#     """Call the ReserveCar stored procedure."""
#     return call_stored_procedure(connection, 'ReserveCar',
#                                  [customer_id, car_id, insurance_id, discount_id, pick_up_location, drop_off_location,
#                                   pick_up_time, drop_off_time])


# def insert_billing_penalty(connection, reservation_id, penalty_id):
#     """Call the InsertBillingPenalty stored procedure."""
#     return call_stored_procedure(connection, 'InsertBillingPenalty', [reservation_id, penalty_id])


# def pay_bill(connection, reservation_id, payment_type, transaction_id, payment_amount, payment_status,
#              transaction_time):
#     """Call the PayBill stored procedure."""
#     return call_stored_procedure(connection, 'PayBill',
#                                  [reservation_id, payment_type, transaction_id, payment_amount, payment_status,
#                                   transaction_time])


# def maintain_update_car(connection, car_id, service_type, date_change):
#     """Call the maintainupdatecar stored procedure."""
#     return call_stored_procedure(connection, 'maintainupdatecar', [car_id, service_type, date_change])


# def create_billing_penalty(connection, reservation_id, penalty_id):
#     """Create a new billing penalty record."""
#     query = "INSERT INTO Billing_Penalty (ReservationID, PenaltyID) VALUES (%s, %s)"
#     values = (reservation_id, penalty_id)
#     execute_query(connection, query, values, "Billing penalty added successfully")


# def create_reservation_with_custom_logic(connection, customer_id, car_id, insurance_id, discount_id, pickup_location,
#                                          dropoff_location, pickup_time, dropoff_time):
#     """Create a new car reservation with additional business logic."""
#     # This function should include any additional logic that is specific to your business requirements.
#     # For example, checking car availability, applying discounts, etc.
#     pass


# def create_initial_data(connection):
#     """Function to create initial data as per Car_Rental_System_Insertion.sql"""

#     # Insert Location Data
#     location_data = [
#         ('2323 Main St', 'Dallas', 'TX', 'USA', 75201),
#         ('4545 Oak Ave', 'San Diego', 'CA', 'USA', 92101),
#         ('6767 Pine Rd', 'Philadelphia', 'PA', 'USA', 19102),
#         ('8989 Maple Blvd', 'Phoenix', 'AZ', 'USA', 85004),
#         ('111 Pine St', 'Portland', 'OR', 'USA', 97204),
#         ('222 Elm St', 'Denver', 'CO', 'USA', 80202),
#         ('333 Oak St', 'New Orleans', 'LA', 'USA', 70112),
#         ('444 Pine Ave', 'Nashville', 'TN', 'USA', 37203),
#         ('555 Maple St', 'Kansas City', 'MO', 'USA', 64106),
#         ('666 Oak Rd', 'Las Vegas', 'NV', 'USA', 89109),
#         ('777 Pine Blvd', 'Minneapolis', 'MN', 'USA', 55401),
#         ('888 Maple St', 'Detroit', 'MI', 'USA', 48226),
#         ('999 Oak St', 'Salt Lake City', 'UT', 'USA', 84101),
#         ('1212 Pine Ave', 'San Antonio', 'TX', 'USA', 78205),
#         ('1414 Maple St', 'Charlotte', 'NC', 'USA', 28202),
#         ('1616 Oak Rd', 'Indianapolis', 'IN', 'USA', 46204),
#         ('1818 Pine Blvd', 'Cincinnati', 'OH', 'USA', 45202),
#         ('2020 Maple St', 'Raleigh', 'NC', 'USA', 27601),
#         ('2222 Oak St', 'Tampa', 'FL', 'USA', 33602)
#     ]
#     for location in location_data:
#         create_new_location(connection, *location)

#     # Insert Person Data
#     person_data = [
#         ('Ethan', 'Jones', 'Male', 'ethan.jones@drivenow.com', 1324567890, 1, '1995-04-03'),
#         ('Sophia', 'Smith', 'Female', 'sophia.smith@gmail.com', 2345678901, 2, '1994-06-15'),
#         ('Jackson', 'Taylor', 'Male', 'jackson.taylor@hotmail.com', 3456789012, 3, '1993-07-11'),
#         ('Mia', 'Brown', 'Female', 'mia.brown@outlook.com', 4567890123, 4, '1997-09-02'),
#         ('Aiden', 'Garcia', 'Male', 'aiden.garcia@gmail.com', 5678901234, 5, '1998-11-23'),
#         ('Chloe', 'Lee', 'Female', 'chloe.lee@yahoo.com', 6789012345, 6, '2000-02-14'),
#         ('Caleb', 'Wilson', 'Male', 'caleb.wilson@outlook.com', 7890123456, 7, '2001-03-10'),
#         ('Avery', 'Miller', 'Female', 'avery.miller@gmail.com', 8901234567, 8, '2002-05-18'),
#         ('Evelyn', 'Davis', 'Female', 'evelyn.davis@outlook.com', 9012345678, 9, '2003-06-22'),
#         ('William', 'Clark', 'Male', 'william.clark@yahoo.com', 1011121314, 10, '2004-08-12'),
#         ('Oliver', 'Johnson', 'Male', 'oliver.johnson@drivenow.com', 1213141516, 11, '2005-10-27'),
#         ('Isabella', 'Anderson', 'Female', 'isabella.anderson@gmail.com', 1314151617, 12, '2006-12-31'),
#         ('Noah', 'Martin', 'Male', 'noah.martin@outlook.com', 1415161718, 13, '1998-07-11'),
#         ('Emma', 'Taylor', 'Female', 'emma.taylor@yahoo.com', 1516171819, 14, '1999-09-02'),
#         ('Liam', 'White', 'Male', 'liam.white@drivenow.com', 1617181920, 15, '2000-11-09'),
#         ('Aria', 'Jackson', 'Female', 'aria.jackson@gmail.com', 1718192021, 16, '2002-02-14'),
#         ('Ethan', 'Lee', 'Male', 'ethan.lee@outlook.com', 1819202122, 17, '2003-04-05'),
#         ('Zoe', 'Scott', 'Female', 'zoe.scott@yahoo.com', 1920212223, 18, '2004-06-15'),
#         ('Harsh', 'Vora', 'Male', 'harsh@gmail.com', 6171231234, 9, '1997-08-25'),
#         ('Malav', 'Patel', 'Male', 'malav.patel@gmail.com', 6171231235, 9, '1999-02-28'),
#         ('Haoran', 'Xu', 'Male', 'xu@drivenow.com', 6171231236, 9, '1999-03-25'),
#         ('Shreyansh', 'Patel', 'Male', 'shreyansh.patel@gmail.com', 6171231237, 9, '1998-05-02'),
#         ('Vidhan', 'Pal', 'Male', 'vidhan.pal@yahoo.com', 6171231238, 9, '2000-08-20'),
#         ('John', 'Doe', 'Male', 'john.doe@drivenow.com', 6171231239, 15, '1990-08-25'),
#         ('Jacob', 'Garcia', 'Male', 'jacob.garcia@drivenow.com', 2021222324, 19, '2005-08-25'),
#         ('Emma', 'Smith', 'Female', 'emma.smith@drivenow.com', 9876543210, 2, '1990-08-15'),
#         ('Liam', 'Johnson', 'Male', 'liam.johnson@drivenow.com', 6543219870, 3, '1988-11-22'),
#         ('Olivia', 'Brown', 'Female', 'olivia.brown@drivenow.com', 1234567890, 4, '1992-05-10'),
#         ('Noah', 'Davis', 'Male', 'noah.davis@drivenow.com', 9871236540, 5, '1993-09-18'),
#         ('Ava', 'Martinez', 'Female', 'ava.martinez@drivenow.com', 4567990123, 6, '1997-02-28'),
#         ('William', 'Taylor', 'Male', 'william.taylor@drivenow.com', 7892123456, 7, '1991-07-14'),
#         ('Will', 'Tay', 'Male', 'wil.tay@servicenow.com', 8892123456, 7, '1991-08-14')
#     ]
#     for person in person_data:
#         create_new_person(connection, *person)

#     # Insert Employee Data
#     employee_data = [
#         (21, 'Employee'),
#         (22, 'Manager'),
#         (23, 'Manager'),
#         (24, 'Employee'),
#         (25, 'CTO'),
#         (26, 'CEO'),
#         (27, 'Marketing Lead'),
#         (28, 'Priciple Engineer'),
#         (29, 'HR'),
#         (30, 'Employee')
#     ]
#     for employee in employee_data:
#         create_new_employee(connection, *employee)

#     # Insert Customer Data
#     customer_data = [
#         (1, 'XYZ123'),
#         (2, 'ABC456'),
#         (3, 'DEF789'),
#         (4, 'GHI012'),
#         (5, 'GHJ012'),
#         (6, 'JKL345'),
#         (7, 'MNO678'),
#         (8, 'PQR901'),
#         (9, 'STU234'),
#         (10, 'VWX567'),
#         (11, 'VXX567'),
#         (12, 'YZA890'),
#         (13, 'DEF012'),
#         (14, 'GHI345'),
#         (15, 'GII345'),
#         (16, 'JKL678'),
#         (17, 'MNO901'),
#         (18, 'PQR234'),
#         (19, 'AQR244'),
#         (20, 'PQS264')
#     ]
#     for customer in customer_data:
#         create_new_customer(connection, *customer)

#     # Insert Car Data
#     car_data = [
#         ('Toyota', 'Sedan', 1, 1, 'Regular', '2023-06-01', 'ABC123', 'Camry', 2022, 1),
#         ('Honda', 'SUV', 2, 1, 'Premium', '2023-05-15', 'XYZ456', 'CR-V', 2023, 1),
#         ('Ford', 'Truck', 3, 2, 'Heavy Duty', '2023-07-10', 'DEF789', 'F-150', 2021, 1),
#         ('Chevrolet', 'Coupe', 1, 1, 'Sports', '2023-08-20', 'GHI012', 'Camaro', 2023, 1),
#         ('Nissan', 'Hatchback', 2, 2, 'Economy', '2023-04-30', 'JKL345', 'Versa', 2022, 0),
#         ('BMW', 'Convertible', 3, 2, 'Luxury', '2023-09-05', 'MNO678', 'Z4', 2022, 1),
#         ('Mercedes-Benz', 'Sedan', 1, 1, 'Executive', '2023-10-12', 'PQR901', 'E-Class', 2023, 1),
#         ('Audi', 'SUV', 2, 2, 'Premium', '2023-11-25', 'STU234', 'Q5', 2021, 1),
#         ('Hyundai', 'Crossover', 3, 2, 'Regular', '2023-12-15', 'VWX567', 'Tucson', 2022, 1),
#         ('Kia', 'Sedan', 1, 2, 'Economy', '2023-04-15', 'YZA890', 'Forte', 2021, 1),
#         ('Tesla', 'Electric', 2, 1, 'Luxury', '2023-05-28', 'BCD123', 'Model S', 2022, 1),
#         ('Subaru', 'SUV', 3, 1, 'Regular', '2023-08-02', 'EFG456', 'Outback', 2023, 0),
#         ('Mazda', 'Convertible', 1, 2, 'Sports', '2023-09-18', 'HIJ789', 'MX-5', 2022, 1),
#         ('Volkswagen', 'Hatchback', 2, 2, 'Economy', '2023-10-30', 'KLM012', 'Golf', 2021, 1),
#         ('Volvo', 'Sedan', 3, 1, 'Executive', '2023-11-08', 'NOP345', 'S60', 2023, 1),
#         ('Jaguar', 'Coupe', 1, 1, 'Luxury', '2023-12-22', 'QRS678', 'F-Type', 2022, 1),
#         ('Lexus', 'SUV', 2, 2, 'Executive', '2024-01-05', 'TUV901', 'RX', 2023, 1),
#         ('Chrysler', 'Van', 3, 1, 'Regular', '2024-02-18', 'WXY234', 'Pacifica', 2022, 1),
#         ('Buick', 'Sedan', 1, 2, 'Premium', '2024-03-03', 'ZAB567', 'Regal', 2021, 1),
#         ('Acura', 'SUV', 2, 1, 'Executive', '2024-04-15', 'CDE890', 'MDX', 2023, 1)
#     ]
#     for car in car_data:
#         create_new_car(connection, *car)

#     # Insert Car Reservation Data
#     car_reservation_data = [
#         (1, 1, 1, 1, 1, 2, '2023-03-04 12:00:00', '2023-03-05 12:00:00', None, '2023-03-05', 0),
#         (2, 2, 2, 2, 2, 3, '2023-03-03 4:30:00', '2023-04-04 10:30:00', None, '2023-04-04', 0),
#         (3, 3, 3, 3, 3, 4, '2023-03-07 23:00:00', '2023-03-09 1:00:00', None, '2023-05-02', 0),
#         (4, 4, 4, 4, 4, 5, '2023-07-29 20:00:00', '2023-08-01 1:30:00', None, '2023-08-01', 0),
#         (6, 6, 6, 6, 6, 7, '2023-07-29 20:00:00', '2023-08-01 1:30:00', None, '2023-08-01', 0),
#         (7, 7, 7, 7, 7, 8, '2023-05-14 2:00:00', '2023-05-15 3:30:00', None, '2023-05-15', 0),
#         (8, 8, 8, 8, 8, 9, '2023-05-14 2:00:00', '2023-05-15 1:30:00', None, '2023-05-15', 0),
#         (9, 9, 9, 9, 9, 10, '2023-08-14 6:00:00', '2023-08-16 1:30:00', None, '2023-08-16', 0),
#         (10, 10, 10, 10, 10, 11, '2023-07-29 10:00:00', '2023-08-20 23:00:00', None, '2023-08-20', 0),
#         (11, 11, 11, 11, 11, 12, '2023-08-07 11:15:00', '2023-08-8 23:15:00', None, '2023-08-8', 0),
#         (13, 13, 13, 13, 13, 14, '2023-04-06 01:05:00', '2023-04-7 23:59:00', None, '2023-04-7', 0),
#         (14, 14, 14, 14, 14, 15, '2021-11-01 15:00:00', '2021-11-02 15:00:00', None, '2021-11-02', 0),
#         (15, 15, 15, 15, 15, 16, '2020-06-10 09:00:00', '2020-06-12 15:00:00', None, '2020-06-12', 0),
#         (16, 16, 1, 1, 16, 17, '2020-10-10 08:00:00', '2020-10-12 12:00:00', None, '2020-10-12', 0),
#         (17, 17, 2, 12, 18, 19, '2020-09-01 12:00:00', '2020-09-02 12:00:00', None, '2020-09-02', 0)

#         # ... Add all other reservation entries here
#     ]
#     for reservation in car_reservation_data:
#         create_new_car_reservation(connection, *reservation)

#     # Insert Discount Data
#     discount_data = [
#         ('Summer Sale', '2023-06-30 18:00:00', 15.00),
#         ('Back to School', '2023-08-31 23:59:59', 10.00),
#         ('Early Bird Special', '2023-09-15 09:00:00', 20.00),
#         ('Fall Clearance', '2023-11-15 20:30:00', 25.00),
#         ('Winter Wonderland', '2023-12-15 22:00:00', 10.00),
#         ('New Year, New You', '2024-01-31 21:00:00', 15.00),
#         ('Spring Fling', '2024-04-15 15:30:00', 10.00),
#         ('Memorial Day Weekend', '2024-05-27 23:00:00', 20.00),
#         ('Independence Day', '2024-07-04 18:45:00', 15.00),
#         ('Labor Day Sale', '2024-09-02 16:00:00', 10.00),
#         ('Oktoberfest', '2024-10-05 22:30:00', 25.00),
#         ('Black Friday', '2024-11-29 23:59:59', 30.00),
#         ('Cyber Monday', '2024-12-02 23:59:59', 35.00),
#         ('Valentine''s Day', '2025-02-14 20:15:00', 15.00),
#         ('St. Patrick''s Day', '2025-03-17 12:00:00', 10.00)
#         # ... Add all other discount entries here
#     ]
#     for discount in discount_data:
#         create_new_discount(connection, *discount)

#     # Insert Insurance Data
#     insurance_data = [
#         ('Allianz', 'Comprehensive', 100.00),
#         ('AIG', 'Collision', 150.50),
#         ('GEICO', 'Liability Only', 75.75),
#         ('State Farm', 'Comprehensive', 125.00),
#         ('Progressive', 'Personal Injury', 90.25),
#         ('Allstate', 'Comprehensive', 120.00),
#         ('Nationwide', 'Comprehensive', 180.50),
#         ('Farmers', 'Comprehensive', 135.25),
#         ('Liberty Mutual', 'Collision', 110.00),
#         ('Esurance', 'Personal Injury', 100.00),
#         ('Travelers', 'Comprehensive', 140.00),
#         ('USAA', 'Liability Only', 65.50),
#         ('Hartford', 'Comprehensive', 155.00),
#         ('MetLife', 'Personal Injury', 95.75),
#         ('Mercury', 'Comprehensive', 110.50)
#     ]
#     for insurance in insurance_data:
#         create_new_insurance(connection, *insurance)

#     # Insert Penalty Data
#     penalty_data = [
#         ('Late payment', 100),
#         ('Damaged property', 500),
#         ('Noise violation', 200),
#         ('Smoking in non-smoking area', 300),
#         ('Parking violation', 150),
#         ('Excessive trash', 75),
#         ('Unauthorized pet', 250),
#         ('Late dropoff penalty per hour', 50),
#         ('Damaged interior', 25),
#         ('Broken windshield', 100),
#         ('Scratched paint', 75),
#         ('Missing license plate', 50),
#         ('Flat tire', 80),
#         ('Damaged headlight', 90),
#         ('Broken side mirror', 60),
#         ('Dented door', 110),
#         ('Broken taillight', 85),
#         ('Damaged bumper', 120),
#         ('Broken rearview mirror', 70),
#         ('Cracked windshield', 95),
#         ('Missing side mirror', 55),
#         ('Broken headlight', 100),
#         ('Dented hood', 125),
#         ('Scratched windshield', 80),
#         ('Graffiti', 400)
#     ]
#     for penalty in penalty_data:
#         create_new_penalty(connection, *penalty)

#     # Insert Payment Data
#     payment_data = [
#         ('Credit Card', '12345', 259.325, 'Processed', '2023-04-05 14:30:00', 10),
#         ('PayPal', '23456', 250, 'Processed', '2023-04-05 14:35:00', 4),
#         ('Debit Card', '34567', 128, 'Pending', '2023-04-04 15:00:00', 13),
#         ('Credit Card', '12341', 128, 'Processed', '2023-04-04 15:05:00', 6),
#         ('Google Pay', '45678', 168, 'Processed', '2023-04-05 15:05:00', 7),
#         ('Venmo', 56789, 840.6, 'Pending', '2023-08-20 23:00:02', 8),
#         ('Credit Card', 67890, 753.00, 'Processed', '2023-12-31 20:00:30', 9),
#         ('PayPal', 78901, 315.9, 'Processed', '2023-05-14 2:10:00', 10),
#         ('Debit Card', 89012, 350, 'Pending', '2023-08-23 1:34:34', 11),
#         ('Venmo', 12340, 1182.9875, 'Failed', '2023-04-11 20:36:47', 8),
#         ('PayPal', 12342, 225, 'Processed', '2023-03-2 22:10:27', 13),
#         ('Venmo', 12343, 525, 'Pending', '2023-02-9 12:11:2', 14),
#         ('Google Pay', 12344, 365, 'Processed', '2023-01-8 21:14:27', 15),
#         ('PayPal', 12345, 322, 'Processed', '2023-09-5 11:39:30', 6),
#         ('Venmo', 12346, 327, 'Processed', '2023-08-2 3:55:40', 7),
#         ('Credit Card', 12347, 820, 'Failed', '2023-07-14 20:39:45', 1),
#         ('Debit Card', 12348, 345, 'Processed', '2023-10-11 4:10:20', 2)
#     ]
#     for payment in payment_data:
#         create_new_payment(connection, *payment)

#     # Insert Garage Data
#     garage_data = [
#         ('ABC Auto Care', 1),
#         ('XYZ Car Services', 2)
#     ]
#     for garage in garage_data:
#         create_new_garage(connection, *garage)

#     # Insert Car Category Data
#     car_category_data = [
#         ('Sedan', 5, 50.0),
#         ('SUV', 7, 70.0),
#         ('Truck', 3, 80.0),
#         ('Coupe', 2, 60.0),
#         ('Hatchback', 4, 45.0),
#         ('Convertible', 2, 75.0),
#         ('Crossover', 5, 55.0),
#         ('Compact', 4, 48.0),
#         ('Electric', 5, 90.0),
#         ('Luxury Sedan', 4, 120.0),
#         ('Luxury SUV', 6, 150.0),
#         ('Sports Car', 2, 100.0),
#         ('Executive', 5, 130.0),
#         ('Compact SUV', 5, 65.0),
#         ('Van', 8, 80.0),
#         ('Hybrid', 5, 85.0),
#         ('Midsize', 5, 60.0),
#         ('Full-size', 6, 70.0),
#         ('Wagon', 5, 55.0),
#         ('Minivan', 7, 75.0)
#     ]
#     for car_category in car_category_data:
#         create_new_car_category(connection, *car_category)

#     # Insert Billing Penalty Data
#     billing_penalty_data = [
#         (15, 7),
#         (15, 13),
#         (15, 12),
#         (15, 5),
#         (15, 9),
#         (15, 22),
#         (2, 24),
#         (12, 8),
#         (3, 8),
#         (4, 8)
#     ]
#     for billing_penalty in billing_penalty_data:
#         create_billing_penalty(connection, *billing_penalty)

#     print("Initial data creation completed successfully.")
