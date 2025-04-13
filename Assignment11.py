''' 3 You are given a list of words. Your task is to group all the anagrams together and return the grouped
list. An anagram is a word formed by rearranging the letters of another word (e.g., &quot;listen&quot; and
&quot;silent&quot;).
Input:
 A list of words, where each word consists of lowercase English letters.
 1 ≤ number of words ≤ 10,000
 1 ≤ length of each word ≤ 100
Output:
 A list of lists, where each inner list contains words that are anagrams of each other.
 The order of the groups and the order of words within each group do not matter.
Example:
Input: [eat,tea, tan, ate, nat, bat]
Output: [[eat, tea, ate], [tan, nat], [bat]]
'''

def grp_anagram(words):
    anagram = {}

    for word in words:
        sort_word = tuple(sorted(word))
        if sort_word in anagram:
            anagram[sort_word].append(word)
        else:
            anagram[sort_word] = [word]
    return list(anagram.values())

words = ['eat','tea', 'tan', 'ate', 'nat', 'bat'] 
print(grp_anagram(words))

'''Problem 4:Longest Consecutive Sequence
Given an unsorted list of integers, find the length of the longest sequence of consecutive numbers.
The algorithm must run in O(n) time.
Input:
 A list of integers, where each integer is in the range [-10^9, 10^9].
 1 ≤ number of integers ≤ 10^5
Output:
 An integer representing the length of the longest consecutive sequence.
Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4 (The longest consecutive sequence is [1, 2, 3, 4])
'''

def long_con(n):
    curr_count =0
    max_count = 1
    prev_smaller = float('-inf')
    n.sort()

    for i in range( len(n)):
        if n[i] -1 == prev_smaller:
            curr_count +=1
            prev_smaller = n[i]
        elif n[i] != prev_smaller:
            curr_count =1
            prev_smaller = n[i]
        max_count = max(max_count , curr_count)

    return max_count

n = [110, 4, 200, 1, 3, 2]
print(long_con(n))


'''Problem 5: Course Schedule
There are a total of n courses you need to take, labeled from 0 to n-1. Some courses have
prerequisites, represented as a list of pairs [a, b], where you need to take course b before course a.
Determine if it is possible to finish all courses.
Input:
 An integer n (1 ≤ n ≤ 10^5), the number of courses.
 A list of prerequisite pairs [a, b], where 0 ≤ a, b &lt; n.
Output:
 True if it is possible to finish all courses, otherwise False.
Example:
Input: n = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: True (One possible order is 0 -> 1 -> 2 -> 3)'''


def canFinish(n, prerequisites):
    graph = {i: [] for i in range(n)}
    for a, b in prerequisites:
        graph[b].append(a)

    visited = [0] * n  

    def hasCycle(course):
        if visited[course] == 1:  
            return True
        if visited[course] == 2:  
            return False

        visited[course] = 1  
        for next_course in graph[course]:
            if hasCycle(next_course):
                return True
        
        visited[course] = 2  
        return False

    for course in range(n):
        if hasCycle(course):
            return False  

    return True  

n = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
print(canFinish(n, prerequisites))