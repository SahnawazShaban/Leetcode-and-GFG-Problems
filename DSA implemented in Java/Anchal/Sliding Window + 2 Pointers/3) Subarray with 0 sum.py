"""
Subarray with 0 sum

Medium

Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. You just need to return true/false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the driver code.

Example 1:
Input:
n = 5
arr = {4,2,-3,1,6}
Output: 
Yes
Explanation: 
2, -3, 1 is the subarray with sum 0.

Example 2:
Input:
n = 5
arr = {4,2,0,1,6}
Output: 
Yes
Explanation: 
0 is one of the element in the array so there exist a subarray with sum 0.
Your Task:
You only need to complete the function subArrayExists() that takes array and n as parameters and returns true or false.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 10^4
-10^5 <= a[i] <= 10^5

"""

# SOLUTION

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        
        #Return true or false
        # Initialize a dictionary to store the running sum as keys and their occurrences as values
        temp_dict = {0: 1}
        
        # Initialize the total sum
        total = 0
        
        # Iterate through the array
        for i in range(n):
            # Update the running sum
            total += arr[i]
            
            # Check if the current running sum has been encountered before
            if total in temp_dict:
                # If yes, there exists a subarray with a sum of 0
                return True
            
            # Store the current running sum in the dictionary
            temp_dict[total] = 1
        
        # If no subarray with a sum of 0 is found
        return False
    

'''
Time Complexity:

The function iterates through the given array once using a single loop.
Inside the loop, each operation (summing elements, checking if a key exists in the dictionary, and updating the dictionary) is constant time.
Therefore, the overall time complexity is O(n), where n is the length of the input array.


Space Complexity:

The function uses a dictionary (temp_dict) to store running sums and their occurrences.
In the worst case, the dictionary could contain all unique running sums, which would be at most the length of the array.
Therefore, the space complexity is O(n), where n is the length of the input array.
'''

