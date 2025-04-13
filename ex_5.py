#Functions
#Find Even Number
'''def find_even(n):
    return n%2 == 0'''

'''l1 = [1,2,3,4,5,6,7,8,9]'''
'''l2 = list(filter(find_even,l1))
print(l2)'''


#using Lambda Functions

'''l2 = list(filter(lambda n : n%2 ==0 , l1))
print(l2)'''

#Find Non-Zero Elements

'''def find_nonzero(n):
    return n!=0'''

'''l1 = [0, 10, 9, 8,0, 53, 0]'''
'''l2 = list(filter(find_nonzero, l1))
print(l2)'''

'''l2 = list(filter(lambda n : n!=0, l1))
print(l2)'''


#Separate negative and positive numbers in a list

''''l1 = [2, -3, 4, 7, -9, 8, -10]
l2 = list(filter(lambda n : n>=0, l1))
print(l2)
l3 = list(filter(lambda n : n<0, l1))
print(l3)'''

#Palindrome
'''def find_palindrome(n):
    return n == n[::-1]
l2 = []'''
'''l1 = ['abc', 'aba', 'bab', 'aaa']'''
'''for i in l1:
   if find_palindrome(i):
        l2.append(i)
print(l2)'''
    

'''l1 = list(filter(lambda n : n == n[::-1], l1))
print(l1)'''

#MAP list elements to double

'''def f1(n):
    return n*2
l1 = [1,2,3,4,5,6]
l2 = list(map(f1,l1))
print(l2)'''

#Store marks and calculate percentage using map

'''def percentage(n):
    return (n/1000)*100'''
'''l1 = [927, 890, 567, 786]'''
'''l2 = list(map(percentage, l1))'''
'''l2 = list(map(lambda n : (n/1000)*100,l1))
print(l2)'''

#Calculate sum of all elements of list

'''import functools
l1 = [1,2,3,4,5,6,7]
sum = functools.reduce(lambda a,b: a+b, l1)
print(sum)'''

#String Concatenation

'''import functools
l1 = ["Hello", " Chavi"," Good", " Morning"]
sum = functools.reduce(lambda a,b : a+b, l1)
print(sum)'''

#Module
import datetime
x = datetime.datetime.now() #2nd datetime is a class and now is function
print(x)
print(x.year)
print(x.month)
print(x.day)

#import datetime
tm = datetime.time(2,25,50,13)
print(tm)

#convert string to date using datetime
from datetime import datetime
print(datetime.strptime('5/5/2019', '%d/%m/%Y'))



