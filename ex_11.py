#Multithreading

'''import threading
import time

def print_numbers():
    for i in range(1,6):
        print(f"Number : {i}\n")
        time.sleep(1)


def print_letters():
    for char in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {char}")
        time.sleep(1.5)

#creating threads for each function
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letters)

#starting threads
t1.start()
t2.start()

#waiting for both threads to complete
t1.join()
t2.join()

print("Both threads completed.")'''


#using class-based threads  - inherits from treading.Thread and override the run() method ...this allows better structure

'''import threading
import time

class MyThread(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(3):
            print(f"Thread {self.name} is running, iteration {i} \n")
            time.sleep(1)


t1 = MyThread("One")
t2 = MyThread("Two")


t1.start()
t2.start()


t1.join()
t2.join()

print("Class - based threads completed")'''



#Bank System

'''import threading
import time


class BankAccount:
    def __init__(self,balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self,amount):
        with self.lock:
            print(f"Depositing{amount}")
            time . sleep(1)
            self.balance +=amount
            print(f"New balance after deposit: {self.balance}")


    def withdraw(self,amount):
        with self.lock:
            if self.balance >= amount:
                print(f"Withdrawing {amount}")
                time.sleep(1)
                self.balance -= amount
                print(f"New balance after withdrawal: {self.balance}")
            else:
                print("Insufficient Balance")

def deposit_task(account, amount):
    account.deposit(amount)

def withdraw_task(aacount, amount):
    account.withdraw(amount)

account = BankAccount(100)


t1 = threading.Thread(target = deposit_task, args=(account, 50))
t2 = threading.Thread(target = withdraw_task, args=(account, 70))
t3 = threading.Thread(target = withdraw_task, args=(account, 30))

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()


print(f"Final Balance: {account.balance}")'''



#MultiProcessing

'''import multiprocessing
import time

def worker(num):
    """worker function"""
    print(f'Worker {num}')
    time.sleep(1)
    


if __name__ =='__main__':
    jobs = []
    for i in range (5):
        p = multiprocessing.Process(target = worker, args =(i,))
        jobs.append(p)
        p.start()
    for p in jobs:
        p.join()'''


#DATA SCIENCE----NUMBER CRUNCHING USING NUMPY

import numpy as np
OneD_arr = np.array([1,2,3,4,5])
print("1:D Array: \n", OneD_arr)

TwoD_arr = np.array(
                [
                    [1,2,3],
                    [4,5,6]
                    ]
                )
print("2:D Array: \n", TwoD_arr)
                
      


        
