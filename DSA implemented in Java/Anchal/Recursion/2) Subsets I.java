/*
78. Subsets

Medium

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
 
*/

// SOLUTION

class Solution {
    // Solution - 1
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(nums, ans, ds, 0);

        return ans;
    }

    public void backtrack(int[] nums, List<List<Integer>> ans, List<Integer> ds, int idx){
        if (idx >= nums.length){
            ans.add(new ArrayList<>(ds));
            return;
        }

        ds.add(nums[idx]); // take ith element
        backtrack(nums, ans, ds, idx+1);
        ds.remove(ds.size()-1);
        backtrack(nums, ans, ds, idx+1);
    }
}

/* 
import java.util.*;

public class Subsets {

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        List<Integer> ds = new ArrayList<>();
        Arrays.sort(nums); // Sorting is not necessary for generating subsets, but can be useful for consistency
        backtrack(nums, ans, ds, 0);
        return ans;
    }

    public void backtrack(int[] nums, List<List<Integer>> ans, List<Integer> ds, int idx) {
        // Always add the current subset to the answer list
        ans.add(new ArrayList<>(ds));
        
        for (int i = idx; i < nums.length; i++) {
            ds.add(nums[i]); // Take the element at index i
            backtrack(nums, ans, ds, i + 1); // Move to the next element
            ds.remove(ds.size() - 1); // Remove the element before moving to the next iteration
        }
    }

    public static void main(String[] args) {
        Subsets subsets = new Subsets();
        int[] nums = {1, 2, 3};
        List<List<Integer>> result = subsets.subsets(nums);
        for (List<Integer> subset : result) {
            System.out.println(subset);
        }
    }
}
*/