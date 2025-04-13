#NAME : CHAVI JAIN
#BATCH : 3
#JECRC UNIVERSITY


#Task 1: Write code and pass the test cases.
#Easy
'''You are playing an online game. In the game, a list of N numbers is
given. The player has to arrange the numbers so that all the odd
numbers of the list come after the even numbers. Write an algorithm
to arrange the given list such that all the odd numbers of the list
come after the even numbers.
Input

The first line of the input consists of an integer num, representing
the size of the list(N). The second line of the input consists of N
space-separated integers representing the values of the list

Output

Print N space-separated integers such that all the odd numbers of
the list come after the even numbers

Example

Sample Input
8
10 98 3 33 12 22 21 11
Sample Output
10 98 12 22 3 33 21 11
Explanation
All the even numbers are placed before all the odd numbers.
Solution
Input
8
15 16 14 17 18 19 20 11'''

n = int(input("Enter the value of n :"))
L = list(map(int, input().split()))

even = []
odd = []

for i in L:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

result = even + odd
print(*result)


#Task-2: Problem Statement
#Intermediate

'''A digital machine generates binary data which consists of a
string of 0s and 1s. A maximum signal M, in the data, consists
of the maximum number of either 1s or 0s appearing
consecutively in the data but M can’t be at the beginning or
end of the string. Design a way to find the length of the
maximum signal.
Input
The first line of the input consists of an integer N, representing
the length of the binary string. The second line consists of a
string of length N consisting of 0s and 1s only.

Output
Print an integer representing the length of the maximum signal.
Example
Example 1:
Input
6
101000
Output
1
Explanation
For 101000, M can be 0 at the second index or at the third
index so in both cases max length = 1.
Example2:
Input
9
101111110
Output
6
Explanation
For 101111110, M = 111111 so maxlength = 6.
Solution

Input
5
10110'''


def signal_length(s):
    max_count = 0
    count_zero = 0
    count_one = 0

    for char in s:
        if char == '0':
            count_zero += 1
            count_one = 0
        else:
            count_one += 1
            count_zero = 0

        max_count = max(max_count, count_zero, count_one)

    return max_count

def represent():
    n = int(input("Enter the value of n:").strip())
    s = input("Enter the string:").strip()

    last_char = s[-1]
    while s and s[-1] == last_char:
        s = s[:-1]

    if s :
        first_char = s[0]
        while s and s[0] == first_char:
            s = s[1:]

    print("MAX CONT:", signal_length(s))

represent()







#Task-3: Problem Statement
#Difficult
'''Alex works at a clothing store. There is a large pile of socks that
must be paired by color for sale. Given an array of integers
representing the color of each sock, determine how many pairs of
socks with matching colors there are.

For example, there are n=7 socks with colors ar = {1,2,1,2,1,3,2}.
There is one pair of color 1 and one of color 2. There are three odd
socks left, one of each color. The number of pairs is 2.

Function Description
Complete the sockMerchant function in the editor below. It must
return an integer representing the number of matching pairs of
socks that are available.
sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock

Input Format
The first line contains an integer n, the number of socks
represented in ar.

The second line contains n space-separated integers
describing the colors ar[i] of the socks in the pile.

Constraints
1 &lt;= n &lt;= 100
1 &lt;= ar[i] &lt;= 100 &amp; 0 &lt;= i &lt; n

Output Format
Return the total number of matching pairs of socks that Alex
can sell.

Sample Input
9
10 20 20 10 10 30 50 10 20
Sample Output
3

Explanation
Alex can match 3 pairs of socks i.e 10-10, 10-10, 20-20
while the left out socks are 50, 60, 20'''



def sockMerchant(n, ar):
    sock_set = set()
    pairs = 0
    
    for sock in ar:
        if sock in sock_set:
            pairs += 1
            sock_set.remove(sock)
        else:
            sock_set.add(sock)
    
    return pairs

n = int(input("Enter the value of n:"))
ar = list(map(int, input().split()))
print(sockMerchant(n, ar))
