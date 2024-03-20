import subprocess
import db_connection
import tkinter as tk
from tkinter import messagebox


def submit():
    
    username = username_entry.get()
    password = password_entry.get()
    user_role = "customers" if var.get() == 1 else "employee"
    result = authenticate_user(username, password, user_role)
    if result:
        user_id = result[0]
        if user_role == "employee":
            open_employee_gui()
        else:
            open_customer_gui(user_id)
    else:
        messagebox.showerror("Error", "Invalid username or password")


def authenticate_user(username, password, user_role):
    try:
        connection = db_connection.create_db_connection("host", "user", "password",
                                                        "db_name")
        cursor = connection.cursor()
        table_name = "Customers" if user_role == "customers" else "Employee"
        query = f"SELECT * FROM {table_name} WHERE UserName = %s AND Pass = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result
    except:
        return None
    

def open_customer_gui(user_id):
    subprocess.run(["python", "customer_gui.py", str(user_id)])
    root.destroy()  

def open_employee_gui():
    subprocess.run(["python", "employee_gui.py"])
    root.destroy()


 

# Main Tkinter window
root = tk.Tk()
root.title("User Type Selection")
root.configure(bg="lightblue")

# Variable to store the selected user type
var = tk.IntVar()

# Radio buttons for customer and employee
customer_radio = tk.Radiobutton(root, text="Customer", variable=var, value=1, bg="lightblue")
employee_radio = tk.Radiobutton(root, text="Employee", variable=var, value=2, bg="lightblue")

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit, bg="lightblue")

# Place widgets in the window
customer_radio.pack()
employee_radio.pack()

username_label = tk.Label(root, text="Username:", bg="lightblue")
username_entry = tk.Entry(root)
password_label = tk.Label(root, text="Password:", bg="lightblue")
password_entry = tk.Entry(root, show="*")

# Place widgets in the window
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
submit_button.pack()
# Run the Tkinter event loop
root.mainloop()

