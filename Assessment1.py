#NAME : CHAVI JAIN
#BATCH : 3
#JECRC UNIVERSITY


#1
'''The function accepts a string 'str' of length n and two characters 'chl' and 'ch2' as its
arguments.
Implement the function to modify and return the string'str' in such a way that all occurrences of 'ch1'
in original string are replaced by 'ch2' and all occurrences of ch2' in original string are replaced by 'ch1'.
Assumption: String Contains only lower-case alphabetical letters.
Note:
* Return null if string is null.
* If both characters are not present in string or both of them are same, then return the string unchanged.
Example:
* Input:
- Str: apples
- chl: a
- ch2: p
* Output:
- paales
Explanation:
'a' in original string is replaced with 'p' and 'p' in original string is replaced with 'a', thus output is paales.'''


def replace( Str, ch1, ch2):
    if str is None:
        return None

    if ch1 == ch2 or (ch1 not in Str and ch2 not in Str):
        return str


    ans = ""

    for i in Str:
        if i == ch1:
            ans += ch2
        elif i == ch2:
            ans += ch1
        else:
            ans += i

    return ans

Str = input("Enter the input String:")
ch1 = input("Enter ch1:")
ch2 = input("Enetr ch2:")

print(replace(Str, ch1, ch2))




#2
'''The function accepts 3 positive integers 'a', b'and'' as its arguments. Implement the function to return:
* (a +b), ifc = 1
* (a-b), ifc = 2
* (a *b), Ifc = 3
* (a/b). ife = 4
Assumption: All operations will result in integer output.
Example:
* Input
- c: 1
- a: 12
- b: 16
* Output:
- Since 'C' = 1, (12 + 16) is performed which is equal to 28, hence 28 Is returned.
Sample Input:
- c: 2
- a: 16
- b: 20
Sample Output:
-4 '''


def calculation(a, b, c):
    

    if c == 1:
        return a+b
    
    elif c == 2:
        return a-b
    
    elif c == 3:
        return a*b
            
    elif c == 4:
        return a//b
    
    else:
        return "Invalid choice! Try again."

a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

print(calculation(a, b, c))



#3
''' Count prime number in the given range
The function accepts two positive integers m and n and returns the count of prime numbers between m and n inclusive.
Example:
* Input:
m = 10, n = 20
Output:
Explanation:
Prime numbers between 10 and 20 are (11, 13, 17, 19).'''


def find_prime(nums):
    if nums < 2:
        return False

    for i in range(2 , nums):
        if nums%i == 0:
            return False
    return True

def count(m,n):
    cnt = 0

    for j in range(m , n+1):
        if find_prime(j):
            cnt = cnt+1
    return cnt

m = int(input("Enter the number m :"))
n = int(input("Enter the number n :"))
print("Prime numbers between m and n are:", count(m, n))




#4
'''The function accepts 2 positive integers 'm' and 'n' as its arguments. You are required to calculate the sum
of numbers divisible both by 3 and 5, between 'm' and 'n' both inclusive and return the
same.
Note:
0 <m <= n
Example:
* Input:
o m: 12
on: 50
* Output:
090
Explanation:
The numbers divisible by both 3 and 5, between 12 and 50 both inclusive are (15, 30, 45) and their sum is 90.
Sample Input:
* m: 100
* n: 160
Sample Output:
510'''

def divisible(m,n):
    cnt = 0
    for i in range(m , n+1):
        if i%3 == 0 and i%5 == 0:
            cnt += i
    return cnt

m = int(input("Enter the number m :"))
n = int(input("Enter the number n :"))
print("The numbers divisible by both 3 and 5 are:", divisible(m, n))



