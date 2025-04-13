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



initialize_files()

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

    
