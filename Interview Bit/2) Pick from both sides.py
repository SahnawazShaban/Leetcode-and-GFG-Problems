"""
Pick from both sides!
Programming
Arrays
Very Easy
51.2% Success

758

137

Bookmark
Asked In:
Problem Description
 
 

Given an integer array A of size N.

You have to pick exactly B elements from either left or right end of the array A to get the maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick the first four elements or can pick the last four elements or can pick 1 from the front and 3 from the back etc. you need to return the maximum possible sum of elements you can pick.


Problem Constraints
1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you picked.



Example Input
Input 1:
 A = [5, -2, 3 , 1, 2]
 B = 3

Input 2:
 A = [1, 2]
 B = 1


Example Output
Output 1:
 8

Output 2:
 2


Example Explanation
Explanation 1:
 Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8

Explanation 2:
 Pick element 2 from end as this is the maximum we can get

"""

# SOLUTION

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        max_sum = 0

        # Calculate the initial sum of the first B elements.
        current_sum = sum(A[:B])
        max_sum = current_sum

        # Iterate over the remaining elements and update the sum by removing elements from the right and adding elements from the left.
        for i in range(B):
            current_sum = current_sum - A[B - 1 - i] + A[n - 1 - i]
            max_sum = max(max_sum, current_sum)

        return max_sum
        
        # -----------------------------------------
        
        n = len(A)
        suff = [0] * (n + 1)
        suff[n - 1] = A[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = A[i] + suff[i + 1]
            
        prefSum = 0
        ans = suff[n - B]
        for i in range(B):
            prefSum = prefSum + A[i]
            suffSum = suff[n - B + i + 1]
            ans = max(ans, prefSum + suffSum)
        return ans
                
