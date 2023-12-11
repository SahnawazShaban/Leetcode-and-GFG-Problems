"""
1287. Element Appearing More Than 25% In Sorted Array

Easy

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.


Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5

"""


# Solution 

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # Solution - 1
        
        n = len(arr)
        quater = (n//4)+1

        temp_dict = {}

        for val in arr:
            temp_dict[val] = temp_dict.get(val, 0)+1
        
        maxi_count = 0
        result = 0
        for key, count in temp_dict.items():
            if count >= quater:
                maxi_count = count
                result = key

        return result
        

        # Solution - 2
        '''
        n = len(arr)
        if n == 1:
            return 1

        i, j = 0, 0
        res = 0
        maxi = 0 # maxi store window length of the maximum number of array

        for k in range(n-1):
            if arr[j] == arr[j+1]:
                j += 1
                # maxi = max(maxi, j-i+1)
                # res = arr[j]
                if maxi < j-i+1:
                    maxi = j-i+1
                    res = arr[j]
            else:
                j += 1
                i = j

        return res
        '''

        # Solution - 3
        '''
        n = len(arr)
        quarter = n // 4

        for i in range(n - quarter):
            if arr[i] == arr[i + quarter]:
                return arr[i]
        '''
