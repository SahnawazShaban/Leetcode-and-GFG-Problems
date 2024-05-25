"""
42. Trapping Rain Water

Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

"""

# SOLUTION

class Solution:
    def trap(self, height: List[int]) -> int:
        # Solution - 1

        n = len(height)

        # Initialize an array to store the maximum height to the left of each element
        maxL = [0] * n
        maxL[0] = height[0]

        # Calculate the maximum height to the left for each element
        for i in range(1, n):
            maxL[i] = max(maxL[i - 1], height[i])

        # Initialize an array to store the maximum height to the right of each element
        maxR = [0] * n
        maxR[n - 1] = height[n - 1]

        # Calculate the maximum height to the right for each element
        for i in range(n - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], height[i])

        # Initialize an array to store the trapped water at each element
        water = [0] * n

        # Calculate the trapped water at each element
        for i in range(n):
            water[i] = min(maxL[i], maxR[i]) - height[i]

        # Calculate the total trapped water
        total = 0
        for i in range(n):
            total += water[i]

        # Return the total trapped water
        return total

        # Time and Space Complexity
        '''
        Time Complexity:
        The first loop, which calculates maxL, runs in O(n) time.
        The second loop, which calculates maxR, also runs in O(n) time.
        The third loop, which calculates the trapped water at each element, runs in O(n) time.
        Since each of these operations runs in linear time, the overall time complexity is O(n).

        Space Complexity:
        The maxL array and maxR array both use O(n) space because they store the maximum height to the left and right of each element.
        The water array also uses O(n) space as it stores the trapped water at each element.
        There are also some constant space variables used (e.g., n, i, total).
        Therefore, the overall space complexity is O(n).
        '''

        # ---------------------------------
        # Solution - 2

        l = 0
        r = len(height) - 1

        # Initialize variables to store the maximum height to the left and right
        ml = height[0]  
        mr = height[-1]

        # Initialize variable to store the total trapped water
        ans = 0

        # Loop until the left and right pointers meet
        while l < r:
            # Check if the height at the left pointer is smaller than the height at the right pointer
            if height[l] < height[r]:
                # If the height at the left pointer is greater than or equal to the maximum height to the left,
                # update the maximum height to the left; otherwise, calculate and add the trapped water
                if height[l] >= ml:
                    ml = height[l]
                else:
                    ans += ml - height[l]
                l += 1  # Move the left pointer to the right
            else:
                # If the height at the right pointer is greater than or equal to the maximum height to the right,
                # update the maximum height to the right; otherwise, calculate and add the trapped water
                if height[r] >= mr:
                    mr = height[r]
                else:
                    ans += mr - height[r]
                r -= 1  # Move the right pointer to the left

        # Return the total trapped water
        return ans