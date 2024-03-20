import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import errorcode
import read_operations
import db_connection
# import update_operations
# import delete_operations
from create_operations import create_new_car_reservation, create_new_car, create_new_person, create_new_customer, \
    create_new_location, create_new_discount, create_new_penalty
from database_procedures import update_car,delete_car,update_reservation,delete_reservation,delete_penalty,\
    delete_discount,add_insurance,update_insurance,delete_insurance,toggle_cars_availability,\
        get_all_customers,updateActualDropoffTime,insertBillingPenalty,maintainupdatecar,fetch_all_cars,updatePenalty,updateDiscount,get_all_reservations
class CarRentalApp:
    def __init__(self, root):
        # self.show_locations = None
        self.add_employee = None
        self.car_tree = None
        self.root = root
        self.root.title("Car Rental System")
        self.root.geometry("1000x600")  # Adjust the size as needed
        self.root.configure(bg="lightblue")


        self.create_menu_bar()
        self.create_main_frame()

    def create_menu_bar(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

    

        # File Menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Reservation Menu
        reservation_menu = tk.Menu(self.menu_bar, tearoff=0)
        reservation_menu.add_command(label="View Reservations", command=self.show_reservations)
        reservation_menu.add_command(label="New Reservation", command=self.add_reservation)
        self.menu_bar.add_cascade(label="Reservations", menu=reservation_menu)

        # Car Management Menu
        car_menu = tk.Menu(self.menu_bar, tearoff=0)
        car_menu.add_command(label="View Cars", command=self.show_cars)
        car_menu.add_command(label="Add Car", command=self.add_car)
        # car_menu.add_command(label="Manage Car Categories", command=self.edit_car)
        self.menu_bar.add_cascade(label="Car Management", menu=car_menu)

        # Customer Management Menu
        customer_menu = tk.Menu(self.menu_bar, tearoff=0)
        customer_menu.add_command(label="View Customers", command=self.show_customers)
        # customer_menu.add_command(label="Add Customer", command=self.add_customer)
        self.menu_bar.add_cascade(label="Customer Management", menu=customer_menu)

        # Employee Management Menu
        employee_menu = tk.Menu(self.menu_bar, tearoff=0)
        employee_menu.add_command(label="View Employees", command=self.show_employees)
        # employee_menu.add_command(label="Add Employee", command=self.add_employee)
        self.menu_bar.add_cascade(label="Employee Management", menu=employee_menu)

        # Location Management Menu
        location_menu = tk.Menu(self.menu_bar, tearoff=0)
        location_menu.add_command(label="View Locations", command=self.show_locations)
        # location_menu.add_command(label="Add Location", command=self.add_location)
        self.menu_bar.add_cascade(label="Location Management", menu=location_menu)

        # Insurance and Discounts Menu
        insurance_menu = tk.Menu(self.menu_bar, tearoff=0)
        insurance_menu.add_command(label="View Insurances", command=self.show_insurances)
        # insurance_menu.add_command(label="Manage Insurances", command=self.manage_insurances)
        insurance_menu.add_command(label="View Discounts", command=self.show_discounts)
        # insurance_menu.add_command(label="Manage Discounts", command=self.manage_discounts)
        self.menu_bar.add_cascade(label="Insurance & Discounts", menu=insurance_menu)

        # Penalties and Payments Menu
        penalty_menu = tk.Menu(self.menu_bar, tearoff=0)
        penalty_menu.add_command(label="View Penalties", command=self.show_penalties)
        # penalty_menu.add_command(label="Manage Penalties", command=self.manage_penalties)
        penalty_menu.add_command(label="View Payments", command=self.show_payments)
        # penalty_menu.add_command(label="View Payments", command=self.show_payments)
        self.menu_bar.add_cascade(label="Penalties & Payments", menu=penalty_menu)

        analysis_menu = tk.Menu(self.menu_bar, tearoff=0)
        analysis_menu.add_command(label="View Location/Revenue Analysis", command=self.show_location_analysis)
        analysis_menu.add_command(label="View Location/Car Analysis", command=self.show_car_analysis)
        analysis_menu.add_command(label="View Car Analysis", command=self.show_popular_car_categories)
        self.menu_bar.add_cascade(label="Analysis", menu=analysis_menu)

    def show_popular_car_categories(self):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual database connection details

        
        cursor = connection.cursor(dictionary=True)

            # Call the stored procedure to get analysis data
        cursor.callproc("PopularCarCategories")  # Replace with your actual procedure name

            # Fetch all the rows from the result set
        for result in cursor.stored_results():
            x=result.fetchall()


            # Prepare data for plotting
        carCategory = [entry['CarCategoryType'] for entry in x]
        reservation_counts = [entry['ReservationCount'] for entry in x]
    

            # Plot the bar chart
        plt.bar(carCategory, reservation_counts, label='Reservation Count')
        

            # Add labels and legend
        plt.xlabel('Car Category')
        plt.ylabel('Reservation Count')
        plt.title('Category-wise Car Reservation Count')
        plt.legend()

            # Show the plot
        plt.show()

        
        cursor.close()
        connection.close()


    def show_car_analysis(self):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual database connection details

        
        cursor = connection.cursor(dictionary=True)

            # Call the stored procedure to get analysis data
        cursor.callproc("LocationBasedAnalytics")  # Replace with your actual procedure name

            # Fetch all the rows from the result set
        for result in cursor.stored_results():
            x=result.fetchall()


            # Prepare data for plotting
        cities = [entry['City'] for entry in x]
        reservation_counts = [entry['ReservationCount'] for entry in x]
        total_revenues = [entry['TotalRevenue'] for entry in x]

            # Plot the bar chart
        plt.bar(cities, reservation_counts, label='Reservation Count')
        #plt.bar(cities, total_revenues, label='Total Revenue', alpha=0.5)

            # Add labels and legend
        plt.xlabel('City')
        plt.ylabel('Count/Revenue')
        plt.title('City-wise Car Reservation Count')
        plt.legend()

            # Show the plot
        plt.show()

        
        cursor.close()
        connection.close()

    

    def show_location_analysis(self):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual database connection details

        
        cursor = connection.cursor(dictionary=True)

            # Call the stored procedure to get analysis data
        cursor.callproc("LocationBasedAnalytics")  # Replace with your actual procedure name

            # Fetch all the rows from the result set
        for result in cursor.stored_results():
            x=result.fetchall()


            # Prepare data for plotting
        cities = [entry['City'] for entry in x]
        total_revenues = [entry['TotalRevenue'] for entry in x]

            # Plot the bar chart
        #plt.bar(cities, reservation_counts, label='Reservation Count')
        plt.bar(cities, total_revenues, label='Total Revenue', alpha=0.5)

            # Add labels and legend
        plt.xlabel('City')
        plt.ylabel('Count/Revenue')
        plt.title('City-wise Generated revenue')
        plt.legend()

            # Show the plot
        plt.show()

        
        cursor.close()
        connection.close()


    

    def create_main_frame(self):
        style = ttk.Style()
        style.configure("TFrame", background="PaleVioletRed1")
        self.main_frame = ttk.Frame(self.root,style="TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
      


    # Placeholder methods for menu commands
    def show_reservations(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.reservation_tree = ttk.Treeview(self.main_frame, columns=("ID", "Customer", "CarBrand","Car Type", "Insurance", "Discount","PicUpLOcation","DropOffLocation","PickUpTime","DropOffTime","ActualDropOffTime","BillingDate","TotalCost"),
                                             show='headings')
        self.reservation_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.reservation_tree["columns"]:
            self.reservation_tree.heading(col, text=col)

        # Fetch data from backend and populate the tree
        self.populate_reservations()

        # Add a button for car reservation
        tk.Button(self.main_frame, text="Edit Reservation", command=self.edit_reservation,bg="orange").pack(side=tk.LEFT)
        tk.Button(self.main_frame, text="Delete Reservation", command=self.delete_reservation,bg="orange").pack(side=tk.RIGHT)
        tk.Button(self.main_frame, text="Update DropOff", command=self.update_actual_dropoff_time,bg="orange").pack(side=tk.RIGHT)
        tk.Button(self.main_frame, text="Add Penalty", command=self.add_penalty_reservation,bg="orange").pack(side=tk.RIGHT)

    def add_penalty_reservation(self):
        selected_item = self.reservation_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No reservation selected")
            return
        
        manage_penalty_win = tk.Toplevel(self.root)
        manage_penalty_win.title("Add Penalty")

        reservation_id = self.reservation_tree.item(selected_item, "values")[0]

        tk.Label(manage_penalty_win, text="Penalty ID").grid(row=0, column=0)
        penalty_id_entry = tk.Entry(manage_penalty_win)
        penalty_id_entry.grid(row=0, column=1)

        submit_button = tk.Button(manage_penalty_win, text="Submit",
                                  command=lambda: self.insert_billing_penalty(reservation_id,penalty_id_entry.get()))
        submit_button.grid(row=1, column=1)

    def insert_billing_penalty(self, reservation_id,penalty_id):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        try:
            insertBillingPenalty(connection, reservation_id, penalty_id)
            print("Penalty added")
            self.populate_reservations()  # Refresh reservation list
        except Exception as e:
            print(f"Error updating car: {e}")
        finally:
            db_connection.close_db_connection(connection)


    def update_actual_dropoff_time(self):
        selected_item = self.reservation_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No reservation selected")
            return
        
        manage_dropOff_win = tk.Toplevel(self.root)
        manage_dropOff_win.title("Actual DroppOff Time")

        reservation_id = self.reservation_tree.item(selected_item, "values")[0]


        tk.Label(manage_dropOff_win, text="Date (YYYY-MM-DD) Time (HH-MM-SS)").grid(row=0, column=0)
        date_entry = tk.Entry(manage_dropOff_win)
        date_entry.grid(row=0, column=1)

        submit_button = tk.Button(manage_dropOff_win, text="Submit",
                                  command=lambda: self.generate_bill(reservation_id,date_entry.get()))
        submit_button.grid(row=1, column=1)

    def generate_bill(self, reservation_id,date):
        print(reservation_id)
        print(date)
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        try:
            updateActualDropoffTime(connection, reservation_id, date)
            print("DropOff Time updated")
            self.populate_reservations()  # Refresh reservation list
        except Exception as e:
            print(f"Error updating car: {e}")
        finally:
            db_connection.close_db_connection(connection)
        

    
    
        

    # Data doesn't show up in correct format (Malav)
    def populate_reservations(self):
        # Clear existing data in the tree
        for i in self.reservation_tree.get_children():
            self.reservation_tree.delete(i)

        # Fetch data from backend and populate the tree
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual database connection details
        # Changes by Malav
        reservations = get_all_reservations(connection)
        db_connection.close_db_connection(connection)  # Close the database connection after fetching data

        for res in reservations:
            # Assuming each reservation is a tuple in the format (id, customer_id, car_id, pickup_time, dropoff_time, ...)
            item_id = self.reservation_tree.insert("", tk.END, values=res)
            
            self.reservation_tree.tag_configure("red_text",background="PaleVioletRed1")
            self.reservation_tree.item(item_id, tags=("red_text",))

    def add_reservation(self):
        # # Open a new window for reservation details
        # add_res_win = tk.Toplevel(self.root)
        # add_res_win.title("Add Reservation")

        # # Example fields: Customer ID, Car ID, etc.
        # tk.Label(add_res_win, text="Customer ID").grid(row=0, column=0)
        # customer_id_entry = tk.Entry(add_res_win)
        # customer_id_entry.grid(row=0, column=1)

        # # Similar fields for Car ID, Pick Up, Drop Off, etc.
        # # ...

        # # Submit Button
        # submit_button = tk.Button(add_res_win, text="Submit",
        #                           command=lambda: self.submit_new_reservation(customer_id_entry.get(),
        #                                                                       ...))  # Add other fields as arguments
        # submit_button.grid(row=6, column=1)


         # Open a new window for reservation details
        add_res_win = tk.Toplevel(self.root)
        add_res_win.title("Add Reservation")

        # Customer ID
        tk.Label(add_res_win, text="Customer ID").grid(row=0, column=0)
        customer_id_entry = tk.Entry(add_res_win)
        customer_id_entry.grid(row=0, column=1)

        # Car ID
        tk.Label(add_res_win, text="Car ID").grid(row=1, column=0)
        car_id_entry = tk.Entry(add_res_win)
        car_id_entry.grid(row=1, column=1)

        # Insurance ID
        tk.Label(add_res_win, text="Insurance ID").grid(row=2, column=0)
        insurance_id_entry = tk.Entry(add_res_win)
        insurance_id_entry.grid(row=2, column=1)

        # Discount ID
        tk.Label(add_res_win, text="Discount ID").grid(row=3, column=0)
        discount_id_entry = tk.Entry(add_res_win)
        discount_id_entry.grid(row=3, column=1)

        # Pick Up Location
        tk.Label(add_res_win, text="Pick Up Location").grid(row=4, column=0)
        pickup_location_entry = tk.Entry(add_res_win)
        pickup_location_entry.grid(row=4, column=1)

        # Drop Off Location
        tk.Label(add_res_win, text="Drop Off Location").grid(row=5, column=0)
        dropoff_location_entry = tk.Entry(add_res_win)
        dropoff_location_entry.grid(row=5, column=1)

        # Pick Up Time
        tk.Label(add_res_win, text="Pick Up Time").grid(row=6, column=0)
        pickup_time_entry = tk.Entry(add_res_win)
        pickup_time_entry.grid(row=6, column=1)

        # Drop Off Time
        tk.Label(add_res_win, text="Drop Off Time").grid(row=7, column=0)
        dropoff_time_entry = tk.Entry(add_res_win)
        dropoff_time_entry.grid(row=7, column=1)

        # Submit Button
        submit_button = tk.Button(add_res_win, text="Submit",
                                  command=lambda: self.submit_new_reservation(
                                      customer_id_entry.get(),
                                      car_id_entry.get(),
                                      insurance_id_entry.get(),
                                      discount_id_entry.get(),
                                      pickup_location_entry.get(),
                                      dropoff_location_entry.get(),
                                      pickup_time_entry.get(),
                                      dropoff_time_entry.get()
                                  ))
        submit_button.grid(row=8, column=1)

    def edit_reservation(self):
        selected_item = self.reservation_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No reservation selected")
            return
        # Open a form similar to add_reservation, but pre-fill with selected reservation details
        reservation_details = self.reservation_tree.item(selected_item, "values")
        edit_res_win = tk.Toplevel(self.root)
        edit_res_win.title("Edit Reservation")

        # Pick Up Location
        tk.Label(edit_res_win, text="Pick Up Location").grid(row=4, column=0)
        pickup_location_entry = tk.Entry(edit_res_win)
        pickup_location_entry.grid(row=4, column=1)
        pickup_location_entry.insert(0, reservation_details[5])  # Pre-fill with selected reservation's pick up location

        # Drop Off Location
        tk.Label(edit_res_win, text="Drop Off Location").grid(row=5, column=0)
        dropoff_location_entry = tk.Entry(edit_res_win)
        dropoff_location_entry.grid(row=5, column=1)
        dropoff_location_entry.insert(0, reservation_details[6])  # Pre-fill with selected reservation's drop off location

        # Pick Up Time
        tk.Label(edit_res_win, text="Pick Up Time").grid(row=6, column=0)
        pickup_time_entry = tk.Entry(edit_res_win)
        pickup_time_entry.grid(row=6, column=1)
        pickup_time_entry.insert(0, reservation_details[7])  # Pre-fill with selected reservation's pick up time

        # Drop Off Time
        tk.Label(edit_res_win, text="Drop Off Time").grid(row=7, column=0)
        dropoff_time_entry = tk.Entry(edit_res_win)
        dropoff_time_entry.grid(row=7, column=1)
        dropoff_time_entry.insert(0, reservation_details[8])  # Pre-fill with selected reservation's drop off time

        # Submit Button
        submit_button = tk.Button(edit_res_win, text="Submit",
                                    command=lambda: self.submit_edited_reservation(
                                        pickup_location_entry.get(),
                                        dropoff_location_entry.get(),
                                        pickup_time_entry.get(),
                                        dropoff_time_entry.get()
                                    ))
        
        submit_button.grid(row=8, column=1)

    def submit_edited_reservation(self, pickup_location, dropoff_location,
                                    pickup_time, dropoff_time):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        # Prepare data for the edited car
        edited_reservation_data = (pickup_location, dropoff_location,
                                    pickup_time, dropoff_time)

        # Get the car ID from the selected item in the Treeview
        selected_item = self.reservation_tree.focus()
        reservation_id = self.reservation_tree.item(selected_item, "values")[0]

        # Update the car in the database
        try:
            update_reservation(connection, reservation_id, *edited_reservation_data)
            print("Reservation updated")
            
            self.populate_reservations()  # Refresh reservation list
        except Exception as e:
            print(f"Error updating car: {e}")
        finally:
            db_connection.close_db_connection(connection)


    def delete_reservation(self):
        selected_item = self.reservation_tree.focus()
        reservation_id = self.reservation_tree.item(selected_item, 'values')[0]

        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        try:
            delete_reservation(connection, reservation_id)
            self.populate_reservations()  # Refresh reservation list
        except mysql.connector.Error as e:
                messagebox.showerror("Error", "Cannot delete the reservation. It is referenced in other records.")
            
        finally:
            db_connection.close_db_connection(connection)

        # Add logic to delete reservation from database

    def submit_new_reservation(self, customer_id, car_id, insurance_id, discount_id, pickup_location, dropoff_location,
                               pickup_time, dropoff_time):
        # Validate inputs (example: ensure IDs are integers, dates are correctly formatted, etc.)
        try:
            customer_id = int(customer_id)
            car_id = int(car_id)
            insurance_id = int(insurance_id)
            discount_id = int(discount_id) if discount_id else None  # Assuming discount_id can be optional
            pickup_location = int(pickup_location)
            dropoff_location = int(dropoff_location)
            # Ensure dates are in correct format, total_cost is a valid number, etc.
        except ValueError:
            print("Invalid input. Please check your data.")
            return

        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual database connection details

        # Call the backend function to add the new reservation
        try:
            create_new_car_reservation(connection, customer_id, car_id, insurance_id, discount_id, pickup_location,
                                       dropoff_location, pickup_time, dropoff_time)
            print("New reservation added successfully.")
            # self.add_res_win.destroy()
        except Exception as e:
            print(f"Error adding reservation: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def show_cars(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.car_tree = ttk.Treeview(self.main_frame, columns=("Car ID", "Brand", "Type", "Car Fixed Cost", "Garage Name","CarServiceType","ServiceDueDate","LicensePlate","Model","ModelYear","Availability"),
                                     show='headings')
        
        self.car_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.car_tree["columns"]:
            self.car_tree.heading(col, text=col)

        # Fetch car data from the backend and populate the tree
        self.populate_cars()

        # Create a button
        tk.Button(self.main_frame, text="Edit Car", command=self.edit_car,bg="orange").pack(side=tk.LEFT)
        tk.Button(self.main_frame, text="Delete Car", command=self.delete_car,bg="orange").pack(side=tk.RIGHT)
        tk.Button(self.main_frame, text="Toggle Availability", command=self.manage_car_availability,bg="orange").pack(side=tk.RIGHT)
        tk.Button(self.main_frame, text="Maintain Car", command=self.maintain_car,bg="orange").pack(side=tk.RIGHT)

    def maintain_car(self):
        selected_item = self.car_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No car selected")
            return
        
        car_details = self.car_tree.item(selected_item, "values")

        manage_maintain_win = tk.Toplevel(self.root)
        manage_maintain_win.title("Maintain Car")

        car_id = self.car_tree.item(selected_item, "values")[0]

        tk.Label(manage_maintain_win, text="Service Type").grid(row=0, column=0)
        maintain_service_entry = tk.Entry(manage_maintain_win)
        maintain_service_entry.grid(row=0, column=1)
        maintain_service_entry.insert(0, car_details[5])  # Pre-fill with selected car's service type
        
        tk.Label(manage_maintain_win, text="Due Date").grid(row=1, column=0)
        maintain_due_date_entry = tk.Entry(manage_maintain_win)
        maintain_due_date_entry.grid(row=1, column=1)
        maintain_due_date_entry.insert(0, car_details[6])  # Pre-fill with selected car's due date

        submit_button = tk.Button(manage_maintain_win, text="Submit",
                                    command=lambda: self.update_maintain_car(car_id,maintain_service_entry.get(),maintain_due_date_entry.get()))
        submit_button.grid(row=2, column=1)

    def update_maintain_car(self, car_id,service_type,due_date):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        try:
            maintainupdatecar(connection, car_id,service_type,due_date)
            print("Car updated")
            self.populate_cars()  # Refresh car list
        except Exception as e:
            print(f"Error updating car: {e}")
        finally:
            db_connection.close_db_connection(connection)
        

    

    def manage_car_availability(self):
        # Create a new window for managing car availability
        manage_availability_win = tk.Toplevel(self.root)
        manage_availability_win.title("Manage Car Availability")

        # Label and Entry for Date
        tk.Label(manage_availability_win, text="Date (YYYY-MM-DD)").grid(row=0, column=0)
        date_entry = tk.Entry(manage_availability_win)
        date_entry.grid(row=0, column=1)

        # Submit Button
        submit_button = tk.Button(manage_availability_win, text="Submit",
                                  command=lambda: self.toggle_cars_availability(date_entry.get()))
        submit_button.grid(row=1, column=1)
        self.populate_cars()
    
    def toggle_cars_availability(self, date):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        print("Here")
        try:
            toggle_cars_availability(connection, date)
            self.populate_cars()  # Refresh car list
        except mysql.connector.Error as e:
                messagebox.showerror("Error", "Cannot toggle availability. Please check your input.")


    def populate_cars(self):
        # Clear existing data in the tree
        for i in self.car_tree.get_children():
            self.car_tree.delete(i)

        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        # Fetch car data from backend
        try:
            cars = fetch_all_cars(connection)
            for car in cars:
                # Assuming the car data is returned as a tuple or list in the order of columns
                item_id = self.car_tree.insert("", tk.END, values=car)

                # Apply red text to the specific item
                self.car_tree.tag_configure("red_text",background="PaleVioletRed1")
                self.car_tree.item(item_id, tags=("red_text",))
        except Exception as e:
            print(f"Error fetching cars: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def add_car(self):
        # # Open a form to add a new car
        # add_car_win = tk.Toplevel(self.root)
        # add_car_win.title("Add New Car")

        # # Example fields: Brand, Model, Type, etc.
        # tk.Label(add_car_win, text="Brand").grid(row=0, column=0)
        # brand_entry = tk.Entry(add_car_win)
        # brand_entry.grid(row=0, column=1)

        # # Similar fields for Model, Type, etc.
        # # ...

        # # Submit Button
        # submit_button = tk.Button(add_car_win, text="Submit", command=lambda: self.submit_new_car(brand_entry.get(),
        #                                                                                           ...))  # Add other fields as arguments
        # submit_button.grid(row=6, column=1)
       
            # Open a form to add a new car
            self.add_car_win = tk.Toplevel(self.root)
            self.add_car_win.title("Add New Car")

            # Car Brand
            tk.Label(self.add_car_win, text="Brand").grid(row=0, column=0)
            brand_entry = tk.Entry(self.add_car_win)
            brand_entry.grid(row=0, column=1)

            # Car Type
            tk.Label(self.add_car_win, text="Type").grid(row=1, column=0)
            type_entry = tk.Entry(self.add_car_win)
            type_entry.grid(row=1, column=1)

            # Car Category ID
            tk.Label(self.add_car_win, text="Category ID").grid(row=2, column=0)
            category_id_entry = tk.Entry(self.add_car_win)
            category_id_entry.grid(row=2, column=1)

            # Car Garage ID
            tk.Label(self.add_car_win, text="Garage ID").grid(row=3, column=0)
            garage_id_entry = tk.Entry(self.add_car_win)
            garage_id_entry.grid(row=3, column=1)

            # Car Service Type
            tk.Label(self.add_car_win, text="Service Type").grid(row=4, column=0)
            service_type_entry = tk.Entry(self.add_car_win)
            service_type_entry.grid(row=4, column=1)

            # Service Due Date
            tk.Label(self.add_car_win, text="Due Date").grid(row=5, column=0)
            due_date_entry = tk.Entry(self.add_car_win)
            due_date_entry.grid(row=5, column=1)

            # License Plate
            tk.Label(self.add_car_win, text="License Plate").grid(row=6, column=0)
            license_plate_entry = tk.Entry(self.add_car_win)
            license_plate_entry.grid(row=6, column=1)

            # Car Model
            tk.Label(self.add_car_win, text="Model").grid(row=7, column=0)
            model_entry = tk.Entry(self.add_car_win)
            model_entry.grid(row=7, column=1)

            # Car Model Year
            tk.Label(self.add_car_win, text="Model Year").grid(row=8, column=0)
            model_year_entry = tk.Entry(self.add_car_win)
            model_year_entry.grid(row=8, column=1)

            # Car Availability
            tk.Label(self.add_car_win, text="Availability").grid(row=9, column=0)
            availability_entry = tk.Entry(self.add_car_win)
            availability_entry.grid(row=9, column=1)

            # Submit Button
            submit_button = tk.Button(self.add_car_win, text="Submit",
                                    command=lambda: self.submit_new_car(
                                        brand_entry.get(),
                                        type_entry.get(),
                                        category_id_entry.get(),
                                        garage_id_entry.get(),
                                        service_type_entry.get(),
                                        due_date_entry.get(),
                                        license_plate_entry.get(),
                                        model_entry.get(),
                                        model_year_entry.get(),
                                        availability_entry.get()
                                    ))
            submit_button.grid(row=10, column=1)

    def submit_new_car(self, brand, car_type, category_id, garage_id, service_type, service_due_date, license_plate,
                       model, model_year, availability):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        # Prepare data for the new car
        car_data = (
            brand, car_type, category_id, garage_id, service_type, service_due_date, license_plate, model, model_year,
            availability)

        # Add new car to the database
        try:
            create_new_car(connection, *car_data)
            print("New car added")
            self.populate_cars()  # Refresh car list
            self.add_car_win.destroy()
        except Exception as e:
            print(f"Error adding new car: {e}")
        finally:
            db_connection.close_db_connection(connection)

    # def edit_car(self):
    #     selected_item = self.car_tree.focus()
    #     if not selected_item:
    #         tk.messagebox.showerror("Error", "No car selected")
    #         return
    #     # Open a form similar to add_car, but pre-fill with selected car details

    def edit_car(self):
        selected_item = self.car_tree.focus()
        print(selected_item)
        if not selected_item:
            tk.messagebox.showerror("Error", "No car selected")
            return

        # Get car details from the selected item in the Treeview (replace this with your actual data retrieval)
        car_details = self.car_tree.item(selected_item, "values")

        # Open a form similar to add_car, pre-fill with selected car details
        edit_car_win = tk.Toplevel(self.root)
        edit_car_win.title("Edit Car")

        # Example fields: Brand, Type, etc.
        tk.Label(edit_car_win, text="Brand").grid(row=0, column=0)
        brand_entry = tk.Entry(edit_car_win)
        brand_entry.grid(row=0, column=1)
        brand_entry.insert(0, car_details[1])  # Pre-fill with selected car's brand

        # Car Type
        tk.Label(edit_car_win, text="Type").grid(row=1, column=0)
        type_entry = tk.Entry(edit_car_win)
        type_entry.grid(row=1, column=1)
        type_entry.insert(0, car_details[2])  # Pre-fill with selected car's type

        # Car Category ID
        tk.Label(edit_car_win, text="Category ID").grid(row=2, column=0)
        category_id_entry = tk.Entry(edit_car_win)
        category_id_entry.grid(row=2, column=1)
        category_id_entry.insert(0, car_details[3])  # Pre-fill with selected car's category ID

        # Car Garage ID
        tk.Label(edit_car_win, text="Garage ID").grid(row=3, column=0)
        garage_id_entry = tk.Entry(edit_car_win)
        garage_id_entry.grid(row=3, column=1)
        garage_id_entry.insert(0, car_details[4])  # Pre-fill with selected car's garage ID

        # Car Service Type
        tk.Label(edit_car_win, text="Service Type").grid(row=4, column=0)
        service_type_entry = tk.Entry(edit_car_win)
        service_type_entry.grid(row=4, column=1)
        service_type_entry.insert(0, car_details[5])  # Pre-fill with selected car's service type

        # Service Due Date
        tk.Label(edit_car_win, text="Due Date").grid(row=5, column=0)
        due_date_entry = tk.Entry(edit_car_win)
        due_date_entry.grid(row=5, column=1)
        due_date_entry.insert(0, car_details[6])  # Pre-fill with selected car's due date

        # License Plate
        tk.Label(edit_car_win, text="License Plate").grid(row=6, column=0)
        license_plate_entry = tk.Entry(edit_car_win)
        license_plate_entry.grid(row=6, column=1)
        license_plate_entry.insert(0, car_details[7])  # Pre-fill with selected car's license plate

        # Car Model
        tk.Label(edit_car_win, text="Model").grid(row=7, column=0)
        model_entry = tk.Entry(edit_car_win)
        model_entry.grid(row=7, column=1)
        model_entry.insert(0, car_details[8])  # Pre-fill with selected car's model

        # Car Model Year
        tk.Label(edit_car_win, text="Model Year").grid(row=8, column=0)
        model_year_entry = tk.Entry(edit_car_win)
        model_year_entry.grid(row=8, column=1)
        model_year_entry.insert(0, car_details[9])  # Pre-fill with selected car's model year

        # Car Availability
        tk.Label(edit_car_win, text="Availability").grid(row=9, column=0)
        availability_entry = tk.Entry(edit_car_win)
        availability_entry.grid(row=9, column=1)
        availability_entry.insert(0, car_details[10])  # Pre-fill with selected car's availability

        # Submit Button
        submit_button = tk.Button(edit_car_win, text="Submit",
                                  command=lambda: self.submit_edited_car(brand_entry.get(),type_entry.get(),
                                                                         category_id_entry.get(),garage_id_entry.get(),
                                                                         service_type_entry.get(),due_date_entry.get(),
                                                                         license_plate_entry.get(),model_entry.get(),model_year_entry.get(),
                                                                         availability_entry.get()))
        submit_button.grid(row=10, column=1)

    def submit_edited_car(self, brand, car_type, category_id, garage_id, service_type, service_due_date, license_plate,
                          model, model_year, availability):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        # Prepare data for the edited car
        edited_car_data = (
            brand, car_type, category_id, garage_id, service_type, service_due_date, license_plate, model, model_year,
            availability)

        # Get the car ID from the selected item in the Treeview
        selected_item = self.car_tree.focus()
        car_id = self.car_tree.item(selected_item, "values")[0]

        # Update the car in the database
        try:
            update_car(connection, car_id, *edited_car_data)
            print("Car updated")
            self.populate_cars()  # Refresh car list
            self.edit_car_win.destroy()
        except Exception as e:
            print(f"Error updating car: {e}")
        finally:
            db_connection.close_db_connection(connection)

        # Close the window after submission
        self.edit_car_win.destroy()

    def delete_car(self):
        selected_item = self.car_tree.focus()
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details
        car_id = self.car_tree.item(selected_item, 'values')[0]
        try:
            delete_car(connection, car_id)
            self.populate_cars()  # Refresh car list
        except mysql.connector.Error as e:
            # if e.errno == errorcode.ER_ROW_IS_REFERENCED_2:  # Check for foreign key constraint violation error code
                messagebox.showerror("Error", "Cannot delete the car. It is referenced in other records.")
            # else:
            #     print(f"Error deleting car: {e}")
        finally:
            db_connection.close_db_connection(connection)
    
        # Add logic to delete car from database

    def manage_car_categories(self):
        # Open a new window for managing car categories
        car_cat_win = tk.Toplevel(self.root)
        car_cat_win.title("Manage Car Categories")

        # Treeview to display car categories
        self.car_cat_tree = ttk.Treeview(car_cat_win, columns=("Category ID", "Type", "Seating Capacity", "Fixed Cost"),
                                         show='headings')
        self.car_cat_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.car_cat_tree["columns"]:
            self.car_cat_tree.heading(col, text=col)

        # Fetch car category data from the backend and populate the tree
        self.populate_car_categories()

    def populate_car_categories(self):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        # Fetch car categories from the database
        try:
            car_categories = read_operations.fetch_car_category_details(connection)
            for cat in car_categories:
                self.car_cat_tree.insert("", tk.END, values=(
                    cat[0], cat[1], cat[2], cat[3]))  # Assuming columns are ID, Type, Seating Capacity, Fixed Cost
        except Exception as e:
            print(f"Error fetching car categories: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def show_customers(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.customer_tree = ttk.Treeview(self.main_frame, columns=("Customer ID", "First Name", "Last Name","Email", "Phone","Driving License"),
                                          show='headings')
        self.customer_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.customer_tree["columns"]:
            self.customer_tree.heading(col, text=col)

        # Fetch customer data from backend and populate the tree
        self.populate_customers()

    def populate_customers(self):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        # Fetch customer data from the database
        try:
            customers = get_all_customers(connection)
            for customer in customers:
                # Assuming columns are CustomerID, PersonID, DrivingLicense
                item_id = self.customer_tree.insert("", tk.END, values=(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5]))
                self.customer_tree.tag_configure("red_text",background="PaleVioletRed1")
                self.customer_tree.item(item_id, tags=("red_text",))
        except Exception as e:
            print(f"Error fetching customers: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def add_customer(self):
        # Open a form to add a new customer
        add_cust_win = tk.Toplevel(self.root)
        add_cust_win.title("Add New Customer")

        # Example fields: Name, Email, Phone, etc.
        tk.Label(add_cust_win, text="Name").grid(row=0, column=0)
        name_entry = tk.Entry(add_cust_win)
        name_entry.grid(row=0, column=1)

        # Similar fields for Email, Phone, etc.
        # ...

        # Submit Button
        submit_button = tk.Button(add_cust_win, text="Submit",
                                  command=lambda: self.submit_new_customer(name_entry.get(),
                                                                           ...))  # Add other fields as arguments
        submit_button.grid(row=4, column=1)

    def submit_new_customer(self, name, email, phone, location_id, dob, person_id=None):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        # Process new customer data and add to the database
        try:
            # Assuming 'name' includes first and last name separated by space
            first_name, last_name = name.split(" ", 1)
            gender = "Unknown"  # Placeholder, modify as needed

            # Create new person record
            create_new_person(connection, first_name, last_name, gender, email, phone, location_id, dob)

            # Fetch the PersonID of the newly created person
            # This step is required if your PersonID is auto-generated by the database
            # Implement a function in read_operations to fetch the latest PersonID

            # Assume person_id is fetched and stored in person_id variable

            # Create new customer record
            driving_license = "YourLogicForLicense"  # Implement your logic for generating a driving license number
            create_new_customer(connection, person_id, driving_license)

            print("New customer added")
        except Exception as e:
            print(f"Error adding new customer: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def show_employees(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.employee_tree = ttk.Treeview(self.main_frame, columns=("Employee ID", "Name", "Designation"),
                                          show='headings')
        self.employee_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.employee_tree["columns"]:
            self.employee_tree.heading(col, text=col)

        # Fetch employee data from backend and populate the tree
        self.populate_employees()

    def populate_employees(self):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        # Fetch employee data from the database
        try:
            employees = read_operations.fetch_all_employees(connection)
            for emp in employees:
                # Assuming the employee data includes EmployeeID, PersonFName, PersonLName, EmployeeDesignation
                employee_id = emp[0]
                name = f"{emp[1]} {emp[2]}"  # Concatenate first name and last name
                designation = emp[3]

                item_id = self.employee_tree.insert("", tk.END, values=(employee_id, name, designation))
                self.employee_tree.tag_configure("red_text",background="PaleVioletRed1")
                self.employee_tree.item(item_id, tags=("red_text",))
        except Exception as e:
            print(f"Error fetching employees: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def show_locations(self):
        print("Showing locations")
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.location_tree = ttk.Treeview(self.main_frame, columns=("Location ID", "Address", "City", "State"), show='headings')
        self.location_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.location_tree["columns"]:
            self.location_tree.heading(col, text=col)

        # Fetch location data from backend and populate the tree
        self.populate_locations()
    
    def populate_locations(self):

        # Fetch data from backend and populate the tree
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual database connection details
         # Close the database connection after fetching data

        try:
            # Fetch insurance data from the database
            locations = read_operations.fetch_all_locations(connection)

            # Clear existing data in the tree
            for i in self.location_tree.get_children():
                self.location_tree.delete(i)

            # Populate the tree with insurance data
            for ins in locations:
                item_id = self.location_tree.insert("", tk.END, values=(
                    ins[0], ins[1], ins[2], ins[3]))  # Adjust indices based on your database structure
                self.location_tree.tag_configure("red_text",background="PaleVioletRed1")
                self.location_tree.item(item_id, tags=("red_text",))

        except Exception as e:
            print(f"Error fetching locations: {e}")
        finally:
            db_connection.close_db_connection(connection)



    def add_location(self):
        # Open a form to add a new location
        add_loc_win = tk.Toplevel(self.root)
        add_loc_win.title("Add New Location")



        # Example fields: Address, City, State, etc.
        tk.Label(add_loc_win, text="Address").grid(row=0, column=0)
        address_entry = tk.Entry(add_loc_win)
        address_entry.grid(row=0, column=1)

        # Similar fields for City, State, etc.
        # ...

        tk.Label(add_loc_win, text="City").grid(row=1, column=0)
        city_entry = tk.Entry(add_loc_win)
        city_entry.grid(row=1, column=1)

        tk.Label(add_loc_win, text="State").grid(row=2, column=0)
        state_entry = tk.Entry(add_loc_win)
        state_entry.grid(row=2, column=1)

        tk.Label(add_loc_win, text="Country").grid(row=3, column=0)
        country_entry = tk.Entry(add_loc_win)
        country_entry.grid(row=3, column=1)

        tk.Label(add_loc_win, text="Zipcode").grid(row=4, column=0)
        zipcode_entry = tk.Entry(add_loc_win)
        zipcode_entry.grid(row=4, column=1)



        # Submit Button
        submit_button = tk.Button(add_loc_win, text="Submit",
                                  command=lambda: self.submit_new_location(address_entry.get(),city_entry.get(),state_entry.get(),country_entry.get(),zipcode_entry.get()))  # Add other fields as arguments
        submit_button.grid(row=5, column=1)

    def submit_new_location(self, address, city, state, country, zipcode):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        try:
            # Add the new location to the database
            create_new_location(connection, address, city, state, country, zipcode)
            print("New location added") 
            self.add_loc_win.destroy()  # Close the add location window
        except Exception as e:
            print(f"Error adding new location: {e}")
        finally:
            db_connection.close_db_connection(connection)


    def show_discounts(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.discount_tree = ttk.Treeview(self.main_frame, columns=("Discount ID", "Code", "Percentage"),
                                          show='headings')
        self.discount_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.discount_tree["columns"]:
            self.discount_tree.heading(col, text=col)

        # Fetch discount data from backend and populate the tree
        self.populate_discounts()

        tk.Button(self.main_frame, text="Edit Discount", command=self.manage_discounts,bg="orange").pack(side=tk.LEFT)

    def show_insurances(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.insurance_tree = ttk.Treeview(self.main_frame, columns=("Insurance ID", "Company", "Type", "Cost"),
                                           show='headings')
        self.insurance_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.insurance_tree["columns"]:
            self.insurance_tree.heading(col, text=col)

        # Fetch insurance data from backend and populate the tree
        self.populate_insurances()

        tk.Button(self.main_frame, text="Edit Insurance", command=self.manage_insurances,bg="orange").pack(side=tk.LEFT)

    def manage_insurances(self):
        # Open a new window for managing insurances
        ins_win = tk.Toplevel(self.root)
        ins_win.title("Manage Insurances")

        # Treeview to display insurances
        self.insurance_tree = ttk.Treeview(ins_win, columns=("Insurance ID", "Company", "Type", "Cost"),
                                           show='headings')
        self.insurance_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.insurance_tree["columns"]:
            self.insurance_tree.heading(col, text=col)

        # Fetch insurance data from the backend and populate the tree
        self.populate_insurances()

        # Add buttons for add, edit, delete insurance
        tk.Button(ins_win, text="Add Insurance", command=self.add_insurance,bg="orange").pack(side=tk.LEFT)
        tk.Button(ins_win, text="Edit Insurance", command=self.edit_insurance,bg="orange").pack(side=tk.LEFT)
        tk.Button(ins_win, text="Delete Insurance", command=self.delete_insurance,bg="orange").pack(side=tk.LEFT)


    def delete_insurance(self):
        selected_item = self.insurance_tree.focus()
        insurance_id = self.insurance_tree.item(selected_item, 'values')[0]

        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        try:
            delete_insurance(connection, insurance_id)
            self.populate_insurances()  # Refresh insurance list
        except mysql.connector.Error as e:
                messagebox.showerror("Error", "Cannot delete the insurance. It is referenced in other records.")
            
        finally:
            db_connection.close_db_connection(connection)

        # Add logic to delete insurance from database

    def edit_insurance(self):
        selected_item = self.insurance_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No insurance selected")
            return
        # Open a form similar to add_insurance, but pre-fill with selected insurance details
        insurance_details = self.insurance_tree.item(selected_item, "values")
        insurance_id = self.insurance_tree.item(selected_item, 'values')[0]
        edit_ins_win = tk.Toplevel(self.root)
        edit_ins_win.title("Edit Insurance")

        # Insurance Company
        tk.Label(edit_ins_win, text="Insurance Company").grid(row=0, column=0)
        company_entry = tk.Entry(edit_ins_win)
        company_entry.grid(row=0, column=1)
        company_entry.insert(0, insurance_details[1])

        # Insurance Type
        tk.Label(edit_ins_win, text="Insurance Type").grid(row=1, column=0)
        type_entry = tk.Entry(edit_ins_win)
        type_entry.grid(row=1, column=1)
        type_entry.insert(0, insurance_details[2])

        # Insurance Cost
        tk.Label(edit_ins_win, text="Insurance Cost").grid(row=2, column=0)
        cost_entry = tk.Entry(edit_ins_win)
        cost_entry.grid(row=2, column=1)
        cost_entry.insert(0, insurance_details[3])

        # Submit Button
        submit_button = tk.Button(edit_ins_win, text="Submit",
                                    command=lambda: self.submit_edited_insurance(
                                        insurance_id,
                                        company_entry.get(),
                                        type_entry.get(),
                                        cost_entry.get()
                                    ))
        submit_button.grid(row=3, column=1)

    def submit_edited_insurance(self, insurance_id,company, type, cost):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        try:
            # Update the discount in the database
            update_insurance(connection,insurance_id,company, type, cost)

            print("Discount updated")
            self.populate_insurances()  # Refresh the display of discounts

        except Exception as e:
            print(f"Error updating insurance: {e}")
        finally:
            db_connection.close_db_connection(connection)



    def add_insurance(self):
        # Open a new window for insurance details
        self.add_insurance_win = tk.Toplevel(self.root)
        self.add_insurance_win.title("Add New Insurance")

        # Insurance Company
        tk.Label(self.add_insurance_win, text="Insurance Company").grid(row=0, column=0)
        company_entry = tk.Entry(self.add_insurance_win)
        company_entry.grid(row=0, column=1)

        # Insurance Type
        tk.Label(self.add_insurance_win, text="Insurance Type").grid(row=1, column=0)
        type_entry = tk.Entry(self.add_insurance_win)
        type_entry.grid(row=1, column=1)

        # Insurance Cost
        tk.Label(self.add_insurance_win, text="Insurance Cost").grid(row=2, column=0)
        cost_entry = tk.Entry(self.add_insurance_win)
        cost_entry.grid(row=2, column=1)

        # Submit Button
        submit_button = tk.Button(self.add_insurance_win, text="Add",
                                  command=lambda: self.submit_new_insurance(
                                      company_entry.get(),
                                      type_entry.get(),
                                      cost_entry.get()
                                  ))
        submit_button.grid(row=3, column=1)

    def submit_new_insurance(self, company, type, cost):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        try:
            # Add the new discount to the database
            add_insurance(connection, company, type, cost)

            print("Discount added")
            self.populate_insurances()  # Update the discounts displayed
            
        except Exception as e:
            print(f"Error adding new insurance: {e}")
        finally:
            db_connection.close_db_connection(connection)


    def populate_insurances(self):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        try:
            # Fetch insurance data from the database
            insurances = read_operations.fetch_all_insurances(connection)

            # Clear existing data in the tree
            for i in self.insurance_tree.get_children():
                self.insurance_tree.delete(i)

            # Populate the tree with insurance data
            for ins in insurances:
                item_id = self.insurance_tree.insert("", tk.END, values=(
                    ins[0], ins[1], ins[2], ins[3]))  # Adjust indices based on your database structure
                self.insurance_tree.tag_configure("red_text",background="PaleVioletRed1")
                self.insurance_tree.item(item_id, tags=("red_text",))

        except Exception as e:
            print(f"Error fetching insurances: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def manage_discounts(self):
        # Open a new window for managing discounts
        self.discount_win = tk.Toplevel(self.root)
        self.discount_win.title("Manage Discounts")

        # Treeview to display discounts
        self.discount_tree = ttk.Treeview(self.discount_win, columns=("Discount ID", "Name", "Validity", "Percentage"),
                                          show='headings')
        self.discount_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.discount_tree["columns"]:
            self.discount_tree.heading(col, text=col)

        # Fetch discount data from the backend and populate the tree
        self.populate_discounts()

        # Add buttons for add, edit, delete discounts
        tk.Button(self.discount_win, text="Add Discount", command=self.add_discount,bg="orange").pack(side=tk.LEFT)
        tk.Button(self.discount_win, text="Edit Discount", command=self.edit_discount,bg="orange").pack(side=tk.LEFT)
        tk.Button(self.discount_win, text="Delete Discount", command=self.delete_discount,bg="orange").pack(side=tk.LEFT)

    def populate_discounts(self):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        try:
            # Fetch discount data from the database
            discounts = read_operations.fetch_all_discounts(connection)

            # Clear existing data in the tree
            for i in self.discount_tree.get_children():
                self.discount_tree.delete(i)

            # Populate the tree with discount data
            for disc in discounts:
                item_id = self.discount_tree.insert("", tk.END, values=(
                    disc[0], disc[1], disc[2], disc[3]))  # Adjust indices based on your database structure
                self.discount_tree.tag_configure("red_text",background="PaleVioletRed1")
                self.discount_tree.item(item_id, tags=("red_text",))

        except Exception as e:
            print(f"Error fetching discounts: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def add_discount(self):
        # Open a new window for discount details
        self.add_discount_win = tk.Toplevel(self.discount_win)
        self.add_discount_win.title("Add New Discount")

        # Discount Name
        tk.Label(self.add_discount_win, text="Discount Name").grid(row=0, column=0)
        name_entry = tk.Entry(self.add_discount_win)
        name_entry.grid(row=0, column=1)

        # Discount Validity
        tk.Label(self.add_discount_win, text="Discount Validity").grid(row=1, column=0)
        validity_entry = tk.Entry(self.add_discount_win)
        validity_entry.grid(row=1, column=1)

        # Discount Percentage
        tk.Label(self.add_discount_win, text="Discount Percentage").grid(row=2, column=0)
        percentage_entry = tk.Entry(self.add_discount_win)
        percentage_entry.grid(row=2, column=1)

        # Submit Button
        submit_button = tk.Button(self.add_discount_win, text="Add",
                                  command=lambda: self.submit_new_discount(
                                      name_entry.get(),
                                      validity_entry.get(),
                                      percentage_entry.get()
                                  ))
        submit_button.grid(row=3, column=1)

    def submit_new_discount(self, name, validity, percentage):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details

        try:
            # Add the new discount to the database
            create_new_discount(connection, name, validity, percentage)

            print("Discount added")
            self.populate_discounts()  # Update the discounts displayed
            self.add_discount_win.destroy()  # Close the add discount window
        except Exception as e:
            print(f"Error adding new discount: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def edit_discount(self):
        # Get selected item from discount_tree
        selected_item = self.discount_tree.focus()
        discount_data = self.discount_tree.item(selected_item, 'values')

        edit_discount_win = tk.Toplevel(self.discount_win)
        edit_discount_win.title("Edit Discount")

        # Pre-fill fields with existing data
        tk.Label(edit_discount_win, text="Name").grid(row=0, column=0)
        name_entry = tk.Entry(edit_discount_win)
        name_entry.insert(0, discount_data[1])  # Assuming name is the second field
        name_entry.grid(row=0, column=1)

        # Other fields for Validity and Percentage, pre-filled
        # ...
        tk.Label(edit_discount_win, text="Validity").grid(row=1, column=0)
        validity_entry = tk.Entry(edit_discount_win)
        validity_entry.insert(0, discount_data[2])  # Assuming validity is the third field
        validity_entry.grid(row=1, column=1)

        tk.Label(edit_discount_win, text="Percentage").grid(row=2, column=0)
        percentage_entry = tk.Entry(edit_discount_win)
        percentage_entry.insert(0, discount_data[3])  # Assuming percentage is the fourth field
        percentage_entry.grid(row=2, column=1)

        discount_id = discount_data[0]  # Assuming ID is the first field

        # Submit Button
        submit_button = tk.Button(edit_discount_win, text="Update",
                                  command=lambda: self.submit_discount_update(discount_id, name_entry.get(),
                                                                              validity_entry.get(),percentage_entry.get()))  # Include other fields
        submit_button.grid(row=3, column=1)

    def submit_discount_update(self, item_id, name, validity, percentage):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        try:
            # Update the discount in the database
            updateDiscount(connection, item_id, name, validity, percentage)

            print("Discount updated")
            self.populate_discounts()  # Refresh the display of discounts

        except Exception as e:
            print(f"Error updating discount: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def delete_discount(self):
        selected_item = self.discount_tree.focus()
        discount_id = self.discount_tree.item(selected_item, 'values')[0]  # Assuming ID is the first field
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        
         

        # Confirmation dialog
        # if tk.messagebox.askyesno("Delete Discount", "Are you sure you want to delete this discount?"):
            # Logic to delete the discount
            # backend.delete_discount(discount_id)
        print(discount_id)
        delete_discount(connection,discount_id)
        self.populate_discounts()  # Refresh the display of discounts
        print("Discount deleted")

    def show_penalties(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.penalty_tree = ttk.Treeview(self.main_frame, columns=("Penalty ID", "Reason", "Cost"), show='headings')
        self.penalty_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.penalty_tree["columns"]:
            self.penalty_tree.heading(col, text=col)

        # Fetch penalty data from backend and populate the tree
        self.populate_penalties()

        tk.Button(self.main_frame, text="Edit Penalty", command=self.manage_penalties,bg="orange").pack(side=tk.LEFT)

    # def show_payments(self):
    #     # Clear the main frame
    #     for widget in self.main_frame.winfo_children():
    #         widget.destroy()

    #     # Create a Treeview widget
    #     self.payment_tree = ttk.Treeview(self.main_frame, columns=("Payment ID", "Customer ID", "Amount", "Date"),
    #                                      show='headings')
    #     self.payment_tree.pack(fill=tk.BOTH, expand=True)

    #     # Define column headings
    #     for col in self.payment_tree["columns"]:
    #         self.payment_tree.heading(col, text=col)

    #     # Fetch payment data from backend and populate the tree
    #     self.populate_payments()

    #     tk.Button(self.main_frame, text="Edit Payment", command=self.manage_payments).pack(side=tk.LEFT)

    def manage_penalties(self):
        penalty_win = tk.Toplevel(self.root)
        penalty_win.title("Manage Penalties")

        self.penalty_tree = ttk.Treeview(penalty_win, columns=("Penalty ID", "Reason", "Cost"), show='headings')
        self.penalty_tree.pack(fill=tk.BOTH, expand=True)

        for col in self.penalty_tree["columns"]:
            self.penalty_tree.heading(col, text=col)

        self.populate_penalties()

        tk.Button(penalty_win, text="Add Penalty", command=self.add_penalty,bg="orange").pack(side=tk.LEFT)
        tk.Button(penalty_win, text="Edit Penalty", command=self.edit_penalty,bg="orange").pack(side=tk.LEFT)
        tk.Button(penalty_win, text="Delete Penalty", command=self.delete_penalty,bg="orange").pack(side=tk.LEFT)

    def populate_penalties(self):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        try:
            # Clear existing data in the tree
            for i in self.penalty_tree.get_children():
                self.penalty_tree.delete(i)

            # Fetch penalties from the database
            penalties = read_operations.fetch_all_penalties(connection)

            for penalty in penalties:
                item_id = self.penalty_tree.insert("", tk.END, values=(
                    penalty[0], penalty[1], penalty[2]))  # Assuming columns are ID, Reason, Cost
                self.penalty_tree.tag_configure("red_text",background="PaleVioletRed1")
                self.penalty_tree.item(item_id, tags=("red_text",))

        except Exception as e:
            print(f"Error fetching penalties: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def add_penalty(self):
        add_penalty_win = tk.Toplevel(self.root)
        add_penalty_win.title("Add New Penalty")

        tk.Label(add_penalty_win, text="Reason").grid(row=0, column=0)
        reason_entry = tk.Entry(add_penalty_win)
        reason_entry.grid(row=0, column=1)

        tk.Label(add_penalty_win, text="Cost").grid(row=1, column=0)
        cost_entry = tk.Entry(add_penalty_win)
        cost_entry.grid(row=1, column=1)

        submit_btn = tk.Button(add_penalty_win, text="Submit",
                               command=lambda: self.submit_new_penalty(reason_entry.get(), cost_entry.get()))
        submit_btn.grid(row=2, column=1)

    def submit_new_penalty(self, reason, cost):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        try:
            # Add the new penalty to the database
            create_new_penalty(connection, reason, cost)

            print("Penalty added")
            self.populate_penalties()  # Refresh the display of penalties

        except Exception as e:
            print(f"Error adding penalty: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def edit_penalty(self):
        selected_item = self.penalty_tree.focus()
        if not selected_item:
            tk.messagebox.showerror("Error", "No penalty selected")
            return
        penalty_id = self.penalty_tree.item(selected_item, 'values')[0]

        penalty_data = self.penalty_tree.item(selected_item, 'values')
        edit_penalty_win = tk.Toplevel(self.root)
        edit_penalty_win.title("Edit Penalty")

        tk.Label(edit_penalty_win, text="Reason").grid(row=0, column=0)
        reason_entry = tk.Entry(edit_penalty_win)
        reason_entry.insert(0, penalty_data[1])  # Assuming reason is the second field
        reason_entry.grid(row=0, column=1)

        tk.Label(edit_penalty_win, text="Cost").grid(row=1, column=0)
        cost_entry = tk.Entry(edit_penalty_win)
        cost_entry.insert(0, penalty_data[2])  # Assuming cost is the third field
        cost_entry.grid(row=1, column=1)

        

        submit_btn = tk.Button(edit_penalty_win, text="Update",
                               command=lambda: self.submit_penalty_update(penalty_id, reason_entry.get(),
                                                                          cost_entry.get()))
        submit_btn.grid(row=2, column=1)

    def submit_penalty_update(self, penalty_id, reason, cost):
        print(penalty_id, reason, cost)

        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        try:
            # Update the penalty in the database
            updatePenalty(connection, penalty_id, reason, cost)

            print("Penalty updated")
            self.populate_penalties()  # Refresh the display of penalties

        except Exception as e:
            print(f"Error updating penalty: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def delete_penalty(self):
        selected_item = self.penalty_tree.focus()
        if selected_item:  # Check if an item is selected
            penalty_id = self.penalty_tree.item(selected_item, 'values')[0]  # Assuming ID is the first field

    
                # Open database connection
            connection = db_connection.create_db_connection("host", "user", "password",
                                                                "db_name")  # Replace with actual details

            try:
                    # Delete the penalty from the database
                delete_penalty(connection, penalty_id)

                print("Penalty deleted")
                self.populate_penalties()  # Refresh the display of penalties

            except Exception as e:
                print(f"Error deleting penalty: {e}")
            finally:
                db_connection.close_db_connection(connection)

    def show_payments(self):
        payment_win = tk.Toplevel(self.root)
        payment_win.title("View Payments")

        self.payment_tree = ttk.Treeview(payment_win,
                                         columns=("Payment ID", "Type", "TransaactionID","Amount", "Status", "Date", "Reservation ID"),
                                         show='headings')
        self.payment_tree.pack(fill=tk.BOTH, expand=True)

        for col in self.payment_tree["columns"]:
            self.payment_tree.heading(col, text=col)

        self.populate_payments()

    def populate_payments(self):
        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        try:
            # Fetch payments from the database
            payments = read_operations.fetch_all_payments(connection)

            # Clear existing data in the tree
            for i in self.payment_tree.get_children():
                self.payment_tree.delete(i)

            # Populate the tree with payments data
            for payment in payments:
                item_id = self.payment_tree.insert("", tk.END, values=(
                    payment[0],  # Payment ID
                    payment[1],  # Type
                    payment[2],  
                    payment[3],  
                    payment[4],  
                    payment[5],
                    payment[6],))  
                self.payment_tree.tag_configure("red_text",background="PaleVioletRed1")
                self.payment_tree.item(item_id, tags=("red_text",))

        except Exception as e:
            print(f"Error fetching payments: {e}")
        finally:
            db_connection.close_db_connection(connection)


def main():
    root = tk.Tk()
    app = CarRentalApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
