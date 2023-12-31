"""
1624. Largest Substring Between Two Equal Characters

Easy

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.


Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
 

Constraints:

1 <= s.length <= 300
s contains only lowercase English letters.

"""


# Solution 

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Solution - 1 - Time complexity:O(n2) - Space complexity:O(1)
        # Brute Force
        '''
        maxi = -1
        
        for l in range(len(s)):
            for r in range(l + 1, len(s)):
                if s[l] == s[r]:
                    maxi = max(maxi, r - l - 1)
        
        return maxi
        '''

        # Solution - 2 (Hashmap) - Time complexity:O(n) - Space complexity:O(1)
        # Optimal

        temp_dict = {}
        maxi = -1

        for i in range(len(s)):
            if s[i] in temp_dict:
                maxi = max(i-temp_dict[s[i]]-1, maxi)
            else:
                temp_dict[s[i]] = i

        return maxi


        # Solution - 3 (Array) - Time complexity:O(n) - Space complexity:O(1)
        '''
        v1 = [-1] * 26
        v2 = [-1] * 26
        ans = -1

        for i in range(len(s)):
            temp = ord(s[i]) - ord('a')

            if v1[temp] == -1:
                v1[temp] = i
            else:
                v2[temp] = i
                ans = max(ans, v2[temp] - v1[temp] - 1)

        return ans
        '''