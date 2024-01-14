"""
1657. Determine if Two Strings Are Close

Medium

Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 

Constraints:

1 <= word1.length, word2.length <= 10^5
word1 and word2 contain only lowercase English letters.

"""


# Solution

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = [0] * 26, [0] * 26
        s1, s2 = set(), set()
        
        for c in word1:
            w1[ord(c) - ord('a')] += 1
            s1.add(c)
        
        for c in word2:
            w2[ord(c) - ord('a')] += 1
            s2.add(c)
        
        w1.sort()
        w2.sort()
        
        return w1 == w2 and s1 == s2


# ASCII code
'''
In the expression ord(c) - ord('a'), ord(c) returns the ASCII code of the character c, and ord('a') returns the ASCII code of the character 'a'. 
By subtracting ord('a') from the ASCII code of the character c, you are effectively mapping the character c to an index in the range [0, 25].

In other words, this expression converts a lowercase English alphabet character into a zero-based index. For example:

For 'a', ord('a') - ord('a') is 0.
For 'b', ord('b') - ord('a') is 1.
For 'c', ord('c') - ord('a') is 2.
And so on...
'''

# Time & Space complexity
'''
Time Complexity:
The loops iterating over word1 and word2 have a time complexity of O(N), where N is the length of the longer word.
Sorting w1 and w2 has a time complexity of O(26 * log(26)), which is effectively O(1).
The set operations (s1.add(c) and s2.add(c)) inside the loops have an average time complexity of O(1).
The final comparison w1 == w2 and s1 == s2 has a time complexity of O(26), which is effectively O(1).
Overall, the time complexity is dominated by the loops, and it's O(N).

Space Complexity:
The space complexity is O(26) for the arrays w1 and w2, which is effectively O(1).
The space complexity is O(N) for the sets s1 and s2, where N is the length of the longer word.
Therefore, the overall space complexity is O(N).
'''

# why O(n) not O(nlogn)
'''
The w1.sort() line sorts the list w1, and sorting a list of length n takes O(n log n) time in the worst case. 
In this specific case, the length of w1 is fixed at 26 (since it represents the frequencies of 26 lowercase English alphabet characters), 
so the sorting operation takes O(26 log 26) time, which simplifies to O(1) because the size of the list is constant.

Therefore, even though the sorting operation has a time complexity of O(n log n) in general, the constant size of the 
list makes the time complexity effectively O(1) in this specific scenario. So, when analyzing the overall time complexity
of the entire algorithm, we can consider it as O(N), where N is the length of the longer word. The sorting operation does not 
significantly impact the overall time complexity in this particular context.
'''
