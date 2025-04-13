
# datetime module in python
'''
import datetime
x= datetime.datetime(2018,5,12,12,50,13)

#to print the weekday
print(x.strftime("%A"))

#to print the month name
print(x.strftime("%B"))

#to print the week as number
print(x.strftime("%w"))

#to define and print AM/PM
print(x.strftime("%p"))


#to compare dates

from datetime import datetime as dt
var=dt.now().hour
if 8<var<16:
    print("workin hours")
else:
    print("fun hours")'''

#calendar module

'''import calendar;

cal=calendar.month(2018,12) #to print calendar of a specific month
print(cal)

calendar.prcal(2018) #to print calendar of entire year
'''
#glob module in python is used for filename pattern matching and allows you to find files and directories that match a specified pattern

'''import glob

files = glob . glob(".txt")
print(files)

python_files = glob.glob("subdir/*.py")
print(python_files)'''


#pickle: used for object serialization(converting a python object into a byte stream so that it can be saved to a file or transferred over a network)
#and deserialization(reconstructing the object from this byte stream)

import pickle

data = {'name':'Alice', 'age':25, 'city':'New York'}

with open('data.pkl','wb') as f:
    pickle.dump(data,f)

with open('data.pkl','rb') as f:
    loaded_data = pickle.load(f)

print(loaded_data)
print(type(loaded_data))


#Iterator (use : when we have to reduce the memory consumption as it uses one element at one point of time

'''my_list = [1, 2, 3]
iterator = iter(my_list)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))'''



'''L = [x for x in range(1, 10000)]

import sys
print(sys.getsizeof(L))


#range function keeps one element in the memory at a time
Y = range(1, 10000)
print(sys.getsizeof(Y))'''


'''X = [25, 45, 'Coding', 'is', '<3']
a = iter(X)

print(a)
print(next(a))'''


'''def fun_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))

        except StopIteration:
            break

L = [1, 2, 3, 4, 5]
fun_for(L)'''

'''class Fibonacci:
    def __init__(self, max_n):
        self.a, self.b = 0, 1
        self.max_n = max_n

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_n:
            raise StopIteration

        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib



for i in Fibonacci(100):
    print(i)'''


#Generators: simple of creating iterators....it generates values one at a time from a given sequence, instead of giving the entire sequence at once....
#this one at a time fashion of generators is what makes them so compatible with for loop

'''def gen_fun():
    yield "First Iterator"
    yield "Second Iterator"
    yield "Third Iterator"

gen = gen_fun()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))'''


'''def square():
    for i in range(20):
        res = i**2
        yield res

gen = square()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))'''


'''def range_fun(start, end):
    for i in range(start, end):
        yield i

gen = range_fun(5,11)
print(next(gen))
print("Inside for lopp:")
for i in gen:
    print(i)'''

'''L = [i**2 for i in range(1,100)]
import sys
print(sys.getsizeof(L))
print(L)'''


'''L = (i**2 for i in range(1,100))    #same thing can be done using generators--replace [] -> () 
import sys
print(sys.getsizeof(L))

for x in L:
    print(x)'''

'''def multi_generate():
    yield "a"; yield "b"; yield "c"

mg = multi_generate()

print(next(mg))
print(next(mg))
print(next(mg))

print(next(multi_generate()))    # new instance generated if you call the function again '''


#Regular Expression

'''import re

text = "Hello, my 23 number is 1234567890"
pattern = r'\d+'
match = re.search(pattern , text)  

print(re.search(pattern,text),"\n")
print(match.group())



#validating an email address

email = "example@example.com"
pattern = r'[\w]+@[\w]+.[\w]+'
if re.match(pattern, email):
    print("Valid email!")


#Finding all words
sentence = "This is a sentense."
words = re.findall(r'\w+', sentence)
print(words)



#Replacing text
text = "Hello World!"
new_text = re.sub(r'World', 'Python', text)
print(new_text)'''

