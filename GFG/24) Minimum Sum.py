"""
Minimum sum

Given an array Arr of size N such that each element is from the range 0 to 9. Find the minimum possible sum of two numbers formed using the elements of the array. All digits in the given array must be used to form the two numbers.


Example 1:

Input:
N = 6
Arr[] = {6, 8, 4, 5, 2, 3}
Output: 604
Explanation: The minimum sum is formed 
by numbers 358 and 246.


Example 2:

Input:
N = 5
Arr[] = {5, 3, 0, 7, 4}
Output: 82
Explanation: The minimum sum is 
formed by numbers 35 and 047.

Your Task:
You don't need to read input or print anything. Your task is to complete the function solve() which takes arr[] and n as input parameters and returns the minimum possible sum. As the number can be large, return string presentation of the number without leading zeroes.
 

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 107
0 ≤ Arri ≤ 9

"""

# SOLUTION

class Solution:
    ## TLE
    # def solve(self, arr, n):
    #     """Finds the maximum alternating sum of two subsequences in the given array."""
    #     s1, s2 = "", ""  # Initialize empty strings for subsequences
    #     arr.sort()  # Sort the input array in ascending order
    
    #     # Alternate appending elements to respective subsequences
    #     for i in range(n):
    #         if i % 2 == 0:
    #             s1 += str(arr[i])  # Append the element to s1
    #         else:
    #             s2 += str(arr[i])  # Append the element to s2
    
    #     max_sum = self.sumof(s1, s2)  # Calculate maximum alternating sum
    #     return max_sum

    # def sumof(self, s1, s2):
    #     i = len(s1) - 1
    #     j = len(s2) - 1
    #     _sum = ""  # Initialize the sum string
    #     carry = 0  # Initialize carry for addition
    
    #     # Loop to perform addition and carry propagation
    #     while i >= 0 or j >= 0:
    #         d1 = 0
    #         d2 = 0
    
    #         if i >= 0:
    #             d1 = int(s1[i])  # Convert the character to an integer
    
    #         if j >= 0:
    #             d2 = int(s2[j])  # Convert the character to an integer
    
    #         temp_sum = d1 + d2 + carry  # Calculate the sum of digits and carry
    #         _sum = str(temp_sum % 10) + _sum  # Append the digit to the result
    #         carry = temp_sum // 10  # Calculate the carry
    
    #         if i >= 0:
    #             i -= 1
    
    #         if j >= 0:
    #             j -= 1
    
    #     if carry != 0:
    #         _sum = str(carry) + _sum  # If there's a carry, append it to the result
    
    #     # Remove leading zeros from the result
    #     for i in range(len(_sum)):
    #         if _sum[i] != '0':
    #             return _sum[i:]
    
    #     return "0"  # If the result is all zeros, return "0"
    
    # ------------------------------------------------------
    
    def solve(self, arr, n):
        if n == 1:
            return str(arr[0])  # If there's only one element, return it as is.

        # Sort the array in non-decreasing order.
        arr.sort()
    
        # Create two empty strings to represent the two numbers.
        num1 = ""
        num2 = ""
    
        for i in range(n):
            # Add digits to the two numbers alternately.
            if i % 2 == 0:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])
    
        # Convert the two strings to integers and calculate their sum.
        sum_of_numbers = int(num1) + int(num2)
    
        # Convert the result to a string without leading zeroes.
        return str(sum_of_numbers)