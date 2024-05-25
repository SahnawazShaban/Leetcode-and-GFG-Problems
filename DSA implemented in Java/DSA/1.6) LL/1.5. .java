/*
136. Single Number
Easy
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
 
Constraints:
1 <= nums.length <= 3 * 10^4
-3 * 104 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.
*/

// SOLUTION

class Solution {
    public int singleNumber(int[] nums) {
        // Using XOR operation
        /*
         * int ans = nums[0];
         * 
         * for (int i = 1; i < nums.length; i++){
         * ans ^= nums[i];
         * }
         * 
         * return ans;
         */

        HashSet<Integer> hm = new HashSet<>();

        for (int val : nums) {
            if (hm.contains(val)) {
                hm.remove(val);
            } else {
                hm.add(val);
            }
        }

        for (int ele : hm) {
            return ele;
        }

        return -1;
    }
}
