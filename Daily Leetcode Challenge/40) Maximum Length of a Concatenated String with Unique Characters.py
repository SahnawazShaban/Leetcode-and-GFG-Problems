"""
1239. Maximum Length of a Concatenated String with Unique Characters

Medium

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:
Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:
Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.


Constraints:
1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.

"""


# SOLUTION

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        unique = ['']
        maxi = 0

        for word in arr:
            size = len(unique)

            for j in range(size):
                x = word + unique[j]

                if len(x) == len(set(x)):
                    unique.append(x)
                    maxi = max(maxi, len(x))

        return maxi


'''
# Recursion

class Solution:
    def solve(self, words, index, word):
        if len(word) != len(set(word)):
            return
        self.ans = max(self.ans, len(word))
        if index == len(words):
            return
        for i in range(index, len(words)):
            self.solve(words, i+1, word+words[i])
    
    def maxLength(self, arr: List[str]) -> int:
        self.ans = 0
        self.solve(arr, 0, '')
        return self.ans
'''

'''
# Bit Manipulation:
Explanation
Initial the result res to include the case of empty string "".
res include all possible combinations we find during we iterate the input.

Itearte the the input strings,
but skip the word that have duplicate characters.
The examples is kind of misleading,
but the input string can have duplicate characters,
no need to considerate these strings.

For each string,
we check if it's conflit with the combination that we found.
If they have intersection of characters, we skip it.
If not, we append this new combination to result.

return the maximum length from all combinations.

# SOLUTION
def maxLength(self, A):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)
'''
