"""
Count Digits
SchoolAccuracy: 30.45%Submissions: 115K+Points: 0
We've got offers as great as this problem! Explore Geek Week 2023

banner
Given a number N. Count the number of digits in N which evenly divides N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
 

Example 1:

Input:
N = 12
Output:
2
Explanation:
1, 2 both divide 12 evenly
Example 2:

Input:
N = 23
Output
0
Explanation:
2 and 3, none of them
divide 23 evenly

Your Task:
You don't need to read input or print anything. Your task is to complete the function evenlyDivides() which takes an integer N as input parameters and returns an integer, total number factor of digits N which divides N evenly.


Expected Time Complexity: O(log N)
Expected Space Complexity: O(1)
 

Constraints:
1<=N<=105

"""

# SOLUTION

class Solution:
    def evenlyDivides (self, N):
        temp = N
        count = 0
        while temp != 0:
            digit = temp%10
            if digit != 0 and N % digit == 0:
                count += 1
            
            temp = temp//10
            
        return count