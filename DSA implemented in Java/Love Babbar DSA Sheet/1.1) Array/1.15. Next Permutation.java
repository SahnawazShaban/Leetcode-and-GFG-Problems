/*
31. Next Permutation
Medium
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
 
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
*/

// SOLUTION

class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int k = n - 2;

        if (n == 0 || nums == null) {
            return;
        }

        for (int i = n - 1; i > 0; i--) {
            if (nums[i] <= nums[i - 1]) {
                k--;
            } else {
                break;
            }
        }

        if (k == -1) {
            reverse(nums, 0, n - 1);
            return;
        }

        for (int i = n - 1; i > 0; i--) {
            if (nums[k] < nums[i]) {
                int temp = nums[k];
                nums[k] = nums[i];
                nums[i] = temp;
                break;
            }
        }

        reverse(nums, k + 1, n - 1);
    }

    void reverse(int[] nums, int start, int end) {
        while (start < end) {
            int temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;

            start++;
            end--;
        }
    }
}

// GFG

class Solution {
    static void reverse(int[] arr, int i, int j) {
        while (i < j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

            i++;
            j--;
        }
    }

    static List<Integer> nextPermutation(int N, int arr[]) {

        int k = N - 2;

        List<Integer> res = new ArrayList<>();

        for (int i = N - 1; i > 0; i--) {
            if (arr[i] <= arr[i - 1]) {
                k--;
            } else {
                break;
            }
        }

        if (k == -1) {
            reverse(arr, 0, N - 1);

            for (int i = 0; i < N; i++) {
                res.add(arr[i]);
            }
            return res;
        }

        for (int i = N - 1; i > 0; i--) {
            if (arr[k] < arr[i]) {
                int temp = arr[k];
                arr[k] = arr[i];
                arr[i] = temp;
                break;
            }
        }
        reverse(arr, k + 1, N - 1);

        for (int i = 0; i < N; i++) {
            res.add(arr[i]);
        }

        return res;
    }
}
