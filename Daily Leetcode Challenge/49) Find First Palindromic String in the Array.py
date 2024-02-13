"""
2108. Find First Palindromic String in the Array

Easy

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 
Example 1:
Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:
Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:
Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.

"""


# SOLUTION

class Solution:
    # Solution - 1
    def check(self, word):
        s, e = 0, len(word)-1
        while s <= e:
            if word[s] != word[e]:
                return False
            s += 1
            e -= 1

        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.check(word):
                return word
        
        return ""

    # -----------------------------

    # Solution - 2
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        
        return ""
    
'''
Solution - 1:

Time Complexity:
Let n be the average length of the words and m be the number of words in the input list.
The function check takes O(n/2) time to determine if a word is a palindrome.
Since this function is called for each word in the list, the overall time complexity is O(m * n).

Space Complexity:
The space complexity is O(1) because the additional space used does not depend on the input size.


Solution - 2:

Time Complexity:
Let n be the average length of the words and m be the number of words in the input list.
Checking if a word is a palindrome using slicing takes O(n) time.
Since this operation is performed for each word in the list, the overall time complexity is O(m * n).

Space Complexity:
The space complexity is O(1) because the additional space used does not depend on the input size.
In summary:

Both solutions have a time complexity of O(m * n), where m is the number of words and n is the average length of the words.
Both solutions have a space complexity of O(1), indicating constant space usage.
'''
