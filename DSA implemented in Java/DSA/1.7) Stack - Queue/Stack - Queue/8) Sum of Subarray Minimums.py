"""
907. Sum of Subarray Minimums

Medium

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.


Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4

"""

# SOLUTION

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Add sentinel values to the array to handle edge cases
        arr = [-math.inf] + arr + [-math.inf]
        n = len(arr)
        st = []  # Monotonic stack to track indices
        res = 0  # Variable to store the final result

        # Traverse the array
        for i in range(n):
            # While the stack is not empty and the current element is less than the element at the top of the stack
            while st and arr[st[-1]] > arr[i]:
                mid = st.pop()  # Pop the top of the stack
                left = st[-1]  # The left boundary of the subarray
                right = i  # The right boundary of the subarray

                # Calculate the contribution of the popped element to the result
                # The contribution is the product of the value of the popped element,
                # the distance between the popped element and the element to its left,
                # and the distance between the popped element and the current element.
                res += (arr[mid] * (mid - left) * (right - mid))
            
            st.append(i)  # Push the current index onto the stack
        
        # Return the result modulo 10^9 + 7
        return res % (10**9 + 7)

        # -----------------------------------------------

        # Explanation
        '''
        Sentinel Values: The code adds -math.inf to both ends of the array to ensure that there are always smaller elements for every element, avoiding edge cases when checking for the minimum value.

        Monotonic Stack: The stack (st) is used to keep track of indices in a way that maintains a non-increasing order of values. This is essential for efficiently calculating the contribution of each element to the final result.

        Traversal: The code iterates through the array, and for each element, it checks the stack. If the current element is smaller than the element at the top of the stack, it means we've found a smaller element, and we need to process it.

        Contribution Calculation: For each popped element, the code calculates its contribution to the result based on the subarray formed by the popped element, the element to its left in the stack, and the current element. The contribution is the product of the value of the popped element and the distances mentioned.

        Modulo Operation: Finally, the result is returned modulo 10^9 + 7 to prevent overflow and meet the problem requirements.


        # -----------------
        ________________
        Time Complexity:
        ________________
        The time complexity of the algorithm is O(n), where n is the length of the input array arr.

        The for loop iterates through each element of the array exactly once. Inside the loop, the while loop may pop elements from the stack, but each index is pushed onto the stack at most once. Therefore, the total number of operations across all iterations is proportional to the length of the array.

        _________________
        Space Complexity:
        _________________
        The space complexity of the algorithm is O(n), where n is the length of the input array arr.

        Stack Space: The space used by the stack (st) is at most n, as each index is pushed onto the stack once and popped once.

        Sentinel Values: The sentinel values do not add to the space complexity since they are part of the original array.

        Other Variables: Other variables (res, n, i, left, right, mid) use a constant amount of space.

        Therefore, the overall space complexity is determined by the size of the stack, leading to a linear space complexity in terms of the input size.

        In summary:

        Time Complexity: O(n)
        Space Complexity: O(n)

        '''

