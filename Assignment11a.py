#CHAVI JAIN
#BATCH 3
#JECRC UNIVERSITY


'''
#1
Rahul is learning about letters and their frequencies in words. He wants to know how many times each letter appears in a given word. Write a Python program to help Rahul find the frequency of each letter in the word.
The first line contains a single string word (the word to analyze).
The word will contain only lowercase English letters.
1≤length of word≤1000.
Print the frequency of each letter in the word in alphabetical order. Each line should contain the letter followed by its frequency.
hello


e 1
h 1
l 2
o 1
'''


def frequency_count(word):
    freq = {}

    for letter in word:
        freq[letter] = freq.get(letter,0)+1
    
    for letter in sorted(freq):
        print(letter, freq[letter])

word = input("Enter the word:").strip()
frequency_count(word)



