"""
1704. Determine if String Halves Are Alike

Easy

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 
Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.

"""


# Solution 

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Brute Force

        n = len(s)

        mid = n//2
        a = s[:mid]
        b = s[mid:]
        
        countA = 0
        countB = 0

        for i in range(len(a)):
            if a[i] in 'aeiouAEIOU':
                countA += 1
            if b[i] in 'aeiouAEIOU':
                countB += 1

        return countA == countB

        # Time Complexity: O(n)
        # Space Complexity: O(n)  

        # --------------------------------------

        # Optimal
        i = 0
        j = n-1

        countI, countJ = 0

        while i < j:
            if s[i] in 'aeiouAEIOU':
                countI += 1
            if s[j] in 'aeiouAEIOU':
                countJ += 1
            i += 1
            j -= 1

        return countI == countJ

        '''
        The time complexity of this optimal solution is O(n), where n is the length of the input string s. The space complexity is O(1) since it uses a constant amount of extra space.
        '''
        