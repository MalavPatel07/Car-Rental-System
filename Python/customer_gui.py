import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import read_operations
import db_connection
from create_operations import create_new_car_reservation, create_new_payment
from database_procedures import update_reservation,delete_reservation, update_customer_information, get_all_available_cars

class CarRentalApp:
    def __init__(self, root):
        # self.show_locations = None
        self.add_employee = None
        self.car_tree = None
        # self.reservation_tree = None
        self.root = root
        self.root.title("Car Rental System")
        self.root.geometry("1000x600")  # Adjust the size as needed
        self.id = int(sys.argv[1])
        self.create_menu_bar()
        self.create_main_frame()
        self.cars = {}
        self.location = {}
        self.insurance = {}
        self.discount = {}

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

        # Car Menu
        car_menu = tk.Menu(self.menu_bar, tearoff=0)
        car_menu.add_command(label="View Cars", command=self.show_cars)
        self.menu_bar.add_cascade(label="Cars", menu=car_menu)

        # Insurance Menu
        insurance_menu = tk.Menu(self.menu_bar, tearoff=0)
        insurance_menu.add_command(label="View Insurances", command=self.show_insurances)
        self.menu_bar.add_cascade(label="Insurances", menu=insurance_menu)

        # Discounts Menu
        discounts_menu = tk.Menu(self.menu_bar, tearoff=0)
        discounts_menu.add_command(label="View Discounts", command=self.show_discounts)
        self.menu_bar.add_cascade(label="Discounts", menu=discounts_menu)

        # Location Menu
        location_menu = tk.Menu(self.menu_bar, tearoff=0)
        location_menu.add_command(label="View Locations", command=self.show_locations)
        self.menu_bar.add_cascade(label="Locations", menu=location_menu)

        # Payments Menu
        payments_menu = tk.Menu(self.menu_bar, tearoff=0)
        payments_menu.add_command(label="Show Payments", command=self.show_payment)
        self.menu_bar.add_cascade(label="Payment", menu=payments_menu)

        # Profile
        profile_menu = tk.Menu(self.menu_bar, tearoff=0)
        profile_menu.add_command(label="View Information", command=self.show_information)
        self.menu_bar.add_cascade(label="Profile", menu=profile_menu)

    def create_main_frame(self):
        style = ttk.Style()
        style.configure("TFrame", background="SpringGreen2")
        self.main_frame = ttk.Frame(self.root, style="TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True)


    # Placeholder methods for menu commands
    def show_reservations(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.reservation_tree = ttk.Treeview(self.main_frame, columns=("Registration ID", "Car", "Insurance", "Discount","Pick Up Location","Pick Up Time","Drop Off Location","Drop Off Time", "TotalCost"),
                                             show='headings')
        self.reservation_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.reservation_tree["columns"]:
            self.reservation_tree.heading(col, text=col)

        # Fetch data from backend and populate the tree
        self.populate_reservations()

        # Add a button for car reservation
        tk.Button(self.main_frame, text="Edit Reservation", command=self.edit_reservation).pack(side=tk.LEFT)
        tk.Button(self.main_frame, text="Delete Reservation", command=self.delete_reservation).pack(side=tk.RIGHT)
        tk.Button(self.main_frame, text="Make Payment", command=self.make_payment).pack(side=tk.LEFT)   

    # Data doesn't show up in correct format (Malav)
    def populate_reservations(self):
        # Clear existing data in the tree
        for i in self.reservation_tree.get_children():
            self.reservation_tree.delete(i)

        

        # Fetch data from backend and populate the tree
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual database connection details
        # Changes by Malav
        reservations = read_operations.fetch_reservation_by_id(connection, self.id)
        db_connection.close_db_connection(connection)  # Close the database connection after fetching data

        for res in reservations:
            # Assuming each reservation is a tuple in the format (id, customer_id, car_id, pickup_time, dropoff_time, ...)
            item_id = self.reservation_tree.insert("", tk.END, values=res)
            self.reservation_tree.tag_configure("red_text", background="SpringGreen2")
            self.reservation_tree.item(item_id, tags=("red_text",))
        
        # tk.Button(self.main_frame, text="Make Payment", command=self.make_payment).pack(side=tk.LEFT)   

    def populate_options(self, table):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details
        if table == 'Cars':
            cars = read_operations.fetch_car_names(connection)
            keys = []
            for car in cars:
                self.cars[car[1]] = car[0]
                self.cars[car[0]] = car[1]
                for key in self.cars.keys():
                    if not isinstance(key, int):
                        keys.append(key)
            return keys
        
        elif table == "Insurance":
            insurances = read_operations.fetch_insurance_names(connection)
            keys = []
            for insurance in insurances:
                self.insurance[insurance[1]] = insurance[0]
                self.insurance[insurance[0]] = insurance[1]
            for key in self.insurance.keys():
                if not isinstance(key, int):
                    keys.append(key)
            return keys
        
        elif table == "Discount":
            discounts = read_operations.fetch_discount_names(connection)
            keys = []
            for discount in discounts:
                self.discount[discount[1]] = discount[0]
                self.discount[discount[0]] = discount[1]
            for key in self.discount.keys():
                if not isinstance(key, int):
                    keys.append(key)
            return keys
        
        elif table == "Location":
            locations = read_operations.fetch_location_names(connection)
            keys = []
            for location in locations:
                self.location[location[1]] = location[0]
                self.location[location[0]] = location[1]
            for key in self.location.keys():
                if not isinstance(key, int):
                    keys.append(key)
            return keys

    def add_reservation(self):
         # Open a new window for reservation details
        add_res_win = tk.Toplevel(self.root)
        add_res_win.title("Add Reservation")

        # Customer ID
        tk.Label(add_res_win, text="Customer ID").grid(row=0, column=0)
        tk.Label(add_res_win, text=self.id).grid(row=0, column=1)

        # Car ID
        tk.Label(add_res_win, text="Car").grid(row=1, column=0)
        car_options = self.populate_options("Cars")
        car_id_var = tk.StringVar(value=car_options[0] if car_options else "")
        car_id_dropdown = tk.OptionMenu(add_res_win, car_id_var, *car_options)
        car_id_dropdown.grid(row=1, column=1)
        # car_id_entry = tk.Entry(add_res_win)
        # car_id_entry.grid(row=1, column=1)

        # Insurance ID
        tk.Label(add_res_win, text="Insurance").grid(row=2, column=0)
        insurance_options = self.populate_options("Insurance")
        ins_id_var = tk.StringVar(value=insurance_options[0] if insurance_options else "")
        ins_id_dropdown = tk.OptionMenu(add_res_win, ins_id_var, *insurance_options)
        ins_id_dropdown.grid(row=2, column=1)
        # insurance_id_entry = tk.Entry(add_res_win)
        # insurance_id_entry.grid(row=2, column=1)

        # Discount ID
        tk.Label(add_res_win, text="Discount").grid(row=3, column=0)
        discount_options = self.populate_options("Discount")
        discount_id_var = tk.StringVar(value=discount_options[0] if discount_options else "")
        discount_id_dropdown = tk.OptionMenu(add_res_win, discount_id_var, *discount_options)
        discount_id_dropdown.grid(row=3, column=1)
        # discount_id_entry = tk.Entry(add_res_win)
        # discount_id_entry.grid(row=3, column=1)

        # Pick Up Location
        tk.Label(add_res_win, text="Pick Up Location").grid(row=4, column=0)
        pLocation_options = self.populate_options("Location")
        pLocation_id_var = tk.StringVar(value=pLocation_options[0] if pLocation_options else "")
        pLocation_id_dropdown = tk.OptionMenu(add_res_win, pLocation_id_var, *pLocation_options)
        pLocation_id_dropdown.grid(row=4, column=1)

        # pickup_location_entry = tk.Entry(add_res_win)
        # pickup_location_entry.grid(row=4, column=1)

        # Drop Off Location
        tk.Label(add_res_win, text="Drop Off Location").grid(row=5, column=0)
        dLocation_options = self.populate_options("Location")
        dLocation_id_var = tk.StringVar(value=dLocation_options[0] if dLocation_options else "")
        dLocation_id_dropdown = tk.OptionMenu(add_res_win, dLocation_id_var, *dLocation_options)
        dLocation_id_dropdown.grid(row=5, column=1)

        # dropoff_location_entry = tk.Entry(add_res_win)
        # dropoff_location_entry.grid(row=5, column=1)

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
                                      add_res_win,
                                      self.id,
                                      self.cars[car_id_var.get()],
                                      self.insurance[ins_id_var.get()],
                                      self.discount[discount_id_var.get()],
                                      self.location[pLocation_id_var.get()],
                                      self.location[dLocation_id_var.get()],
                                      pickup_time_entry.get(),
                                      dropoff_time_entry.get()
                                  ))
        submit_button.grid(row=8, column=1)

    def submit_new_reservation(self, add_res_win, customer_id, car_id, insurance_id, discount_id, pickup_location, dropoff_location,
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
            self.populate_reservations()
        except Exception as e:
            print(f"Error adding reservation: {e}")
        finally:
            db_connection.close_db_connection(connection)
        add_res_win.destroy()

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
        pLocation_options = self.populate_options("Location")
        pLocation_id_var = tk.StringVar(value=(reservation_details[4]) if pLocation_options else "")
        pLocation_id_dropdown = tk.OptionMenu(edit_res_win, pLocation_id_var, *pLocation_options)
        pLocation_id_dropdown.grid(row=4, column=1)

        # Drop Off Location
        tk.Label(edit_res_win, text="Drop Off Location").grid(row=5, column=0)
        dLocation_options = self.populate_options("Location")
        dLocation_id_var = tk.StringVar(value=(reservation_details[6]) if dLocation_options else "")
        dLocation_id_dropdown = tk.OptionMenu(edit_res_win, dLocation_id_var, *dLocation_options)
        dLocation_id_dropdown.grid(row=5, column=1)

        # Pick Up Time
        tk.Label(edit_res_win, text="Pick Up Time").grid(row=6, column=0)
        pickup_time_entry = tk.Entry(edit_res_win)
        pickup_time_entry.grid(row=6, column=1)
        pickup_time_entry.insert(0, reservation_details[5])  # Pre-fill with selected reservation's pick up time

        # Drop Off Time
        tk.Label(edit_res_win, text="Drop Off Time").grid(row=7, column=0)
        dropoff_time_entry = tk.Entry(edit_res_win)
        dropoff_time_entry.grid(row=7, column=1)
        dropoff_time_entry.insert(0, reservation_details[7])  # Pre-fill with selected reservation's drop off time

        # Submit Button
        submit_button = tk.Button(edit_res_win, text="Submit",
                                    command=lambda: self.submit_edited_reservation(
                                        edit_res_win,
                                        self.location[pLocation_id_var.get().split(", ")[0]],
                                        self.location[dLocation_id_var.get().split(", ")[0]],
                                        pickup_time_entry.get(),
                                        dropoff_time_entry.get()
                                    ))
        
        submit_button.grid(row=8, column=1)

    def submit_edited_reservation(self, edit_res_win, pickup_location, dropoff_location,
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
        edit_res_win.destroy()

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


    def show_cars(self):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.car_tree = ttk.Treeview(self.main_frame, columns=("Car Brand", "Car Model", "Car Type","Car Fixed Cost"),
                                     show='headings')
        self.car_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.car_tree["columns"]:
            self.car_tree.heading(col, text=col)

        # Fetch car data from the backend and populate the tree
        self.populate_cars()

    def populate_cars(self):
        # Clear existing data in the tree
        for i in self.car_tree.get_children():
            self.car_tree.delete(i)

        # Open database connection
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        # Fetch car data from backend
        try:
            cars = get_all_available_cars(connection)
            for car in cars:
                self.car_tree.insert("", tk.END, values=car)
                # Assuming the car data is returned as a tuple or list in the order of columns
                # item_id = self.car_tree.insert("", tk.END, values=car)
                # self.car_tree.tag_configure("red_text", background="SpringGreen2")
                # self.car_tree.item(item_id, tags=("red_text",))
        except Exception as e:
            print(f"Error fetching cars: {e}")
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
                self.location_tree.tag_configure("red_text", background="SpringGreen2")
                self.location_tree.item(item_id, tags=("red_text",))

        except Exception as e:
            print(f"Error fetching locations: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def show_insurances(self):
        # Open a new window for managing insurances
        ins_win = tk.Toplevel(self.root)
        ins_win.title("Insurances")

        # Treeview to display insurances
        self.insurance_tree = ttk.Treeview(ins_win, columns=("Insurance ID", "Company", "Type", "Cost"),
                                           show='headings')
        self.insurance_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.insurance_tree["columns"]:
            self.insurance_tree.heading(col, text=col)

        # Fetch insurance data from the backend and populate the tree
        self.populate_insurances()

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
                self.insurance_tree.insert("", tk.END, values=(
                    ins[0], ins[1], ins[2], ins[3]))  # Adjust indices based on your database structure

        except Exception as e:
            print(f"Error fetching insurances: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def show_discounts(self):
        # Open a new window for managing discounts
        self.discount_win = tk.Toplevel(self.root)
        self.discount_win.title("Discounts")

        # Treeview to display discounts
        self.discount_tree = ttk.Treeview(self.discount_win, columns=("Discount ID", "Name", "Validity", "Percentage"),
                                          show='headings')
        self.discount_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.discount_tree["columns"]:
            self.discount_tree.heading(col, text=col)

        # Fetch discount data from the backend and populate the tree
        self.populate_discounts()

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
                self.discount_tree.tag_configure("red_text", background="SpringGreen2")
                self.discount_tree.item(item_id, tags=("red_text",))

        except Exception as e:
            print(f"Error fetching discounts: {e}")
        finally:
            db_connection.close_db_connection(connection)

    def show_payment(self):
        # Open a new window for managing discounts
        self.payment_win = tk.Toplevel(self.root)
        self.payment_win.title("Payments")
 
        # Treeview to display discounts
        self.payment_tree = ttk.Treeview(self.payment_win, columns=("Payment Type", "Tranaction ID", "Amount", "Status", "Payment Time", "Reservation ID"),
                                          show='headings')
        self.payment_tree.pack(fill=tk.BOTH, expand=True)
 
        # Define column headings
        for col in self.payment_tree["columns"]:
            self.payment_tree.heading(col, text=col)
 
        # Fetch discount data from the backend and populate the tree
        self.populate_payments()
 
    def populate_payments(self):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with your actual details
 
        try:
            # Fetch discount data from the database
            payments = read_operations.fetch_payment_by_id(connection, self.id)
 
            # Clear existing data in the tree
            for i in self.payment_tree.get_children():
                self.payment_tree.delete(i)
 
            # Populate the tree with discount data
            for payment in payments:
                item_id = self.payment_tree.insert("", tk.END, values=(
                    payment[0], payment[1], payment[2], payment[3], payment[4], payment[5]))  # Adjust indices based on your database structure
                self.payment_tree.tag_configure("red_text", background="SpringGreen2")
                self.payment_tree.item(item_id, tags=("red_text",))
 
        except Exception as e:
            print(f"Error fetching payments: {e}")
        finally:
            db_connection.close_db_connection(connection)


    def make_payment(self):
        selected_item = self.reservation_tree.focus()
        if not selected_item:
            messagebox.showerror("Error", "No reservation selected")
            return
        # Open a form similar to add_reservation, but pre-fill with selected reservation details
        reservation_details = self.reservation_tree.item(selected_item, "values")
        make_payment_win = tk.Toplevel(self.root)
        make_payment_win.title("Make Payment")

        # 
        tk.Label(make_payment_win, text="Payment Type").grid(row=4, column=0)
        payment_type_entry = tk.Entry(make_payment_win)
        payment_type_entry.grid(row=4, column=1)

        

        reservation_id = reservation_details[0]
        total_cost = reservation_details[11]

        # Submit Button
        submit_button = tk.Button(make_payment_win, text="Submit",
                                    command=lambda: self.submit_payment(
                                        payment_type_entry.get(),reservation_id,total_cost
                                
                                    ))
        submit_button.grid(row=8, column=1)

    def submit_payment(self, payment_type, reservation_id,total_cost):
        
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        
        create_new_payment(connection,payment_type,total_cost,reservation_id)
        print("New payment added successfully.")
        
        db_connection.close_db_connection(connection)
    
    def show_information(self):
        # Clear the main frame

        for widget in self.main_frame.winfo_children():
            widget.destroy()

        # Create a Treeview widget
        self.info_tree = ttk.Treeview(self.main_frame, columns=("Phone Number", "Email"), show='headings')
        self.info_tree.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.info_tree["columns"]:
            self.info_tree.heading(col, text=col)

        # Fetch data from backend and populate the tree
        self.populate_information()


    def populate_information(self):

        connection = db_connection.create_db_connection("host", "user", "password", "db_name")
        customer_info = read_operations.fetch_customer_info(connection, self.id)

        # Clear existing data in the tree
        for i in self.info_tree.get_children():
            self.info_tree.delete(i)

        # Populate the tree with discount data
        for info in customer_info:
            item_id = self.info_tree.insert("", tk.END, values=(
                info[0], info[1]))
            self.info_tree.tag_configure("red_text", background="SpringGreen2")
            self.info_tree.item(item_id, tags=("red_text",))

        tk.Button(self.main_frame, text="Edit Information", command=self.update_information).pack(side=tk.LEFT)

    


    def update_information(self):

        # Open a form similar to add_reservation, but pre-fill with selected reservation details
        customer_details = self.info_tree.item(self.info_tree.focus(), "values")
        update_res_win = tk.Toplevel(self.root)
        update_res_win.title("Edit Information")

        # Phone Number
        tk.Label(update_res_win, text="Phone Number").grid(row=1, column=0)
        phone_entry = tk.Entry(update_res_win)
        phone_entry.grid(row=1, column=1)
        phone_entry.insert(0, customer_details[0])

        # Email
        tk.Label(update_res_win, text="Email").grid(row=2, column=0)
        email_entry = tk.Entry(update_res_win)
        email_entry.grid(row=2, column=1)
        email_entry.insert(0, customer_details[1])

        # Submit Button
        submit_button = tk.Button(update_res_win, text="Submit",
                                    command=lambda: self.submit_updated_information(
                                        update_res_win, phone_entry.get(), email_entry.get()
                                    ))
        
        submit_button.grid(row=4, column=1)
        
    def submit_updated_information(self, update_res_win, phone, email):
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")  # Replace with actual details

        updated_information = (phone, email)
        person_id = read_operations.fetch_person_id(connection, self.id)[0][0]
        try:
            update_customer_information(connection, person_id, *updated_information)
            print("Information updated")
            
            self.show_information() 
        except Exception as e:
            print(f"Error updating information: {e}")
        finally:
            db_connection.close_db_connection(connection)
        update_res_win.destroy()

def main():
    root = tk.Tk()
    app = CarRentalApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
