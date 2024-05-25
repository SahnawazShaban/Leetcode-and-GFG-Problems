/*
90. Subsets

Medium

Given an integer array nums that may contain duplicates, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

*/

// SOLUTION

/*
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Arrays.sort(nums);
        sets(nums, 0, new ArrayList<>(), res);
        return res;
    }

    private void sets(int[] nums, int idx, List<Integer> temp, List<List<Integer>> res) {
        if (idx == nums.length) {
            if (!res.contains(temp)) {
                res.add(new ArrayList<>(temp));
            }
            return;
        }

        // Include the current element
        temp.add(nums[idx]);
        sets(nums, idx + 1, temp, res);

        // Exclude the current element
        temp.remove(temp.size() - 1);
        sets(nums, idx + 1, temp, res);
    }
}

*/

class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
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

        ds.add(nums[idx]);
        backtrack(nums, ans, ds, idx+1);

        while (idx+1 < nums.length && nums[idx] == nums[idx+1]){
            idx++;
        }

        ds.remove(ds.size()-1);
        backtrack(nums, ans, ds, idx+1);
        
    }
}
        


/*
Recursive Calls:
Each element has two choices: either to be included in the current subset or to be excluded.
Therefore, the total number of recursive calls is 2^n for n elements.

Handling Duplicates:
Before adding a subset to the result, the algorithm checks if the subset already exists in the result using res.contains(temp).
In the worst case, this check can take O(k) time, where k is the number of subsets generated. However, because this is inside a recursive call, the overall complexity is affected.

Subset Generation:
Each subset can be copied in O(n) time, as copying a list of n elements takes O(n) time.
Combining these, the total time complexity is O(2^n * n). This is because there are 2^n subsets, and each subset can take up to O(n) time to be created and checked for duplicates.

Space Complexity:
The space complexity includes both the space used by the recursive stack and the space required to store the subsets.

Recursive Stack:
The depth of the recursion is n, so the space used by the recursive stack is O(n).

Storage for Subsets:
There are 2^n subsets, and each subset can contain up to n elements.
Therefore, the space required to store all subsets is O(n * 2^n).
Combining these, the overall space complexity is O(n * 2^n).

Summary:
Time Complexity: O(2^n * n)
Space Complexity: O(n * 2^n)
These complexities reflect the exponential growth in the number of subsets generated, which is inherent to the problem of generating all subsets (power set) of a given set.
*/