#FileNotFoundError
'''try:
    
    file=open("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\randomm.txt","r")
except FileNotFoundError :
    print("File not found.")'''

#ValueError
'''try:
    n = int(input("Enter the number"))
except ValueError:
    print("Invlid Input")'''

#Raising Exception
'''class IncorrectPassword(Exception):
    pass
try:
    username = input("Enter the valid username")
    password = input("Enter the password")
    required_password = 12345

    if password != required_password:
        raise IncorrectPassword("Enter Valid Password")
except IncorrectPassword :
    print ("Password Incorrect...Enter Valid Password")'''

#Calculator
'''
def add():
    a = float(input("Enter the a"))
    b = float(input("Enter the b"))
    return a+b

def sub():
    a = float(input("Enter the a"))
    b = float(input("Enter the b"))
    return a-b

def mul():
    a = float(input("Enter the a"))
    b = float(input("Enter the b"))
    return a*b

def div():
    a = float(input("Enter the a"))
    b = float(input("Enter the b"))
    return a/b

def Calculator():
    while True:
        

        print("Calculator")
        print("1. Add")
        print("2. Sub")
        print("3. Multiply")
        print("4. Division")

        choice = input("Choose an otion: ").strip()

        if choice == "1":
            print("Addition:", add())
        elif choice == "2":
            print("Subtract:", sub())
        elif choice == "3":
            print("Multiply:", mul())
        elif choice == "4":
            print("Division:",div())
        else:
            print("Invalid choice! Try again.")


Calculator()'''

class obj:
    obj1 = "Orange"

o1 = obj()
print(o1.obj1)

    
'''file.write("Indias got latent....not exist")
file.close()
print("file is created...")'''
