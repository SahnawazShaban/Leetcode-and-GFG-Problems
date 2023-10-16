"""
Addition of Two Numbers
SchoolAccuracy: 79.5%Submissions: 48K+Points: 0
We've got offers as great as this problem! Explore Geek Week 2023

banner
Given two numbers A and B. Your task is to return the sum of A and B.

 

Example 1:

Input:
A = 1, B = 2
Output:
3
Explanation:
Addition of 1 and 2 is 3.

"""


# Solution 

class Solution:
    def addition (ob,A,B):
        # code here 
        ob = A+B
        return ob

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input())
    for _ in range (t):
        
        A,B=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.addition(A,B))
# } Driver Code Ends