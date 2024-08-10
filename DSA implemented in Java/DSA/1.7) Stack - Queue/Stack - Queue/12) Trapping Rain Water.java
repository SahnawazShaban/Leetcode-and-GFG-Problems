/*
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
*/

// SOLUTION

// Solution 1: Using Arrays to Track Maximum Heights

import java.util.List;

public class Solution {
    public int trap(int[] height) {
        int n = height.length;

        // Initialize arrays to store the maximum height to the left and right of each element
        int[] maxL = new int[n];
        int[] maxR = new int[n];

        // Calculate the maximum height to the left for each element
        maxL[0] = height[0];
        for (int i = 1; i < n; i++) {
            maxL[i] = Math.max(maxL[i - 1], height[i]);
        }

        // Calculate the maximum height to the right for each element
        maxR[n - 1] = height[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            maxR[i] = Math.max(maxR[i + 1], height[i]);
        }

        // Calculate the total trapped water
        int total = 0;
        for (int i = 0; i < n; i++) {
            total += Math.min(maxL[i], maxR[i]) - height[i];
        }

        return total;
    }
}

// Solution 2: Using Two Pointers

public class Solution {
    public int trap(int[] height) {
        int l = 0;
        int r = height.length - 1;
        
        // Initialize variables to store the maximum height to the left and right
        int ml = height[0];
        int mr = height[height.length - 1];
        
        // Initialize variable to store the total trapped water
        int ans = 0;
        
        // Loop until the left and right pointers meet
        while (l < r) {
            // Check if the height at the left pointer is smaller than the height at the right pointer
            if (height[l] < height[r]) {
                // If the height at the left pointer is greater than or equal to the maximum height to the left,
                // update the maximum height to the left; otherwise, calculate and add the trapped water
                if (height[l] >= ml) {
                    ml = height[l];
                } else {
                    ans += ml - height[l];
                }
                l++;  // Move the left pointer to the right
            } else {
                // If the height at the right pointer is greater than or equal to the maximum height to the right,
                // update the maximum height to the right; otherwise, calculate and add the trapped water
                if (height[r] >= mr) {
                    mr = height[r];
                } else {
                    ans += mr - height[r];
                }
                r--;  // Move the right pointer to the left
            }
        }
        
        return ans;
    }
}
