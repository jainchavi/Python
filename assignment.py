#NAME: CHAVI JAIN
#BATCH : 3
#JECRC UNIVERSITY




#ASSIGNMENT 1
# BANKING CONTROL PANEL:
user_accounts = {
    "user 1": {"balance": 1000, "pin": "1234"},
    "user 2": {"balance": 500, "pin": "5678"}
   
}

# Welcome message
print("Welcome to Simple Bank Console Server")

# Main program logic
is_logged_in = False
current_user = ""

while True:
    if not is_logged_in:
        # Login process
        username = input("Enter username (or 'exit' to quit): ")
        
        if username.lower() == "exit":
            print("Thank you for using Simple Bank Console Server. Goodbye!")
            break
            
        if username in user_accounts:
            pin = input("Enter your PIN: ")
            if pin == user_accounts[username]["pin"]:
                is_logged_in = True
                current_user = username
                print(f"Login successful. Welcome {current_user}!")
            else:
                print("Incorrect PIN. Please try again.")
        else:
            print("Username not found. Please try again.")
    
    else:
        # Display menu
        print("\n----- MENU -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer Money")
        print("5. Logout")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        # Check balance
        if choice == "1":
            print(f"Your current balance: ${user_accounts[current_user]['balance']}")
        
        # Deposit
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    user_accounts[current_user]["balance"] += amount
                    print(f"${amount} deposited successfully.")
                    print(f"New balance: ${user_accounts[current_user]['balance']}")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Withdraw
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0:
                    if amount <= user_accounts[current_user]["balance"]:
                        user_accounts[current_user]["balance"] -= amount
                        print(f"${amount} withdrawn successfully.")
                        print(f"New balance: ${user_accounts[current_user]['balance']}")
                    else:
                        print("Insufficient funds.")
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Transfer Money
        elif choice == "4":
            recipient = input("Enter recipient's username: ")
            if recipient in user_accounts and recipient != current_user:
                try:
                    amount = float(input(f"Enter amount to transfer to {recipient}: $"))
                    if amount > 0:
                        if amount <= user_accounts[current_user]["balance"]:
                            user_accounts[current_user]["balance"] -= amount
                            user_accounts[recipient]["balance"] += amount
                            print(f"Transfer successful!")
                            print(f"${amount} debited from your account.")
                            print(f"${amount} credited to {recipient}'s account.")
                            print(f"Your new balance: ${user_accounts[current_user]['balance']}")
                        else:
                            print("Insufficient funds for this transfer.")
                    else:
                        print("Please enter a positive amount.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif recipient == current_user:
                print("Cannot transfer money to yourself.")
            else:
                print("Recipient username not found.")
        
        # Logout
        elif choice == "5":
            is_logged_in = False
            print(f"Logged out successfully. Goodbye, {current_user}!")
            current_user = ""
        
        # Exit
        elif choice == "6":
            print(f"Logged out successfully. Goodbye, {current_user}!")
            print("Thank you for using Simple Bank Console Server.")
            break
        
        else:
            print("Invalid choice. Please try again.")



            

#Problem Statement: Car Rental System
#Objective: Develop a simple car rental system using lists, tuples, dictionary, sets and loops in Python. The
#system allows customers to view avilable cars, rent a car, and check rental history.

#Features and Functionalities
#1) View Availabale Cars:
        #Display a list of cars available for rent.
        #Each car has a Car ID, Model Name, and Price Per Day
        #If a car is booked, it won't appear in the available cars list.

#2)Rent a Car:
        #Users enter a Car ID to rent a car
        #System asks for the rental duration(number of days).
        #System calculates and display the total price for the rental
        #Booked cars are stored, and their IDs are marked as unavailable.

#3)View Booked Cars:
        #Display the list of currently rented cars.
        #Show Customer Name, Car ID, Rental Days, and Total Price

#4)Return a Car:
        #User enters their name to return the rented car.
        #The car is removed from the active rentals list.
        #The system adds this booking to rental history.

#5)View Rental History(Invoice):
        #User enters theirs names to view past records.
        #Display Car ID, Rental Duration, and Total Cost as an invoice.

#6)Exit System:
        #Allows the users to safely exit the rental records.

        


available_cars = {
    101: ("Porsche", 4500),
    102: ("Hyundai", 1900),
    103: ("Ford F-Series", 1800),
    104: ("Honda CR-V", 1500)
}

rented_cars = []  
rental_history = {}  
users = {}  

# User Authentication System
while True:
    print("\nWelcome to Car Rental System")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Forgot Password")
    print("4. Exit")

    auth_choice = input("Choose an option: ").strip()

    if auth_choice == "1":  # Sign Up
        username = input("Enter a username: ").strip().lower()
        if username in users:
            print("Username already exists! Try another one.")
            continue
        password = input("Create a password: ").strip()
        users[username] = password
        print("Sign-up successful! Please sign in.")

    elif auth_choice == "2":  # Sign In
        username = input("Enter your username: ").strip().lower()
        password = input("Enter your password: ").strip()

        if username in users and users[username] == password:
            print("\nLogin successful! Welcome,", username)
            break  
        else:
            print("Invalid username or password. Try again.")

    elif auth_choice == "3":  # Forgot Password
        username = input("Enter your username: ").strip().lower()
        if username in users:
            new_password = input("Enter a new password: ").strip()
            users[username] = new_password
            print("Password reset successful! Please sign in.")
        else:
            print("Username not found!")

    elif auth_choice == "4":  # Exit
        print("Exiting the system.")
        exit()

    else:
        print("Invalid choice! Please try again.")

# Car Rental System Loop (After Login)
while True:
    print("\nCar Rental System")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. View Rented Cars")
    print("4. Return a Car")
    print("5. View Rental History")
    print("6. Logout & Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":  # View Available Cars
        print("\nAvailable Cars:")
        if not available_cars:
            print("No cars available!")
        else:
            for car_id, car_details in available_cars.items():
                print("{car_id} - {car_details[0]} - Rs{car_details[1]}/day")

    elif choice == "2":  # Rent a Car
        if not available_cars:
            print("\nNo cars available for rent!")
            continue

        print("\nAvailable Cars:")
        for car_id, car_details in available_cars.items():
            print("{car_id} - {car_details[0]} - Rs{car_details[1]}/day")

        car_id_input = input("\nEnter Car ID to rent: ").strip()
        if not car_id_input.isdigit():
            print("Invalid input! Please enter a valid car ID.")
            continue

        car_id = int(car_id_input)
        if car_id not in available_cars:
            print("Invalid Car ID or already rented!")
            continue

        days_input = input("Enter rental duration (days): ").strip()
        if not days_input.isdigit():
            print("Invalid input! Please enter a valid number of days.")
            continue

        days = int(days_input)
        if days <= 0:
            print("Rental duration must be at least 1 day.")
            continue

        car_details = available_cars.pop(car_id)  # Remove car from available list
        total_price = car_details[1] * days

        rented_cars.append((username, car_id, car_details[0], days, total_price))

        if username not in rental_history:
            rental_history[username] = []

        rental_history[username].append((car_id, days, total_price))

        print("\n{car_details[0]} rented successfully for Rs{total_price} ({days} days)!")

    elif choice == "3":  # View Rented Cars
        print("\nCurrently Rented Cars:")
        if not rented_cars:
            print("No cars are rented at the moment.")
        else:
            for rental in rented_cars:
                print("{rental[0]} - Car ID: {rental[1]} - {rental[2]} - {rental[3]} Days - Rs{rental[4]}")

    elif choice == "4":  # Return a Car (Using `for-else`)
        if not rented_cars:
            print("\nNo cars are rented currently!")
            continue

        for rental in rented_cars:
            if rental[0] == username:  # Check if the user has rented a car
                rented_cars.remove(rental)
                available_cars[rental[1]] = (rental[2], rental[4] // rental[3])
                print("\n{rental[2]} returned successfully!")
                break  # Exit the loop once the car is returned
        else:
            print("No rented car found under your name.")  # Runs if no match is found

    elif choice == "5":  # View Rental History
        if username in rental_history:
            print("\nRental History:")
            for rental in rental_history[username]:
                print(f"Car ID: {rental[0]} - {rental[1]} Days - Rs{rental[2]}")
        else:
            print("No rental history found!")

    elif choice == "6":  # Logout & Exit
        print("Logging out. Have a great day!")
        break

    else:
        print("Invalid choice! Please try again.")






#ASSIGNMENT 2
#CAR RENTAL SYSTEM USING FUNCTIONS 
available_cars = {
    101: ("Porsche", 4500),
    102: ("Hyundai", 1900),
    103: ("Ford F-Series", 1800),
    104: ("Honda CR-V", 1500)
}

rented_cars = []  
rental_history = {}  
users = {}

        
def sign_up():
        # Sign Up
        username = input("Enter a username: ").strip().lower()
        if username in users:
            print("Username already exists! Try another one.")
            return None
        password = input("Create a password: ").strip()
        users[username] = password
        print("Sign-up successful! Please sign in.")
        
def sign_in():
        # Sign In
        while True:
            
            username = input("Enter your username: ").strip().lower()
            password = input("Enter your password: ").strip()

            if username in users and users[username] == password:
                print("\nLogin successful! Welcome,", username)
                return username
                 
            else:
                print("Invalid username or password. Try again.")

def forgot_password():
        # Forgot Password
        username = input("Enter your username: ").strip().lower()
        if username in users:
            new_password = input("Enter a new password: ").strip()
            users[username] = new_password
            print("Password reset successful! Please sign in.")
        else:
            print("Username not found!")


    #choice = input("Choose an option: ").strip()

# View Available Cars
def available_car():
        print("\nAvailable Cars:")
        if not available_cars:
            print("No cars available!")
        else:
            for car_id, car_details in available_cars.items():
                print(f"{car_id} - {car_details[0]} - Rs{car_details[1]}/day")

# Rent a Car
def rent_car(username):
        if not available_cars:
            print("\nNo cars available for rent!")
            return None

        available_car()
        print("\nAvailable Cars:")

        car_id_input = input("\nEnter Car ID to rent: ").strip()
        if not car_id_input.isdigit():
            print("Invalid input! Please enter a valid car ID.")
            return None 

        car_id = int(car_id_input)
        if car_id not in available_cars:
            print("Invalid Car ID or already rented!")
            return None

        days_input = input("Enter rental duration (days): ").strip()
        if not days_input.isdigit():
            print("Invalid input! Please enter a valid number of days.")
            return None

        days = int(days_input)
        if days <= 0:
            print("Rental duration must be at least 1 day.")
            return None

        car_details = available_cars.pop(car_id)  # Remove car from available list
        total_price = car_details[1] * days

        rented_cars.append((username, car_id, car_details[0], days, total_price))

        if username not in rental_history:
            rental_history[username] = []

        rental_history[username].append((car_id, days, total_price))

        print(f"\n{car_details[0]} rented successfully for Rs{total_price} ({days} days)!")

# View Rented Cars
def view_rented_car():
        print("\nCurrently Rented Cars:")
        if not rented_cars:
            print("No cars are rented at the moment.")
        else:
            for rental in rented_cars:
                print(f"{rental[0]} - Car ID: {rental[1]} - {rental[2]} - {rental[3]} Days - Rs{rental[4]}")

# Return a Car (Using `for-else`)
def return_car(username):
        if not rented_cars:
            print("\nNo cars are rented currently!")
            return None

        for rental in rented_cars:
            if rental[0] == username:  # Check if the user has rented a car
                rented_cars.remove(rental)
                available_cars[rental[1]] = (rental[2], rental[4] // rental[3])
                print(f"\n{rental[2]} returned successfully!")
                break  # Exit the loop once the car is returned
        else:
            print("No rented car found under your name.")  # Runs if no match is found

# View Rental History
def rentals_history(username):
        if username in rental_history:
            print("\nRental History:")
            for rental in rental_history[username]:
                print(f"Car ID: {rental[0]} - {rental[1]} Days - ₹{rental[2]}")
        else:
            print("No rental history found!")




# User Authentication System
while True:
    print("\nWelcome to Car Rental System")
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Forgot Password")
    print("4. Exit")


    auth_choice = input("Enter the choice you wnt to select:").strip()
    if auth_choice == "1":
        sign_up()
    elif auth_choice == "2":
        logged_in_user = sign_in()
        if logged_in_user:
            break  # Proceed to rental system after login
    elif auth_choice == "3":
        forgot_password()
    elif auth_choice == "4":
        print("Exiting the system.")
        exit()
    else:
        print("Invalid choice! Please try again.")

# Car Rental System Loop (After Login)
while True:
        
    print("\nCar Rental System")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. View Rented Cars")
    print("4. Return a Car")
    print("5. View Rental History")
    print("6. Logout & Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        available_car()
    elif choice == "2":
        rent_car(logged_in_user)
    elif choice == "3":
        view_rented_car()
    elif choice == "4":
        return_car(logged_in_user)
    elif choice == "5":
        rentals_history(logged_in_user)
    elif choice == "6":
        print("Logging out. Have a great day!")
        break
    else:
        print("Invalid choice! Please try again.")

    


#ASSIGNMENT 3
#1) Hospital Appointment System
'''Objective:
Build a Hospital Appointment System where patients can:
-Register as a new patient
-Book an appointment with a doctor
-View available doctors
-Check appointment history
Requirements:
- Use a list of tuples to store doctor details (Doctor Name, Specialization).
- Use a dictionary to manage patient appointments.
- Implement functions for appointment booking, checking available doctors, and viewing
patient history.
- Use sets to track unique patient IDs.'''



doctors = [
    ("Dr. Aditya Soral","Orthopaedics"),
    ("Dr. Alok Mathur","Cardiologist"),
    ("Dr. Arpit Kalla","Physiotherapist"),
    ("Dr. Lokesh Jain","Gastroenterology"),
    ("Dr. Ashish Sharma","Pathology")
    ]

appointment = {}

track_patient = set()

def registered_patient():
    patient_id = input("Enter the ID:").strip()
    if patient_id in track_patient:
        print("Patient already registered")
    else:
        track_patient.add(patient_id)
        appointment[patient_id] = []
        print("Registered Successfully!")


def available_doctors():
    print("Available Doctors")
    for i in range(len(doctors)):
        print(f"{i+1} - {doctors[i][0]} - {doctors[i][1]}")

def book_appointment():
    patient_id = input("Enter the ID:").strip()
    if patient_id not in track_patient:
        print("Not registered! Please register.")
        return

    available_doctors()
    choice = input("Select Doctor by entering your preference:").strip()
    if choice.isdigit() and 1<=int(choice)<<len(doctors):
        doctor = doctors[int(choice) - 1]
        appointment[patient_id].append(doctor)
        print(f"Appointment successfully booked with {doctor[0]} ({doctor[1]})!")
    else:
        print("Invalid")

def appointment_history():
    patient_id = input("Enter the ID:").strip()
    if patient_id not in track_patient:
        print("Not registered! Please register.")
        return

    print("Your Appointment History:")
    history = appointment[patient_id]
    if history:
        for i in range(len(history)):
            print(f"{i+1} - {history[i][0]} - {history[i][1]}")
    else:
        print("No history found")
    
while True:
        
    print("\nHospital Appointment Syatem")
    print("1. Register as a new patient")
    print("2. View available doctors")
    print("3. Book an appointment with a doctor")
    print("4. Check appointment history")
    print("5. Exit")

    choice = input("Enter your choice:").strip()
    
    if choice == "1":
        registered_patient()
    elif choice == "2":
        available_doctors()
    elif choice == "3":
        book_appointment()
    elif choice == "4":
        appointment_history()
    elif choice == "5":
        print("Thank you for using the Hospital Appointment System!")
        break
    else:
        print("Invalid choice! Please try again.")


#2) Grocery Store Billing System
'''Objective:
Design a Grocery Store Billing System where users can:
- Add items to the cart
- Remove items from the cart
- View total bill
- Apply discount coupons
Requirements:
- Use a dictionary to store item prices.
- Use a list to maintain items in the cart.
- Implement functions for adding/removing items and calculating bills.
- Use lambda functions for discount calculations.'''


items = {
    "milk": 70,
    "cheese" : 50,
    "paneer": 80,
    "potatoes" :20,
    "onions" : 40,
    "oranges" :60,
    "grapes" : 90
    }

cart =[]

discount = lambda total, discount: total - (total*discount/100)

def add_item():
    item = input("Enter item:").strip().lower()
    if item in items:
        cart.append(item)
        print(f"{item} added to cart.")
    else:
        print("Item not present")


def remove_item():
    item = input("Enter item:").strip().lower()
    if item in cart:
        cart.remove(item)
        print(f"{item} removed from the cart.")
    else:
        print("Item not present")

def bill():
    if not cart:
        print("Cart Empty")
        return

    total = sum(items[item] for item in cart)
    print("Your Cart:")
    for item in set(cart):
        print(f"{item} x {cart.count(item)} - Rs{items[item]*cart.count(item)}")

    print(f"Total Bill: Rs{total}")

    disc_code = input("Enter discount code ").strip().lower()
    discounts = {"save 10":10, "save 20": 20}


    if disc_code in discounts:
        total = discount(total, discounts[disc_code])
        print(f"Discount Applied: {discounts[disc_code]}%")
        print(f"Final Bill: Rs{total}")
    else:
        print("Code Invalid")

while True:
    print("Grocery Store Billing System")
    print("1. Add Item to Cart")
    print("2. Remove Item from Cart")
    print("3. View Total Bill")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        bill()
    elif choice == "4":
        print("Thank you for shopping!")
        break
    else:
        print("Invalid choice! Try again.")


#3) Online Movie Ticket Booking System
'''Objective:
Develop an Online Movie Ticket Booking System where users can:
- View available movies
- Book tickets
- Cancel tickets
- Check booking history
Requirements:
- Use a list of tuples to store movie details (Movie Name, Show Timing).
- Use a dictionary to manage ticket bookings.
- Implement functions for booking, cancellation, and history tracking.
- Use sets to maintain unique seat numbers.'''



movie_details = [
    ("Chaava", "2:00 P.M"),
    ("Mrs.", "5:00 PM"),
    ("Kal Ho Na Ho", "6:30 PM"),
    ("Rockstar", "10:45 AM"),
    ("Laila Majnu", "7:35 PM"),
    ]

ticket_booking = {}
seat_number = set()

def available_movies():
    print("Available Movies")
    for i in range(len(movie_details)):
        print(f"{i+1} - {movie_details[i][0]} - {movie_details[i][1]}")

def booking(username):
    available_movies()
    choice = input("\nEnter movie number to book: ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(movie_details)):
        print("Invalid choice!")
        return
    
    movie_index = int(choice) - 1
    seat_no = input("Enter seat number: ").strip()

    if seat_no in seat_number:
        print("Seat already booked! Choose another.")
        return

    seat_number.add(seat_no)
    if username not in ticket_booking:
        ticket_booking[username] = []

    ticket_booking[username].append((movie_details[movie_index][0], movie_details[movie_index][1], seat_no))
    print(f"Ticket booked successfully for {movie_details[movie_index][0]} at {movie_details[movie_index][1]}, Seat No: {seat_no}")
        
def cancel_booking(username):
    if username not in ticket_booking or not ticket_booking[username]:
        print("No bookings found!")
        return

    print("Your Bookings:")
    for i in range(len(ticket_booking[username])):  
        print(f"{i + 1}. {ticket_booking[username][i][0]} - {ticket_booking[username][i][1]} - Seat No: {ticket_booking[username][i][2]}")

    choice = input("Enter booking number to cancel: ").strip()
    
    if not choice.isdigit() or not (1 <= int(choice) <= len(ticket_booking[username])):
        print("Invalid choice!")
        return

    canceled_booking = ticket_booking[username].pop(int(choice) - 1)
    seat_number.remove(canceled_booking[2])
    print(f"Booking canceled for {canceled_booking[0]} at {canceled_booking[1]}, Seat No: {canceled_booking[2]}")


def view_booking_history(username):
    if username not in ticket_booking or not ticket_booking[username]:
        print("No bookings found!")
    else:
        print("Your Booking History:")
        for ticket in ticket_booking[username]:
            print(f"{ticket[0]} - {ticket[1]} - Seat No: {ticket[2]}")


username = input("Enter your name: ").strip().lower()

    
     
while True:
    print("Online Movie Ticket Booking System")
    print("1. View available movies")
    print("2. Book tickets")
    print("3. Cancel tickets")
    print("4. Check booking history")
    print("5. Exit")

    choice = input("Choose an otion: ").strip()

    if choice == "1":
        available_movies()
    elif choice == "2":
        booking(username)
    elif choice == "3":
        cancel_booking(username)
    elif choice == "4":
        view_booking_history(username)
    elif choice == "5":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Try again.")




#4) Flight Reservation System
'''Objective:
Create a Flight Reservation System where users can:
- Search available flights
- Book a flight ticket
- Cancel a booking
- View flight details
Requirements:
- Use a list of dictionaries to store flight details (Flight No, Destination, Price).
- Use a dictionary to manage passenger bookings.
- Implement functions for searching flights, booking, and cancellation.
- Use lambda functions to filter flights based on price.'''
    


          

    
flights = [
    {"Flight No": "101", "Destination": "New York", "Price": 50000},
    {"Flight No": "202", "Destination": "London", "Price": 45000},
    {"Flight No": "303", "Destination": "Dubai", "Price": 30000},
    {"Flight No": "404", "Destination": "Singapore", "Price": 35000}
]


bookings = {}

def search_flights():
    print("Available Flights:")
    for i in range(len(flights)):  
        print(f"{i + 1}. {flights[i]['Flight No']} - {flights[i]['Destination']} - ₹{flights[i]['Price']}")

def filter_flights_by_price():
    max_price = input("Enter maximum budget (₹): ").strip()

    if not max_price.isdigit():
        print("Invalid input! Please enter a valid number.")
        return
    
    max_price = int(max_price)
    filtered_flights = list(filter(lambda flight: flight["Price"] <= max_price, flights))

    if filtered_flights:
        print("Flights within your budget:")
        for flight in filtered_flights:
            print(f"{flight['Flight No']} - {flight['Destination']} - ₹{flight['Price']}")
    else:
        print("No flights found within this budget.")

def book_ticket(username):
    search_flights()
    choice = input("\nEnter flight number to book: ").strip()

    for flight in flights:
        if flight["Flight No"] == choice:
            if username not in bookings:
                bookings[username] = []
            bookings[username].append((flight["Flight No"], flight["Destination"], flight["Price"]))
            print(f"Flight {flight['Flight No']} to {flight['Destination']} booked successfully for ₹{flight['Price']}!")
            return

    print("Invalid Flight Number!")

def cancel_ticket(username):
    if username not in bookings or not bookings[username]:
        print("\nNo bookings found!")
        return

    print("nYour Bookings:")
    for i in range(len(bookings[username])):  
        print(f"{i + 1}. {bookings[username][i][0]} - {bookings[username][i][1]} - ₹{bookings[username][i][2]}")

    choice = input("Enter booking number to cancel: ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(bookings[username])):
        print("Invalid choice!")
        return

    canceled_booking = bookings[username].pop(int(choice) - 1)
    print(f"Booking for {canceled_booking[0]} to {canceled_booking[1]} canceled successfully!")

def view_booking_history(username):
    if username not in bookings or not bookings[username]:
        print("No bookings found!")
    else:
        print("Your Booking History:")
        for booking in bookings[username]:
            print(f"{booking[0]} - {booking[1]} - ₹{booking[2]}")


username = input("Enter your name: ").strip().lower()

while True:
    print("Flight Reservation System")
    print("1. Search Available Flights")
    print("2. Filter Flights by Price")
    print("3. Book a Flight Ticket")
    print("4. Cancel a Booking")
    print("5. View Booking History")
    print("6. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        search_flights()
    elif choice == "2":
        filter_flights_by_price()
    elif choice == "3":
        book_ticket(username)
    elif choice == "4":
        cancel_ticket(username)
    elif choice == "5":
        view_booking_history(username)
    elif choice == "6":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice! Try again.")
    
