"""
LCS of three strings

Medium

Given 3 strings A, B and C, the task is to find the length of the longest sub-sequence that is common in all the three given strings.

Example 1:
Input:
A = "geeks"
B = "geeksfor", 
C = "geeksforgeeks"
Output: 5
Explanation: 
"geeks"is the longest common subsequence with length 5.

Example 2:
Input: 
A = "abcd"
B = "efgh"
C = "ijkl"
Output: 0
Explanation: 
There's no subsequence common in all the three strings.

Your Task:
You don't need to read input or print anything. Your task is to complete the function LCSof3() which takes the strings A, B, C and their lengths n1, n2, n3 as input and returns the length of the longest common subsequence in all the 3 strings.

Expected Time Complexity: O(n1*n2*n3).
Expected Auxiliary Space: O(n1*n2*n3).

Constraints:
1 <= n1, n2, n3 <= 20
Elements of the strings consitutes only of the lower case english alphabets.

"""


# SOLUTION
# Refer pdf : 2) Concept
class Solution:
    
    def memo(self, i, j, k, A, B, C, dp):
        if i < 0 or j< 0 or k < 0:
            return 0
            
        if dp[i][j][k] != -1:
            return dp[i][j][k]
            
        if A[i] == B[j] == C[k]:
            dp[i][j][k] = 1 + self.memo(i-1, j-1, k-1, A, B, C, dp)
        else:
            dp[i][j][k] = 0 + max(self.memo(i-1, j, k, A, B, C, dp), self.memo(i, j-1, k, A, B, C, dp), self.memo(i, j, k-1, A, B, C, dp))

        return dp[i][j][k]
        
        
    def LCSof3(self,A,B,C,n1,n2,n3):
        dp = [[[-1]*n3 for _ in range(n2)] for _ in range(n1)]
        
        return self.memo(n1-1, n2-1, n3-1, A, B, C, dp)
    

# Time Complexity: O(n1*n2*n3)
# Auxiliary Space: O(n1*n2*n3)
