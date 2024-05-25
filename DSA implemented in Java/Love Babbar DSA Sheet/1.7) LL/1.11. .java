/*
189. Rotate Array
Medium
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 
Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
 

Follow up:
Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
*/

// SOLUTION

class Solution {
    public void reverse(int[] nums, int i, int j) {
        while (i < j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;

            i++;
            j--;
        }
    }

    public void rotate(int[] nums, int k) {
        // Solution - 1
        int n = nums.length;
        k = k % n;
        int[] res = new int[n];
        int j = 0;

        for (int i = n - k; i < n; i++) {
            res[j++] = nums[i];
        }

        for (int i = 0; i < n - k; i++) {
            res[j++] = nums[i];
        }

        for (int i = 0; i < n; i++) {
            nums[i] = res[i];
        }

        // --------------------------------------
        
        // Recursive approach
        int n = nums.length;
        k = k % n;

        reverse(nums, 0, n - k - 1);
        reverse(nums, n - k, n - 1);
        reverse(nums, 0, n - 1);
    }
}