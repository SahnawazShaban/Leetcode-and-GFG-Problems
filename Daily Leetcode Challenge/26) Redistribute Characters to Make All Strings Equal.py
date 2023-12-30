"""
1897. Redistribute Characters to Make All Strings Equal

Easy

You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.


Example 1:
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

"""


# Solution 

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Initialize an empty dictionary to store the count of each character
        temp_dict = {}

        # Loop through each word in the list of words
        for word in words:
            # Loop through each character in the current word
            for i in word:
                # Check if the character is already in the dictionary
                temp_dict[i] = temp_dict.get(i, 0)+1

        # Get the total number of words in the list
        n = len(words)

        # Loop through the items (key-value pairs) in the dictionary
        for k, v in temp_dict.items():
            # Check if the count of the character is not divisible evenly by the total number of words
            if (v % n) != 0:
                # If any character count is not divisible evenly, return False
                return False

        # If all character counts are divisible evenly, return True
        return True

'''
Time Complexity:
The outer loop iterates through each word in the list of words, which takes O(m) time, where m is the total number of characters in all words combined.
The nested inner loop iterates through each character in the current word. In the worst case, this loop iterates over all characters in all words, contributing O(m) time complexity.
The final loop iterates through the items in the dictionary, which can have at most O(m) unique characters.
Therefore, the overall time complexity is O(m).

Space Complexity:
The space complexity is determined by the dictionary temp_dict, which stores the count of each character.
In the worst case, all unique characters in all words are stored in the dictionary. Therefore, the space complexity is O(m), where m is the total number of characters in all words combined.
'''