"""
Recamans sequence

Easy

Given an integer n, return the first n elements of Recaman’s sequence.
It is a function with domain and co-domain as whole numbers. It is recursively defined as below:
Specifically, let a(n) denote the (n+1)th term. (0 being the 1st term).
The rule says:
a(0) = 0
a(n) = a(n-1) - n, if a(n-1) - n > 0 and is not included in the sequence previously
     =  a(n-1) + n otherwise.

Example 1:
Input: 
n = 5
Output: 
0 1 3 6 2
Explaination: 
a(0) = 0,
a(1) = a(0)-1 = 0-1 = -1 and -1<0, therefore a(1) = a(0)+1 = 1,
a(2) = a(1)-2 = 1-2 = -1 and -1<0, therefore a(2) = a(1)+2 = 3,
a(3) = a(2)-3 = 3-3 = 0 but since 0 is already present in the sequence, a(3) = a(2)+3 = 3+3 = 6,
a(4) = a(3)-4 = 6-4 = 2.
Therefore the first 5 elements of Recaman's sequence will be 0 1 3 6 2.

Example 2:
Input: 
n = 3
Output: 
0 1 3
Explaination: 
As seen in example 1, the first three elements will be 0 1 3.
Your Task:
You do not need to read input or print anything. Your task is to complete the function recamanSequence() which takes n as the input parameter and returns the sequence.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n ≤ 10^5

"""

# Solution

class Solution:
    def recamanSequence(self, n):
        if n < 2:
            return [i for i in range(n)]
       
        vis = {0, 1}
        sequence = [0, 1]
        cur = 1

        for i in range(2, n + 1):
            if cur - i >= 0 and cur - i not in vis:
                cur -= i
            else:
                cur += i
                
            vis.add(cur) # visited
            sequence.append(cur)

        return sequence
    