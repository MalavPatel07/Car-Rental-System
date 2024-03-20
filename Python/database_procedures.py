import mysql.connector
from db_connection import create_db_connection, close_db_connection


# 1. Reservation Related Procedures
def cancel_reservation(connection, reservation_id):
    """Call stored procedure to cancel a reservation."""
    cursor = connection.cursor()
    try:
        cursor.callproc('CancelReservation', [reservation_id])
        connection.commit()
        print("Reservation cancelled successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def check_age_requirement(connection, person_id):
    """Call SQL function to check age requirement."""
    query = "SELECT CheckAgeRequirement(%s)"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (person_id,))
        result = cursor.fetchone()
        return result[0]  # Returns True or False
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def check_dropoff_time(connection, pickup_time, dropoff_time):
    """Call SQL function to check the validity of drop-off time."""
    query = "SELECT fn_CheckDropOffTime(%s, %s)"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (pickup_time, dropoff_time))
        result = cursor.fetchone()
        return result[0]  # Returns 1 if invalid, 0 if valid
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()

def get_all_customers(connection):
    """Call stored procedure to fetch all customers."""
    cursor = connection.cursor()
    try:
        cursor.callproc('GetCustomerInfo')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def get_all_reservations(connection):
    """Call stored procedure to fetch all reservations."""
    cursor = connection.cursor()
    try:
        cursor.callproc('GetAllReservations')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def get_reservation_details(connection, reservation_id):
    """Call stored procedure to get details of a specific reservation."""
    cursor = connection.cursor()
    try:
        cursor.callproc('GetReservationDetails', [reservation_id])
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def toggle_cars_availability(connection, check_date):
    cursor = connection.cursor()
    try:
        cursor.callproc('ToggleCarsAvailability', [check_date])
        connection.commit()
        print("Car availability updated.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def get_all_available_cars(connection):
    cursor = connection.cursor()
    try:
        cursor.callproc('GetAllAvailableCars')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def reserve_car(connection, customer_id, car_id, insurance_id, discount_id, pick_up_location, drop_off_location,
                pick_up_time, drop_off_time):
    """Call stored procedure to reserve a car."""
    cursor = connection.cursor()
    try:
        cursor.callproc('ReserveCar',
                        [customer_id, car_id, insurance_id, discount_id, pick_up_location, drop_off_location,
                         pick_up_time, drop_off_time])
        connection.commit()
        print("Car reserved successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def update_reservation(connection, reservation_id, new_pick_up_location, new_drop_off_location, new_pick_up_time,
                       new_drop_off_time):
    """Call stored procedure to update a reservation."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateReservation',
                        [reservation_id, new_pick_up_location, new_drop_off_location, new_pick_up_time,
                         new_drop_off_time])
        connection.commit()
        print("Reservation updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def delete_reservation(connection, reservation_id):
    """Call stored procedure to delete a reservation."""
    cursor = connection.cursor()
    try:
        cursor.callproc('CancelReservation', [reservation_id])
        connection.commit()
        print("Reservation deleted successfully.")
    finally:
        cursor.close()


# 2. Penalty Related Procedures
def insert_penalty(connection, penalty_reason, penalty_cost):
    """Call stored procedure to insert a new penalty."""
    cursor = connection.cursor()
    try:
        cursor.callproc('InsertPenalty', [penalty_reason, penalty_cost])
        connection.commit()
        print("Penalty inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def calculate_penalty_amount(connection, reservation_id):
    """Call SQL function to calculate penalty amount for a reservation."""
    query = "SELECT CalculatePenaltyAmount(%s)"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (reservation_id,))
        result = cursor.fetchone()
        return result[0]  # Returns the total penalty amount
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def get_penalty(connection, penalty_id):
    """Call stored procedure to get a specific penalty."""
    cursor = connection.cursor()
    try:
        cursor.callproc('GetPenalty', [penalty_id])
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


# 3. Insurance Related Procedures
def add_insurance(connection, insurance_company, insurance_type, insurance_cost):
    """Call stored procedure to add a new insurance record."""
    cursor = connection.cursor()
    try:
        cursor.callproc('AddInsurance', [insurance_company, insurance_type, insurance_cost])
        connection.commit()
        print("Insurance record added successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def get_insurance_by_id(connection, insurance_id):
    cursor = connection.cursor()
    try:
        cursor.callproc('GetInsuranceByID', [insurance_id])
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def get_all_insurances(connection):
    """Call stored procedure to fetch all insurances."""
    cursor = connection.cursor()
    try:
        cursor.callproc('GetAllInsurances')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def update_insurance(connection, insurance_id, new_company, new_type, new_cost):
    """Call stored procedure to update insurance details."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateInsurance', [insurance_id, new_company, new_type, new_cost])
        connection.commit()
        print("Insurance updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def delete_insurance(connection, insurance_id):
    """Call stored procedure to delete an insurance record."""
    cursor = connection.cursor()
    try:
        cursor.callproc('DeleteInsurance', [insurance_id])
        connection.commit()
        print("Insurance deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# 4. Discount Related Procedures
def create_discount(connection, discount_name, discount_validity, discount_percentage):
    """Call stored procedure to create a new discount."""
    cursor = connection.cursor()
    try:
        cursor.callproc('CreateDiscount', [discount_name, discount_validity, discount_percentage])
        connection.commit()
        print("Discount created successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def read_all_discounts(connection):
    """Call stored procedure to fetch all discounts."""
    cursor = connection.cursor()
    try:
        cursor.callproc('ReadAllDiscounts')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def read_discount_by_id(connection, discount_id):
    cursor = connection.cursor()
    try:
        cursor.callproc('ReadDiscountByID', [discount_id])
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def update_discount(connection, discount_id, new_name, new_validity, new_percentage):
    """Call stored procedure to update a discount."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateDiscount', [discount_id, new_name, new_validity, new_percentage])
        connection.commit()
        print("Discount updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def delete_discount(connection, discount_id):
    """Call stored procedure to delete a discount."""
    cursor = connection.cursor()
    try:
        cursor.callproc('DeleteDiscount', [discount_id])
        connection.commit()
        print("Discount deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# 5. Car Maintenance Procedure
def maintain_update_car(connection, car_id, service_type, date_change):
    """Call stored procedure for car maintenance update."""
    cursor = connection.cursor()
    try:
        cursor.callproc('maintainupdatecar', [car_id, service_type, date_change])
        connection.commit()
        print("Car maintenance information updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

# Function to call the stored procedure for updating car details
def update_car(connection, car_id, brand, car_type, category_id, garage_id, service_type,
                         service_due_date, license_plate, model, model_year, availability):
    try:
        with connection.cursor() as cursor:
            # Call the stored procedure with the provided parameters
            cursor.callproc("UpdateCarDetails", (car_id, brand, car_type, category_id, garage_id, service_type,
                                                  service_due_date, license_plate, model, model_year, availability))
        connection.commit()
        print("Car details updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# 6. Bill Related Procedures
def insert_billing_penalty(connection, reservation_id, penalty_id):
    """Call stored procedure to insert billing penalty."""
    cursor = connection.cursor()
    try:
        cursor.callproc('InsertBillingPenalty', [reservation_id, penalty_id])
        connection.commit()
        print("Billing penalty inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def pay_bill(connection, reservation_id, payment_type, transaction_id, payment_amount, payment_status,
             transaction_time):
    """Call stored procedure to process payment for a bill."""
    cursor = connection.cursor()
    try:
        cursor.callproc('PayBill', [reservation_id, payment_type, transaction_id, payment_amount, payment_status,
                                    transaction_time])
        connection.commit()
        print("Payment processed successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def update_actual_dropoff_time(connection, reservation_id, actual_dropoff_time):
    """Call stored procedure to update the actual dropoff time."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateActualDropoffTime', [reservation_id, actual_dropoff_time])
        connection.commit()
        print("Actual dropoff time updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def update_total_cost(connection, reservation_id, new_total_cost):
    """Call stored procedure to update the total cost of a reservation."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateTotalCost', [reservation_id, new_total_cost])
        connection.commit()
        print("Total cost updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def calculate_costs(connection, reservation_id):
    """Call SQL function to calculate total costs for a reservation."""
    query = "SELECT CalculateCosts(%s)"
    cursor = connection.cursor()
    try:
        cursor.execute(query, (reservation_id,))
        result = cursor.fetchone()
        return result[0]  # Returns the total cost
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def update_penalty(connection, penalty_id, new_reason, new_cost):
    """Call stored procedure to update penalty details."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdatePenalty', [penalty_id, new_reason, new_cost])
        connection.commit()
        print("Penalty updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def delete_penalty(connection, penalty_id):
    """Call stored procedure to delete a penalty record."""
    cursor = connection.cursor()
    try:
        cursor.callproc('DeletePenalty', [penalty_id])
        connection.commit()
        print("Penalty deleted successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


# 7. Analytics and Reporting Procedures
def location_based_analytics(connection):
    """Call stored procedure to generate analytics based on location."""
    cursor = connection.cursor()
    try:
        cursor.callproc('LocationBasedAnalytics')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


def popular_car_categories(connection):
    """Call stored procedure to identify most popular car categories."""
    cursor = connection.cursor()
    try:
        cursor.callproc('PopularCarCategories')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()


# 8. Update customer information
def update_customer_information(connection, person_id, new_phone_number, new_email):
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateCustomerInformation', [person_id,  new_phone_number,new_email])
        connection.commit()
        print("Customer information updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def delete_car(connection, car_id):
    """Call stored procedure to delete a car."""
    cursor = connection.cursor()
    # try:
    cursor.callproc('DeleteCar', [car_id])
    connection.commit()
    print("Car deleted successfully.")
    # except mysql.connector.Error as e:
    #     print(f"Error: {e}")
    # finally:
    cursor.close()


def updateActualDropoffTime(connection, reservation_id, actual_dropoff_time):
    """Call stored procedure to update the actual dropoff time."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateActualDropoffTime', [reservation_id, actual_dropoff_time])
        connection.commit()
        print("Actual dropoff time updated successfully.")
        updateTotalBill(connection, reservation_id)
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def updateTotalBill(connection, reservation_id):
    """Call stored procedure to update the total cost of a reservation."""
    cursor = connection.cursor()
    try:
        cursor.execute('select CalculateCosts(%s);', (reservation_id,))
        result = cursor.fetchone()
        print(result[0])
        connection.commit()
        print("Total cost updated successfully.")
        updateBillInReservation(connection, reservation_id, result[0])
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def updateBillInReservation(connection, reservation_id, total_cost):
    """Call stored procedure to update the total cost of a reservation."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateTotalCost', [reservation_id, total_cost])
        connection.commit()
        print("Total cost updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def insertBillingPenalty(connection, reservation_id, penalty_id):
    """Call stored procedure to insert billing penalty."""
    cursor = connection.cursor()
    try:
        cursor.callproc('InsertBillingPenalty', [reservation_id, penalty_id])
        connection.commit()
        print("Billing penalty inserted successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()


def maintainupdatecar(connection,car_id,service_type,date_change):
    """Call stored procedure for car maintenance update."""
    cursor = connection.cursor()
    try:
        cursor.callproc('maintainupdatecar',[car_id,service_type,date_change])
        connection.commit()
        print("Car maintenance information updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def fetch_all_cars(connection):
    """Fetch all records from the Cars table."""
    cursor = connection.cursor()
    try:
        cursor.callproc('GetAllCars')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None
    

def get_favourite_location(connection):
    cursor = connection.cursor()
    try:
        cursor.callproc('LocationBasedAnalytics')
        result = []
        for result_set in cursor.stored_results():
            result = result_set.fetchall()
        return result
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    

def updatePenalty(connection, penalty_id, new_reason, new_cost):
    """Call stored procedure to update penalty details."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdatePenalty', [penalty_id, new_reason, new_cost])
        connection.commit()
        print("Penalty updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()

def updateDiscount(connection, discount_id, new_name, new_validity, new_percentage):
    """Call stored procedure to update a discount."""
    cursor = connection.cursor()
    try:
        cursor.callproc('UpdateDiscount', [discount_id, new_name, new_validity, new_percentage])
        connection.commit()
        print("Discount updated successfully.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()