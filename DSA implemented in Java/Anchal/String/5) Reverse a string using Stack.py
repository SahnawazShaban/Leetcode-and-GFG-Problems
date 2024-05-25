"""
Reverse a string using Stack

Easy

You are given a string S, the task is to reverse the string using stack.

Example 1:
Input: S="GeeksforGeeks"
Output: skeeGrofskeeG

Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which takes the string S as an input parameter and returns the reversed string.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ length of the string ≤ 100

"""

# SOLUTION

class Solution:
    # Solution - 1
    def reverse(S):
        n = len(S)
        l = 0
        r = n-1
        S = list(S)

        while l <= r:
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1

        return "".join(S)
    
    # ------------------------------------
    
    # Solution - 2

    def reverse(S):
        reversed_string = ""
        n = len(S)
        r = n - 1

        while r >= 0:
            reversed_string += S[r]
            r -= 1

        return reversed_string
    
    # ---------------------------------

    # Solution - 3

    def reverse(S):
        reversed_string = ''.join(S[i] for i in range(len(S)-1, -1, -1))
        return reversed_string