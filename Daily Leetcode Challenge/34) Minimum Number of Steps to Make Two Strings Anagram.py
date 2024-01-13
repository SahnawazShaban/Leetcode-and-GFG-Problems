"""
1347. Minimum Number of Steps to Make Two Strings Anagram

Medium

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
 

Constraints:

1 <= s.length <= 5 * 10^4
s.length == t.length
s and t consist of lowercase English letters only.

"""


# Solution

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_dict = {}

        for val in s:
            s_dict[val] = s_dict.get(val, 0)+1

        count = 0
        for x in range(len(t)):
            if t[x] not in s_dict or s_dict[t[x]] == 0:
                count += 1
            else:
                s_dict[t[x]] -= 1 
        
        return count


'''
Time Complexity:
The first loop that iterates over the characters in string s takes O(len(s)) time.
The second loop that iterates over the characters in string t also takes O(len(t)) time.
Inside the second loop, the dictionary lookup and updates take constant time.
So, the overall time complexity is O(len(s) + len(t)).

Space Complexity:
The space complexity is determined by the dictionary s_dict. In the worst case, where all characters in s are distinct, 
the dictionary could have a size of O(len(s)).
Other than the dictionary, the additional space used is constant.
So, the overall space complexity is O(len(s)).

In summary:

Time Complexity: O(len(s) + len(t))
Space Complexity: O(len(s))
'''
