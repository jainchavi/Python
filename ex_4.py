#Factorial
'''n = int(input("Enter a number"))
fact = 1
for i in range(1,n+1):
        fact *= i
print("factorial =", fact)'''


#Continue Statement
'''for i in range(1,20):
    if i%5 == 0:
        continue
    else:
        print(i)'''

# Break Statement
'''for i in range(1,20):
        a = int(input("Enter a"))
        b = int(input("Enter b"))

        if b==0:
                 print("Error")
                 break
        else:
            c = a//b
            print("Quotient :", c)'''

#Store squares of first 10 natural nos. in list

'''squares = []
for x in range(1,10):
        squares.append(x**2)
print(squares)'''


#Create a Customer info for E-commerce website with id, name, email id, order history
#per order history maintain order id, item purchased, and price of item.

'''cus_id = 101
cus_name = "Chavi"
cus_email = "jainchavi@gmail.com"

order_history = []
order_history.append({"Order_id" : 1, "item_name" : "Oranges", "item_price" : 100})
order_history.append({"Order_id" : 2, "item_name" : "Grapes", "item_price" : 250})
order_history.append({"Order_id" : 3, "item_name" : "Mango", "item_price" : 80})

print(f"Customer ID : {cus_id}, Name :{cus_name}, Email :{cus_email}")
print("Order History:")
for order in order_history:
    print(f"Order ID: {order['Order_id']}, Item: {order['item_name']}, Price: {order['item_price']}")'''


#Student Grade Management(Using List and Loops)
#Objective: Store and manage student grades using a list.
#Problem Statement: Write a Python program that allows the user to enter grades for 5 students. Store these grades in a
#list and perform the following operations:
#1.Display all Grades.
#2.Find and print the highest and lower grades.
#3.Calculate and print the average grade.



'''print("Display Grades Of Students")
student_grade = []
for i in range(5):
        grade = float(input("Enter the grade of student"))
        student_grade.append(grade)
print("All grades", student_grade)
print("Maximum Grades",max(student_grade))
print("Minimum Grades", min(student_grade))
average = sum(student_grade)/len(student_grade)
print("Average Grade", average)'''



#Store and Retrieve Employee Data (Using Tuples)
#Objective: store fixed employee details using tuples
#Problem Statement: write python program that stores Employee id, Name and Salary for 3 emplyees using tuples.Allow the
#user to enter an employee id and retrieve their details.

'''employees = ((101, "Yash", 10000),
             (102, "Chavi", 20000),
             (103, "Divyam", 30000))

emp_id = int(input("Enter the employee id:"))
for emp in employees:
        if emp[0]==emp_id:
                print(f"Employee Id:{emp[0]}, Name:{emp[1]}, Salary:{emp[2]}")
                break
else:
        print("Employee not found")'''


#Library Book Management(Using Dictionary)
#Objective: Manage books in a library using a dictionary
#Problem Statement: write a python program that allows a library to store book info(book id as key and Book Title
#as a value). The program should:
#1. Allow the user to add new books.
#2. Allow the user to search for a book by its ID.
#3. Display all available books


'''book_info = {101:"IKIGAI", 102:"Atomic Habits", 103:"The Power of Habit", 104:"Mindset", 105:"Flamingo"}

book_id = int(input("Enter the book id:"))
if book_id in book_info:
        print(f"Book ID: {book_id}, Book Name: {book_info[book_id]}")
else:
    print("Book not found!")

n = int(input("Enter the value of n:"))
for i in range(n):
    new_book_id = int(input("Enter the new book ID: "))
    new_book_name = input("Enter the new book name: ")
    book_info[new_book_id] = new_book_name

print("Available Books", book_info)'''


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
