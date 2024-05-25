/*
283. Move Zeroes
Easy
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 

Constraints:
1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 
Follow up: Could you minimize the total number of operations done?
*/

// SOLUTION

class Solution {
    public void moveZeroes(int[] nums) {
        // Solution - 1
        /*
         * int j = 0;
         * 
         * for (int i = 0; i < nums.length; i++){
         * if (nums[i] != 0){
         * nums[j++] = nums[i];
         * }
         * }
         * 
         * while (j < nums.length){
         * nums[j++] = 0;
         * }
         */

        // Solution - 2 - The number of steps is decreasing, but the answer is not in a
        // sorted order.
        int n = nums.length;

        int j = n - 1;

        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                continue;
            }

            if (i < j) {
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                j--;
            }
        }
    }
}
