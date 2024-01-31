"""
Insert and Search in a Trie

Medium

Complete the Insert and Search functions for a Trie Data Structure. 

Insert: Accepts the Trie's root and a string, modifies the root in-place, and returns nothing.
Search: Takes the Trie's root and a string, returns true if the string is in the Trie, otherwise false.
Note: To test the correctness of your code, the code-judge will be inserting a list of N strings called into the Trie, and then will search for the string key in the Trie. The code-judge will generate 1 if the key is present in the Trie, else 0.

Example 1:
Input:
n = 8
list[] = {the, a, there, answer, any, by, bye, their}
key = the
Output: 1
Explanation: 
"the" is present in the given set of strings. 

Example 2:
Input:
n = 8
list[] = {the, a, there, answer, any, by, bye, their}
key = geeks
Output: 0
Explanation: 
"geeks" is not present in the given set of strings.

Your Task:
You do not have to take any input or print anything. Complete insert and search functions. 

Expected Time Complexity: O(M+|key|)
Expected Auxiliary Space: O(M)
Here M = sum of the length of all strings which are present in the list[] 

Constraints:
1 <= N <= 10^4
1 <= length of list[i] <= 30
All strings will constitute of lowercase alphabets only.

"""

'''
In Python, the ord() function is used to get the Unicode code point of a given character. 
The Unicode code point is an integer representation of a character in the Unicode standard. 

For example:
print(ord('A'))  # Output: 65
print(ord('a'))  # Output: 97
print(ord('1'))  # Output: 49
'''

# Solution 

"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    #Function to insert string into TRIE.
    def insert(self, root, key):
        for char in key:
            nextNode = root.children[ord(char)-97]
            if not nextNode:
                newNode = TrieNode()
                root.children[ord(char)-97] = newNode
                root = newNode
            else:
                root = nextNode
        root.isEndOfWord = True

    #Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        for char in key:
            nextNode = root.children[ord(char)-97]
            if not nextNode:
                return False
            else:
                root = nextNode
        return root.isEndOfWord is True
    