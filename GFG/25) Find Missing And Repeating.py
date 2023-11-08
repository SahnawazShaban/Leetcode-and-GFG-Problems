"""
Find Missing And Repeating

Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2,....,N} is missing and one number 'B' occurs twice in array. Find these two numbers.

Example 1:

Input:
N = 2
Arr[] = {2, 2}
Output: 2 1
Explanation: Repeating number is 2 and 
smallest positive missing number is 1.
Example 2:

Input:
N = 3
Arr[] = {1, 3, 3}
Output: 3 2
Explanation: Repeating number is 3 and 
smallest positive missing number is 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function findTwoElement() which takes the array of integers arr and n as parameters and returns an array of integers of size 2 denoting the answer ( The first index contains B and second index contains A.)

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ N ≤ 105
1 ≤ Arr[i] ≤ N

Company Tags :
Amazon, Samsung, D-E-Shaw, Goldman Sachs, MAQ Software

"""

# SOLUTION

class Solution:
    def findTwoElement( self,arr, n): 
        ## TLE
        temp_dict = {}
        for num in arr:
            temp_dict[num] = temp_dict.get(num,0)+1
            
        for key, val in temp_dict.items():
            if val > 1:
                twice = key
                
        for val in range(1,n+1):
            if val not in arr:
                missing = val
                break
            
        return [twice,missing]
        
        # ----------------------------------
        ## Proper Executed
        total_sum = 0
        for val in range(1,n+1):
            total_sum += val
        
        arr_sum = sum(set(arr))
        
        missing = total_sum - arr_sum
        
        twice = sum(arr) - arr_sum
        
        return [twice, missing]