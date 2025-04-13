#OOPS:
#1
'''class MyClass:
    x=5

p1 = MyClass()
print(p1.x)'''


#2
'''class Arithmetic:
    x=7
    y=9

p1 = Arithmetic()
print(p1.x)
print(p1.y)'''


#3
'''class student:
    def __init__(self, n, r, m):           #self represent the current object, it is a mandatory parameter
        print(id(self))
        self.name = n
        self.roll_no = r
        self.marks = m

    def display(self):                        #instance method
        print("Name =", self.name)
        print("Roll No =", self.roll_no)
        print("Marks =", self.marks)

    def __str__(self):
        return f"{self.name} roll no is {self.roll_no}"


s1 = student("Chavi","21BCON550",85)
s2 = student("Divyam","21BCON096",90)
s1.marks = 95
#del s1.marks ---- it 
print("s1",id(s1))
print("s2",id(s2))
print(s1.name)
print(s1.roll_no)
#print(s1.marks)
print(s2.display())
print(s1)'''


#4
'''class one:
    def __init__(self,name1):
        self.name = name1            #instance variable
        self.version = None            #instance variable
        ph_no = 237654891073        #local variable
        print(ph_no)

    def display(self):
        print(self.name)            #intance variable is accessible
        print(self.version)
        #print(ph_no)                #local variable is not accessible

ref1 = one("Python")
ref1.version = 3.0
ref1.display()'''


#5 Encapsulation

'''class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  #private instace variable (__ for private variable and _ for protected variable)


    def get_balance(self):        #Getter method
        return self.__balance

    def set_balance(self,amount): #Setter method
        if amount >= 0:
            self.__balance = amount

        else:
            print("Invalid balance")

account = BankAccount(1000)
print(account.get_balance())       # accessing via method
account.set_balance(2000)   # modifying via setter
print(account.get_balance())
account.set_balance(-500)          #Prevents invalid operations'''




'''class VoteEligibility:
    def __init__(self, name1):
        self.name = name1
        self.__age = None

    def get_age(self):
        return self.__age

    def set_age(self,age):
        
        if age>=18:
            self.__age = age
            print("Eligible to vote")
        else:
            print("Ineligible to vote")

    def display(self):
        print(self.name)
        print(self.__age)

ref1 = VoteEligibility("Chavi")
ref1.display()


ref1.name = "Jerry"
a = int(input("Enter the age"))
ref1.set_age(a)
ref1.display()'''


#6 Abstraction

'''class car:
    wheels = 4      #static variable
    def __init__(self, brand):
        self.brand = brand

car1 = car("Toyota")
car2 = car("Honda")

print(car1.wheels)     #4(shared variable)
print(car2.wheels)     #4(same for all instances)


car.wheels = 6
print(car1.wheels)     #6
print(car2.wheels)     #6

car1.__class__.wheels = 5
print(car1.wheels)
print(car2.wheels)'''





'''class student:
    __cnt = 101    #static variable declared at class level

    def __init__(self):
        self.__studid = 'S_' + str(student.__cnt)
        student.__cnt +=1

    def get_studid(self):
        return self.__studid

    @staticmethod     #decorator need to be added
    def fun1():       #Static method(no 'self' required)
        loc_var = 100 #local variable allowed
        student.__cnt = student.__cnt+10000 #static vars allowed

s1 = student()
s2 = student()
s3 = student()
#s3.fun1()            #not a good practice
print(s1.get_studid())
print(s2.get_studid())
print(s3.get_studid())
student.fun1()       #static function call'''


'''class Account:
    def __init__(self,a):
        self.acc_no = a
        self.__balance = 1000

obj = Account(12345)
print(obj.acc_no)

print(obj._Account__balance)       #Name Mangling---its not a good practice'''


#print(dir(int))


'''class Fraction:
    def __init__(self,numerator,denominator):
        
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def __add__(self,second):
        temp = Fraction(0,0)
        temp.numerator = self.numerator*second.denominator + self.denominator*second.numerator
        temp.denominator = self.denominator*second.denominator
        return temp

f1 = Fraction(4,5)
f2 = Fraction(2,3)
f3 = f1+f2
print(f1)
print(f2)ff
print(f3)'''


gems = ["Ruby", "Daimond", "Sapphire", "Ivory","Emerald"]
cus_gems = ["Daimond", "Ivory", "Emerald"]
price = [7000, 9000, 10000, 6000, 7500]
gems_quantity = [4, 8, 10]

def calculate_bill(gems, cus_gems, price,  gems_quantity):
    total_cost = 0

    for gem, quantity in zip(cus_gems,gems_quantity):
        if gem in gems:
            index = gems.index(gem)
            total_cost += price[index]*quantity
        else:
            return -1


    if total_cost>30000:
        total_cost -= total_cost*(5/100)

    return total_cost

bill_amount = calculate_bill(gems, cus_gems, price,  gems_quantity)
print("Your total bill is:", bill_amount)








    
    



    


