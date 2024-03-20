import mysql.connector
from db_connection import create_db_connection, close_db_connection


def execute_read_query(connection, query, values=None):
    """Generic function to execute a given SQL read query."""
    cursor = connection.cursor()
    try:
        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def fetch_all_locations(connection):
    """Fetch all records from the Location table."""
    query = "SELECT * FROM Location"
    return execute_read_query(connection, query)



def fetch_all_employees(connection):
    """Fetch all records from the Employee table."""
    query = "SELECT * FROM Employee"
    return execute_read_query(connection, query)




def fetch_all_cars(connection):
    """Fetch all records from the Cars table."""
    query = "SELECT * FROM Cars"
    return execute_read_query(connection, query)




def fetch_all_discounts(connection):
    """Fetch all records from the Discount table."""
    query = "SELECT * FROM Discount"
    return execute_read_query(connection, query)


def fetch_all_insurances(connection):
    """Fetch all records from the Insurance table."""
    query = "SELECT * FROM Insurance"
    return execute_read_query(connection, query)


def fetch_all_penalties(connection):
    """Fetch all records from the Penalty table."""
    query = "SELECT * FROM Penalty"
    return execute_read_query(connection, query)


def fetch_all_payments(connection):
    """Fetch all records from the Payment table."""
    query = "SELECT * FROM Payment"
    return execute_read_query(connection, query)




def fetch_car_category_details(connection):
    """Fetch all records from the Car_Category table."""
    query = "SELECT * FROM Car_Category"
    return execute_read_query(connection, query)




def fetch_reservation_by_id(connection, id):
    """Fetch all records from the Reservation table."""
    query = "SELECT cr.ReservationID, c.CarModel, i.InsuranceCompany, d.DiscountName,\
       CONCAT(pick_up_location.Address, ', ', pick_up_location.City, ', ', pick_up_location.State) AS PickUpLocation,\
       cr.PickUpTime,\
       CONCAT(drop_off_location.Address, ', ', drop_off_location.City, ', ', drop_off_location.State) AS DropOffLocation,\
       cr.DropOffTime, cr.TotalCost\
       FROM Car_Reservation cr JOIN Cars c ON cr.CarID = c.CarID JOIN Insurance i ON cr.InsuranceID = i.InsuranceID \
       JOIN Discount d ON cr.DiscountID = d.DiscountID\
       JOIN Location pick_up_location ON cr.PickUpLocation = pick_up_location.LocationID\
       JOIN Location drop_off_location ON cr.DropoffLocation = drop_off_location.LocationID\
       WHERE cr.CustomerID = %s;"
    # query = "SELECT * from Car_Reservation where CustomerID = %s"
    return execute_read_query(connection, query, (id,))
 
def fetch_car_names(connection):
    query = "SELECT CarId, CarModel FROM Cars"
    return execute_read_query(connection, query)
 
def fetch_insurance_names(connection):
    query = "SELECT InsuranceId, InsuranceCompany FROM Insurance"
    return execute_read_query(connection, query)
 
def fetch_discount_names(connection):
    query = "SELECT DiscountId, DiscountName FROM Discount"
    return execute_read_query(connection, query)
 
def fetch_location_names(connection):
    query = "SELECT LocationId, Address FROM Location"
    return execute_read_query(connection, query)


def fetch_payment_by_id(connection, id):
    query = "SELECT PaymentType, TransactionID, PaymentAmount, PaymentStatus, TransactionTime, Payment.ReservationID FROM Payment Join Car_Reservation ON Payment.ReservationID = Car_Reservation.ReservationID WHERE Car_Reservation.CustomerID = %s"
    return execute_read_query(connection, query, (id, ))

def fetch_customer_info(connection, id):
    query = "Select p.Email, p.PhoneNumber from Customers c join Person p on c.PersonID = p.PersonID where c.CustomerID = %s"
    return execute_read_query(connection, query, (id, ))
 
def fetch_person_id(connection, id):
    query = "Select PersonID from Customers c where c.CustomerID = %s"
    return execute_read_query(connection, query, (id, ))

def fetch_all_reservations(connection):
    """Fetch all records from the Reservation table."""
    query = "SELECT * FROM car_reservation"
    return execute_read_query(connection, query)