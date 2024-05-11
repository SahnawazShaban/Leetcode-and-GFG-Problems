/*
41. First Missing Positive
Hard
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
*/

// SOLUTION

class Solution {
    //Solution-1 - Brute Force
    
    public int firstMissingPositive(int[] nums) {
        int count = 1;
        for (int i = 0; i < nums.length; i++){
            if (!contains(nums, count)){
                return count;
            }
            else{
                count++;
            }
        }
        return count;
    }

    public boolean contains(int[] nums, int target) {
        for (int val : nums){
            if (val == target){
                return true;
            }
        }
        return false;
    }
    

    // Space Complexity : O(n)
    // Time Complexity : O(n)
    // Solution - 2 - Better
    public int firstMissingPositive(int[] nums){
        HashSet<Integer> hs = new HashSet<>();

        for (int val : nums){
            hs.add(val);
        }

        int i = 0;
        for (i = 1; i <= nums.length; i++){
            if (!hs.contains(i)){
                return i;
            }
        }
        return i;
        //hashset approach takes tc O(n) also space O(n) worst case
    }
    

    // Solution - 3 - Optimal
    // first learn cyclic sort
    public int firstMissingPositive(int[] nums){
        int n = nums.length;
        
        // Use cycle sort to place positive elements smaller than n
        // at the correct index
        int i = 0;
        while (i < n) {
            int correctIdx = nums[i] - 1;
            if (nums[i] > 0 && nums[i] <= n && nums[i] != nums[correctIdx]) {
                swap(nums, i, correctIdx);
            } else {
                i++;
            }
        }

        // Iterate through nums
        // return smallest missing positive integer
        for (i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        // If all elements are at the correct index
        // the smallest missing positive number is n + 1
        return n + 1;
    }

    // Swaps two elements in nums
    private void swap(int[] nums, int index1, int index2) {
        int temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
    }
}