"""
204. Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

"""

# SOLUTION

class Solution:
    def countPrimes(self, n: int) -> int:
        '''TLE'''
        # if n == 0 or n == 1:
        #     return 0
        # count = 0
        # for i in range(2,n):
        #     flag = True
        #     for j in range(2,i):
        #         if i%j == 0:
        #             flag = False
        #     if flag:
        #         count += 1

        # return count

        if n < 2:
            return 0
        
        count_list = [True]*(n+1)
        count_list[0] = count_list[1] = False
        p = 2

        while p*p <= n:
            if count_list[p]:
                for i in range(p*p,n+1,p):
                    count_list[i] = False
            p += 1

        count = 0
        for i in range(2,n):
            if count_list[i]:
                count += 1

        return count