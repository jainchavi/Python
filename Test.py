#1

# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# total_sum = sum(numbers)
# product = 1
# for num in numbers:
#     product *= num
# print(total_sum)
# print(product)


#2

# class Password_manager:
#     def __init__(self):
#         self.old_password = []

#     def get_password(self):
#         if not self.old_password:
#             return None
#         return self.old_password[-1]

#     def set_password(self, password):
#         if password != "" and password not in self.old_password:
#             self.old_password.append(password)

#     def is_correct(self, password):
#         current = self.get_password()
#         if current is None:
#             return False
#         return password == current
    
# p=Password_manager()
# p.set_password("123")
# p.is_correct("123")
# p.get_password()
# p.set_password("1234")
# p.is_correct("1234")




#3


# class TelephoneBook:
#   def __init__(self, contacts):
#     self.contacts = contacts

#   def addContacts(self):
#     with open("C:\\Users\\user\\Desktop\\Capgemeni\\Practice\\contacts.txt", "w") as file:
#       for name, number in self.contacts:
#         file.write(f"{name}:{number}\n")

#   def getContacts(self, startsWith):""
#     result = []
#     for name, number in self.contacts:
#       if name.startswith(startsWith):
#         result.append([name, number])
#     return result


# # Sample test case
# contacts = [['John', '7655'], ['Jeffry', '22937923'], ['Tack', '2323']]
# r = TelephoneBook(contacts)
# r.addContacts()
# res = r.getContacts("T")
# print(res)




#4

# class WicketOutException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#         self.message = message

# class OutException(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#         self.message = message

# class Match:
#     def __init__(self, player1, player2):
#         self.player1 = player1
#         self.player2 = player2

#     def count_special_triples(self, player):
#         count = 0
#         length = len(player)
#         for i in range(length - 1):
#             if i + 1 < length and length - 2 < length:
#                 if player[i] % 2 == 0 and player[i + 1] % 2 == 0 and player[length - 2] % 2 == 0:
#                     count += 1
#         return count

#     def findWinner(self):
#         special_triples_p1 = self.count_special_triples(self.player1)
#         special_triples_p2 = self.count_special_triples(self.player2)

#         if special_triples_p1 > special_triples_p2:
#             return "Player1"
#         elif special_triples_p1 < special_triples_p2:
#             raise OutException("Player 1 out")
#         else:
#             raise WicketOutException("ALL OUT")

# # Sample Input
# p1 = [2, 2, 4, 6]
# p2 = [2, 2, 6, 8]

# d = Match(p1, p2)

# try:
#     print(d.findWinner())
# except Exception as e:
#     print(e.message)

class Patient:
    def __init__(self, name: str, pincode: int, phoneNumber: str, is_corona: bool):
        self.name = name
        self.pincode = pincode
        self.phoneNumber = phoneNumber
        self.is_corona = is_corona

    def getName(self):
        return self.name

    def getPincode(self):
        return self.pincode

    def getPhoneNumber(self):
        return self.phoneNumber

    def getIsCorona(self):
        return self.is_corona


class CoronaPatient:
    def __init__(self):
        self.patients = []

    def addPatient(self, newPatient: Patient):
        self.patients.append(newPatient)

    def getLessCases(self):
        corona_counts = {}
        for patient in self.patients:
            if patient.getIsCorona():
                corona_counts[patient.getPincode()] = corona_counts.get(patient.getPincode(), 0) + 1

        return min(corona_counts, key=corona_counts.get) if corona_counts else None

    def countPositiveCase(self):
        return sum(1 for patient in self.patients if patient.getIsCorona())


# Sample Input
corona_patients = CoronaPatient()
corona_patients.addPatient(Patient("Alice", 12345, "9876543210", True))
corona_patients.addPatient(Patient("Bob", 12345, "9123456789", False))
corona_patients.addPatient(Patient("Charlie", 67890, "8765432109", True))
corona_patients.addPatient(Patient("David", 67890, "7654321098", True))
corona_patients.addPatient(Patient("Eve", 54321, "6543210987", True))

# Expected Output
print("Pincode with least corona cases:", corona_patients.getLessCases())  # Output: 12345
print("Total positive cases:", corona_patients.countPositiveCase())  # Output: 4|

