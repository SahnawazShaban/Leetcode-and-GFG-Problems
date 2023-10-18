"""
Sum of all prime numbers between 1 and N.

Given a positive integer N, find the sum of all prime numbers between 1 and N(inclusive).
 

Example 1:

Input: N = 5
Output: 10
Explanation: 2, 3, and 5 are prime
numbers between 1 and 5(inclusive).
Example 2:

Input: N = 10
Output: 17
Explanation: 2, 3, 5 and 7 are prime
numbers between 1 and 10(inclusive).
 

Your Task:
You don't need to read or print anything. Your task is to complete the function prime_Sum() which takes N as input parameter and returns the sum of all primes between 1 and N(inclusive).
 

Expected Time Complexity: O(N*log(N))
Expected Space Complexity: O(N)

Constraints:
1 <= N <= 1000000

Company Tags
Samsung, Adobe

"""

# SOLUTION

def prime_Sum(self, n):
    """
    TLE : because of O(n^2)
    
    res = 0
    if n < 2:
        return 0
    elif n == 2:
        return n
    else:
        for i in range(2,n+1):
            flag = True
            for j in range(2,i):
                if i%j == 0:
                    flag = False
                    break
            if flag:
                res += i

    return res
    """
    
    if n < 2:
        return 0
    
    list_prime = [True]*(n+1)
    list_prime[0] = list_prime[1] = False
    
    p = 2
    
    while p*p <= n:
        if list_prime[p]:
            for i in range(p*p,n+1,p):
                list_prime[i] = False
        p += 1
    
    # sum of prime numbers
    prime_sum = 0
    for i in range(2,n+1):
        if list_prime[i]:
            prime_sum += i
    # or
    # prime_sum = sum(i for i in range(2, n + 1) if is_prime[i])
            
    return prime_sum