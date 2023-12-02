"""
3. Check If N and Its Double Exist
Easy
Given an array of integers arr, check if there exists two distinct indices i and j such that arr[i] == 2 * arr[j].

Example 1:
Input
4
10 2 5 3

Output
True

Explaination:

In the given example, arr[0] = 10 and arr[2] = 5, which satisfy the condition 10 == 2 * 5.

Constraints:

2 <= n <= 500
-10^3<= arr[i] <= 10^3
Input Format:

An integer array arr of length n.

Output Format:

A boolean value indicating whether such two distinct indices exist.

"""


# Solution 

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Solution - 1
        set1 = set()

        for num in arr:
            if num == 0 and 0 in set1:
                return True

            temp_double = num * 2
            temp_half = num // 2 if num % 2 == 0 else None

            if temp_double in set1 or temp_half in set1:
                return True

            set1.add(num)

        return False
    
        '''
        # Solution - 2

        seen = set()

        for num in arr:
            # Check if either the double or half of the current number is in the set
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            
            # Add the current number to the set
            seen.add(num)

        return False
        '''

