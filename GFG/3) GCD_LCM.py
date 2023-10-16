"""
LCM And GCD

Given two numbers A and B. The task is to find out their LCM and GCD.

 

Example 1:

Input:
A = 5 , B = 10
Output:
10 5
Explanation:
LCM of 5 and 10 is 10, while
thier GCD is 5.
Example 2:

Input:
A = 14 , B = 8
Output:
56 2
Explanation:
LCM of 14 and 8 is 56, while
thier GCD is 2.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function lcmAndGcd() which takes an Integer N as input and returns a List of two Integers, the required LCM and GCD.

 

Expected Time Complexity: O(log(min(A, B))
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= A,B <= 1018

"""

# SOLUTION

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        # gcd = 0
        
        # for num in range(1, min(A,B)+1):
        #     if A%num == 0 and B%num == 0:
        #         gcd = num
                
        # lcm = (A*B)//gcd
        # return (lcm, gcd)
        
        def gcdCalculate(a,b):
            while b:
                a, b = b, a%b
            return a
        
        gcd = gcdCalculate(A,B)
        lcm = (A*B)//gcd
        
        return (lcm, gcd)