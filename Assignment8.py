#NAME: CHAVI JAIN
#BATCH : 3
#JECRC UNIVERSITY




#Problem Statement 1: Event Scheduler
'''Create a Python program using Object-Oriented Programming (OOP) to manage events. Each event
should have a name, date, and time. Use the datetime module to handle date and time operations.
Implement the following functionalities:
1. Add an event.
2. Remove an event.
3. Display all events in chronological order.
4. Save events to a file using the pickle module.
5. Load events from a file using the pickle module.'''


import pickle
from datetime import datetime

class Event:
    def _init_(self, name, date, time):
        self.name = name
        self.datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

class EventScheduler:
    def _init_(self):
        self.events = []
    
    def add_event(self, name, date, time):
        event = Event(name, date, time)
        self.events.append(event)
        self.events.sort(key=lambda e: e.datetime)
    
    def remove_event(self, name):
        self.events = [event for event in self.events if event.name != name]
    
    def display_events(self):
        if not self.events:
            print("No events scheduled.")
        else:
            for event in self.events:
                print(f"{event.name} - {event.datetime.strftime('%Y-%m-%d %H:%M')}")
    
    def save_events(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.events, file)
    
    def load_events(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.events = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.events = []

scheduler = EventScheduler()
scheduler.load_events("events.pkl")

while True:
    print("\nEvent Scheduler:")
    print("1. Add Event")
    print("2. Remove Event")
    print("3. Display Events")
    print("4. Save Events")
    print("5. Load Events")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter event name: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        time = input("Enter event time (HH:MM): ")
        scheduler.add_event(name, date, time)
    elif choice == "2":
        name = input("Enter event name to remove: ")
        scheduler.remove_event(name)
    elif choice == "3":
        scheduler.display_events()
    elif choice == "4":
        scheduler.save_events("events.pkl")
    elif choice == "5":
        scheduler.load_events("events.pkl")
    elif choice == "6":
        break
    else:
        print("Invalid choice, please try again.")

#2) Advanced Password Manager
'''Create a password manager using OOP. Each password entry should have attributes
like website, username, password, and last updated date (use datetime). Implement the following
functionalities:
1. Add a password entry (handle exceptions for invalid inputs).
2. Use regex to validate password strength.
3. Use a generator to yield passwords that were last updated more than 90 days ago.
4. Save password entries to a file using pickle (handle file-related exceptions).
5. Load password entries from a file using pickle (handle file-related exceptions).
6. Create a custom module password_utils.py to handle password validation and encryption.
7. Handle exceptions for invalid file operations. '''


import pickle
from datetime import datetime, timedelta
from password_utils import encrypt_password, decrypt_password, is_valid_password

class PasswordManager:
    def _init_(self):
        self.entries = []
    
    def add_entry(self, website, username, password):
        if not is_valid_password(password):
            print("Weak password!")
            return
        self.entries.append({
            "website": website, "username": username,
            "password": encrypt_password(password), "last_updated": datetime.now()
        })
    
    def display_entries(self):
        for e in self.entries:
            print(f"{e['website']} | {e['username']} | {decrypt_password(e['password'])} | {e['last_updated'].date()}")
    
    def save_entries(self, filename="passwords.pkl"):
        with open(filename, 'wb') as file:
            pickle.dump(self.entries, file)
    
    def load_entries(self, filename="passwords.pkl"):
        try:
            with open(filename, 'rb') as file:
                self.entries = pickle.load(file)
        except (FileNotFoundError, EOFError):
            self.entries = []
    
    def expired_passwords(self, days=90):
        return [e for e in self.entries if e['last_updated'] < datetime.now() - timedelta(days=days)]

manager = PasswordManager()
manager.load_entries()

while True:
    choice = input("1:Add 2:Show 3:Save 4:Load 5:Expired 6:Exit > ")
    if choice == "1":
        manager.add_entry(input("Website: "), input("Username: "), input("Password: "))
    elif choice == "2":
        manager.display_entries()
    elif choice == "3":
        manager.save_entries()
    elif choice == "4":
        manager.load_entries()
    elif choice == "5":
        for e in manager.expired_passwords():
            print(f"{e['website']} | {e['username']} | Last Updated: {e['last_updated'].date()}")
    elif choice == "6":
        break


#code for module password_utils.py

import re

def is_valid_password(password):
    """Validates password strength using a regex limited to numbers and letters only."""
    pattern = r"^(?=.[A-Z])(?=.[a-z])(?=.*\d)[A-Za-z\d]{6,}$"
    return re.match(pattern, password) is not None

def encrypt_password(password):
    """Simple encryption: reverses the password string."""
    return password[::-1]

def decrypt_password(encrypted_password):
    """Simple decryption: reverses the encrypted password back."""
    return encrypted_password[::-1]



#3) Problem Statement : Advanced Travel Itinerary Planner
'''Create a Python program that plans travel itineraries. Each itinerary should have attributes
like itinerary ID, destination, start date (use datetime), and end date. Implement the following
functionalities:
1. Add an itinerary (handle exceptions for invalid dates).
2. Use regex to validate the format of the destination.
3. Use a generator to yield itineraries starting in the next 7 days.
4. Save itinerary data to a file using pickle (handle file-related exceptions).
5. Load itinerary data from a file using pickle (handle file-related exceptions).
6. Create a custom module travel_utils.py to handle itinerary planning logic.
7. Implement logic to handle overlapping itineraries.'''


import pickle
import re
from datetime import datetime, timedelta

class TravelPlanner:
    def _init_(self):
        self.itineraries = []

    def add_itinerary(self, itinerary_id, destination, start_date, end_date):
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            if start_date > end_date:
                raise ValueError("Start date must be before end date.")
            if not re.match(r'^[A-Za-z ]+$', destination):
                raise ValueError("Invalid destination format. Use only letters and spaces.")
            if self.has_overlap(start_date, end_date):
                raise ValueError("Itinerary overlaps with an existing one.")
            self.itineraries.append({
                "id": itinerary_id, "destination": destination,
                "start_date": start_date, "end_date": end_date
            })
        except ValueError as e:
            print(f"Error: {e}")

    def has_overlap(self, start_date, end_date):
        for it in self.itineraries:
            if (it['start_date'] <= end_date and it['end_date'] >= start_date):
                return True
        return False

    def save_itineraries(self, filename="itineraries.pkl"):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.itineraries, file)
        except Exception as e:
            print(f"Error saving file: {e}")

    def load_itineraries(self, filename="itineraries.pkl"):
        try:
            with open(filename, 'rb') as file:
                self.itineraries = pickle.load(file)

    
            for it in self.itineraries:
                if isinstance(it['start_date'], str):  
                    it['start_date'] = datetime.strptime(it['start_date'], "%Y-%m-%d")
                    it['end_date'] = datetime.strptime(it['end_date'], "%Y-%m-%d")
        except (FileNotFoundError, EOFError):
            self.itineraries = []
        except Exception as e:
            print(f"Error loading file: {e}")


    def upcoming_itineraries(self, days=7):
        now = datetime.now().date()
        future_threshold = now + timedelta(days=days)

        print(f"Checking for itineraries between {now} and {future_threshold}")

        upcoming = []
        for it in self.itineraries:
            print(f"Checking itinerary: {it['destination']} ({it['start_date'].date()} - {it['end_date'].date()})")
            if now <= it['start_date'].date() <= future_threshold:
                upcoming.append(it)
    
        return upcoming





planner = TravelPlanner()
planner.load_itineraries()

while True:

    choice = input("1:Add 2:Save 3:Load 4:Upcoming 5:Exit > ")

    if choice == "1":
        planner.add_itinerary(input("ID: "), input("Destination: "), input("Start Date (YYYY-MM-DD): "), input("End Date (YYYY-MM-DD): "))

    elif choice == "2":
        planner.save_itineraries()

    elif choice == "3":
        planner.load_itineraries()
        print("Loaded Itineraries:", planner.itineraries)

    elif choice == "4":
        upcoming = planner.upcoming_itineraries()
    
        if upcoming:  
            for it in upcoming:
                print(f"{it['id']} | {it['destination']} | {it['start_date'].date()} - {it['end_date'].date()}")
        else:
            print("No upcoming itineraries found.")


    elif choice == "5":
        break

#code for travel_utils.py

import re
from datetime import datetime

def is_valid_destination(destination):
    """Validates that the destination contains only letters and spaces."""
    return bool(re.match(r'^[A-Za-z ]+$', destination))

def has_overlap(itineraries, start_date, end_date):
    """Checks if a new itinerary overlaps with existing ones."""
    for it in itineraries:
        if it['start_date'] <= end_date and it['end_date'] >= start_date:
            return True
    return False


#4) Problem Statement: Goods Trading &amp; Tax Calculator
'''Create a Python program to manage goods trading between buyers and sellers. The program should
track purchases, sales, and calculate taxes like GST/VAT on sold goods. It should also analyze trading
patterns and handle inventory.

✅ Key Features &amp; Requirements:
1. OOP-based Design:
- Classes: Product, Trade, Inventory, Trader.
- Each Product should have a name, SKU (Stock Keeping Unit), price, and tax rate.
- Each Trade will have product details, buy/sell type, quantity, price, and date.
2. Inventory Management:
- Add products to the inventory.
- Track available stock levels after trades.
3. Trade Operations:
- Add buy and sell trades.
- Use regex to validate product names and SKUs (e.g., SKU-12345).
4. Tax Calculation:
- Apply GST/VAT on sold goods based on their tax rate.
- Calculate total sales, total tax, and net profit.
- Use datetime to handle trade dates for sales reports.
5. Profit Analysis:
- Calculate profits/losses on goods sold.
- Use a generator to yield trades with profit margins &gt;20%.
6. Custom Module trade_utils.py:
- Functions for tax calculation, profit analysis, and SKU validation.
7. File Handling with Pickle:
- Save inventory and trade history to a file.
- Load saved data on startup, handling file-related exceptions.
8. Exception Handling:
- Handle invalid product inputs, trade entries, or file errors.
- Raise custom exceptions for invalid SKUs or insufficient stock.

�� Example Flow:
1. User starts the program and loads inventory.
2. User adds products:
- Product: Laptop, SKU-12345, Price: $1000, Tax Rate: 18%
- Product: Phone, SKU-67890, Price: $600, Tax Rate: 12%
3. User records trades:
- BUY Laptop x10 on 2024-03-01
- SELL Laptop x5 @ $1200 on 2024-03-15
4. Program validates SKUs using regex.
5. Tax and profit are calculated:
- Sale Amount: $6000
- GST (18%): $1080
- Profit: $1000
6. Inventory updates: 5 Laptops remain.
7. All data is saved using pickle.'''

import pickle
import re
from datetime import datetime

class Product:
    def _init_(self, name, sku, price, tax_rate):
        if not re.match(r'^SKU-\d+$', sku):
            raise ValueError("Invalid SKU format. Use SKU-12345 format.")
        self.name = name
        self.sku = sku
        self.price = price
        self.tax_rate = tax_rate

class Trade:
    def _init_(self, product, trade_type, quantity, price, date):
        self.product = product
        self.trade_type = trade_type  # "BUY" or "SELL"
        self.quantity = quantity
        self.price = price
        self.date = datetime.strptime(date, "%Y-%m-%d")

class Inventory:
    def _init_(self):
        self.products = {}
        self.trades = []

    def add_product(self, name, sku, price, tax_rate):
        try:
            product = Product(name, sku, price, tax_rate)
            self.products[sku] = product
            print("Product added successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def add_trade(self, sku, trade_type, quantity, price, date):
        if sku not in self.products:
            print("Product not found in inventory.")
            return
        if trade_type == "SELL":
            available_stock = self.get_stock(sku)
            if quantity > available_stock:
                print("Insufficient stock!")
                return
        trade = Trade(self.products[sku], trade_type, quantity, price, date)
        self.trades.append(trade)
        print("Trade recorded successfully!")

    def get_stock(self, sku):
        stock = 0
        for trade in self.trades:
            if trade.product.sku == sku:
                stock += trade.quantity if trade.trade_type == "BUY" else -trade.quantity
        return stock

    def calculate_profit(self):
        total_sales, total_tax, total_profit = 0, 0, 0
        for trade in self.trades:
            if trade.trade_type == "SELL":
                tax = trade.price * trade.quantity * (trade.product.tax_rate / 100)
                profit = (trade.price - trade.product.price) * trade.quantity
                total_sales += trade.price * trade.quantity
                total_tax += tax
                total_profit += profit
        print(f"Total Sales: ${total_sales}\nTotal Tax: ${total_tax}\nTotal Profit: ${total_profit}")

    def save_data(self, filename="trading_data.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self, file)
        print("Data saved successfully!")

    @staticmethod
    def load_data(filename="trading_data.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return Inventory()

inventory = Inventory.load_data()

while True:
    print("\n1: Add Product\n2: Add Trade\n3: View Stock\n4: Calculate Profit\n5: Save & Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        inventory.add_product(
            input("Product Name: "),
            input("SKU: "),
            float(input("Price: ")),
            float(input("Tax Rate (%): "))
        )
    elif choice == "2":
        inventory.add_trade(
            input("SKU: "),
            input("Trade Type (BUY/SELL): "),
            int(input("Quantity: ")),
            float(input("Price: ")),
            input("Date (YYYY-MM-DD): ")
        )
    elif choice == "3":
        sku = input("Enter SKU to check stock: ")
        print(f"Stock for {sku}: {inventory.get_stock(sku)}")
    elif choice == "4":
        inventory.calculate_profit()
    elif choice == "5":
        inventory.save_data()
        break
    else:
        print("Invalid choice. Please try again.")
