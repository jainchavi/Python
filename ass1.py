'''import pickle
from datetime import datetime



class Event:

    def __init__(self):
        self.events = []

    def add_event(self, name, date, time):
        event_date = datetime. strptime(f"{date} {time}" , "%Y-%m-%d %H:%M")
        self.events.append((event_date, name))
        self.events.sort()

    def remove_event(self, name):
        self.events = [event for event in self.events if event[1] != name]

    def event_display(self):
        for event in self.events:
            print(event[1] , "-", event[0].strftime("%Y-%m-%d %H:%M"))

    def save_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.events, f)

    def load_file(self, filename):
        try:
            with open(filename, 'rb') as f:
                self.events = pickle.load(f)

        except FileNotFoundError:
            self.events = []


e1 = Event()

e1.add_event("Dancing", "2025-02-25" , "02:30")
e1.add_event("Singing", "2025-02-26" , "03:30")
e1.add_event("Acting", "2025-02-27" , "04:30")
e1.add_event("Painting", "2025-02-28" , "05:30")



e1.remove_event("Acting")


e1.event_display()


e1.save_file("events.pkl")
e1.load_file("events.pkl")'''

import re
import pickle
from datetime import datetime, timedelta

class AdvancedPasswordManager:

    def __init__(self):
        self.passwords = []


    def add_pass(self, website,username,password):
        if not self.validate_pass(password):
            raise ValueError("Password strength is weak")
        
        self.passwords.append({
            "website": website,
            "username": username,
            "password": password,
            "last_updated": datetime.now()
        })

    def validate_pass(self, password):
        return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password))

    def outdated_pass(self):
        for i in self.passwords:
            if datetime.now() - i["last_updated"] > timedelta(days=90):
                yield i


    def save_file(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self.passwords, f)
        except Exception as e:
            print(f"Error saving file: {e}")
    
    def load_file(self, filename):
        try:
            with open(filename, "rb") as f:
                self.passwords = pickle.load(f)
        except FileNotFoundError:
            print("File not found. Starting fresh.")
        except Exception as e:
            print(f"Error loading file: {e}")


manager = AdvancedPasswordManager()
manager.add_pass("example.com", "user123", "Strong@123")
manager.save_file("passwords.pkl")
manager.load_file("passwords.pkl")
for i in manager.outdated_pass():
    print("Outdated password for: ",{website})