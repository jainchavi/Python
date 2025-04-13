#NAME :CHAVI JAIN
#BATCH : 3
#JECRC UNIVERSITY




#1) Custom String Class with OOP Features
'''Problem Statement:
Implement a class FileOps initialized with two files. One for reading and one for writing. The first file
contain one entry in each line, can be either string or number. Read the strings only and write a
report in the second file with the entry as result of following operations. Implement exception
handling while reading the file
Palindrome, Number of vowels, Number of consonants, resulting string with duplicates removed
Input Format:
- Input line abcefgaccdbgh
- Output Line: N, 3, 10, abcefgdh'''

class FileOps:
    def __init__(self,read,write):
        self.read = read
        self.write = write

    def run_file(self):
        try:
            with open(self.read, 'r') as read_file ,open(self.write,'w')as write_file:
                for i in read_file:
                    s = i.strip()
                    if s.isalpha():
                        is_palindrome = 'Y' if s == s[::-1] else 'N'
                        vowels = sum(1 for c in s if c in "aeiouAEIOU")
                        consonants = sum(1 for c in s if c.isalpha() and c not in "aeiouAEIOU")
                        unique_str = "".join(dict.fromkeys(s))
                        write_file.write(f"{is_palindrome}, {vowels}, {consonants}, {unique_str}\n")
        except Exception as e:
            print(f"Error: {e}")


file_ops = FileOps("C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\input.txt","C:\\Users\\CHAVI JAIN\\OneDrive\\Desktop\\output.txt")
file_ops.run_file()



#2) Word Frequency Counter in Large Text
'''Design a program to read a large text and count the frequency of each unique word, ignoring case
and punctuation.

Task: Build a class WordFrequencyCounter with method count_words(text).
Input:
"The quick brown fox jumps over the lazy dog. The dog barked."
Output:
the:3,quick:1,brown:1,fox:1,jumps:1, over:1, lazy:1,dog:2,barked:1 '''

import re

class WordFrequencyCounter:
    def count_words(self, text):
        text = text.lower()  # Convert to lowercase
        words = re.findall(r'\b\w+\b', text)  # Extract words
        word_count = {}  # Dictionary to store word frequencies

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        return word_count

text = "The quick brown fox jumps over the lazy dog. The dog barked."
counter = WordFrequencyCounter()
print(counter.count_words(text))



#Task: 3 write the code as per the given test cases

'''Every decimal number can be changed into its binary form. Suppose your computer has
Its own Coronavirus, that eats binary digits from the right side of a number. Suppose a
Virus has 6 spikes, it will eat up 6 LSB binary digits in your numbers.

You will have a bunch of numbers, and your machine will have a virus with n spikes, you
Have to calculate what will be the final situation of the final numbers.
Input Format:
First line, a single Integer N
Second line N space separated integers of the bunch of values as array V
Third line a single integer n, the number of spikes in Corona for Computer
Output Format:
Single N space separated integers denoting the final situation with the array v.
Sample Input:
5
1 2 3 4 5
2
Output:
0 0 0 1 1'''


class VirusEffect:
    def __init__(self, values, spikes):
        self.values = values
        self.spikes = spikes

    def run(self):
        result = []
        for i in self.values:
            binary = bin(i)[2:]  # Convert to binary (remove '0b' prefix)
            truncated_binary = binary[:-self.spikes] if len(binary) > self.spikes else '0'
            result.append(int(truncated_binary, 2))  # Convert back to decimal
        return result


N = int(input("Enter the number of elements:"))  # Number of elements
V = list(map(int, input("Enter the list of numbers:").split()))  # List of numbers
spikes = int(input("Enter the number of spikes:"))  # Number of spikes


virus = VirusEffect(V, spikes)
output = virus.run()


print(*output)

