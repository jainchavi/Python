'''class A(object):
    def __new__(cls):
        print("Creating an instance")     #return object.__new__(cls)
        return object.__new__(cls)        #instance is created expilcitly

    def __init__(self):
        print("Init is called")

A()'''


#Private method

'''class Login:
    def __init__(self, username, password):
        self.id = username   #public variable
        self.__pwd = password #private variable
        self.__pvt_method()

    def __pvt_method(self):
        print("This is a Private Method")


obj = Login("asdf","adfgggh")
print(obj.pvt_method())'''


#Member data and constructor get inherited

'''class student:
    def __init__(self, name, rollno , marks):
        self.__name = name
        self._rollno = rollno
        self.marks = marks

class BTech(student):
    pass

obj = BTech("AAA", 1, 90)
print(obj.marks)
print(obj._rollno)
print(obj.__name)'''


#Derived class can access the members of parent class but the opposite is not possible

'''class student:
    def __init__(self, name, rollno, marks):
        self.__name = name
        self.rollno = rollno
        self.marks = marks

    def get_name(self):
        return self.__name

class Btech(student):
    def __init__(self, name, rollno, marks, marks_12th):
        #calling constructor of parent class
        student.__init__(self, name ,rollno, marks)
        #OR: self is not required in super()
        #super().__init__(name, rollno, marks)

        self.marks_12th = marks_12th

        
s1 = student("John", 21, 50)
print(s1.rollno)

b1 = Btech("dghjk",65, 78, 79)
print(b1.get_name(),b1.rollno, b1.marks, b1.marks_12th)'''

#Multiple Inheritance
#If child do not have its own constructor

'''class Base1():
    def __init__(self):
        print("Base1 init")

class Base2():
    def __init__(self):
        print("Base2 init")

#sequence of inheritance decides which constructor gets called
#This is called as MRO(Method Resolution Order)

class Derived(Base2, Base1):
    pass

ob = Derived()'''


#if child class has its own constructor

'''class Base1():
    def __init__(self):
        self.str1 = "Base1"
        print("Base1 init")

class Base2():
    def __init__(self):
        self.str2 = "Base2"
        print("Base2 init")

class Derived(Base1, Base2):
    def __init__(self):
        #Calling constructor of Base1 and Base2
        Base2.__init__(self)
        Base1.__init__(self)
        print("Derived")

    def printStr(self):
        print(self.str1, self.str2)

ob = Derived()
ob.printStr()'''


#Multilevel Inheritance
'''class Base():
    def __init__(self):
        print("Parent")

class Child(Base):
    def __init__(self):
        print("Child")
        super().__init__()

class GrandChild(Child):
    def __init__(self):
        print("GrandChild")
        super().__init__()

g = GrandChild()'''




#Abstract Class

'''from abc import ABC , abstractmethod

class Animal(ABC):    #abstract class
    @abstractmethod
    def speak (self): #abstract method(must be implemented in subclass)
        pass


class Dog(Animal):
    def speak(self):
        return "Bark!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


#animal = Animal()  #Error: cannot instantiate abstract class
dog = Dog()
print(dog.speak())
cat = Cat()
print(cat.speak())'''



'''from abc import ABC, abstractmethod
import time

class Vehicle(ABC):
    def __init__(self,brand):
        print("init")
        time.sleep(2)
        self.brand = brand #instance variable

    @abstractmethod
    def start(self):        #abstract method
        pass

    def display_brand(self): #concrete method
        print(f"Brand : {self.brand}")


class Car(Vehicle):
    def start(self):
        print(f"{self.brand} Car is starting..")

car = Car("Tesla")
print("In Main")
car.start()
car.display_brand()'''


#Polymorphism Method Overriding
'''class Parent():
    #constructor
    def __init__(self):
        self.value = "Parent"


    def show(self):
        print(self.value)

class Child(Parent):
    def __init__(self):
        self.value = "Child"

    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()

print(obj1.show())
print(obj2.show())'''


#operator overloading

'''class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Point(self.x + other.x , self.y + other.y)

    def __str__(self):
        return f"{self.x},{self.y}"

p1 = Point(2,3)
p2 = Point(3,4)
p3 = p1+p2

print(p3.x,p3.y)
print(p3)'''


#Decorators is a function that modifies the behavior of another function

'''def my_decorator(func):
    def wrapper():
        print("********")
        func()
        print("********")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()




def my_decorator(func):
    def wrapper(*args):
        print("Function is called with argument:",args)
        return func(*args)
        
    return wrapper

@my_decorator
def add(a,b):
    return a+b

print(add(3,4))



#find time taken by the function

import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {end-start:.5f} seconds")
        return result
    return wrapper


@timer
def fun1(a):
    time.sleep(2)
    print("fun1:", a)
@timer
def fun2(a,b):
    time.sleep(3)
    print("fun2:", a+b)

fun1(2)
fun2(10,20)'''



from abc import ABC , abstractmethod

class Map(ABC):
    
    @abstractmethod
    def start(self, location):
        print("MAP")

class Call(ABC):
    
    @abstractmethod
    def start1(self, phn_no):
        print("Calling")

class Payment(ABC):

    @abstractmethod
    def start2(self, payment_modes):
        print("Payment")

class App(Map, Call, Payment):
    def start(self):
        return

        

        
