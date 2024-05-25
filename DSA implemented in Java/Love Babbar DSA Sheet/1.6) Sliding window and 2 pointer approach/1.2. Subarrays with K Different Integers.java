/*
992. Subarrays with K Different Integers
Hard
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.


Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:
1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length
*/

// SOLUTION

class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        return atMostK(A, K) - atMostK(A, K - 1);
    }

    int atMostK(int[] A, int K) {
        int i = 0, res = 0;
        int n = A.length;
        int r = 0, l = 0;
        Map<Integer, Integer> map = new HashMap<>();
        while (r < n) {
            map.put(A[r], map.getOrDefault(A[r], 0) + 1);

            while (map.size() > K) {
                map.put(A[l], map.getOrDefault(A[l], 0) - 1);
                if (map.get(A[l]) == 0) {
                    map.remove(A[l]);
                }
                l++;
            }
            res += r - l + 1;
            r++;
        }
        return res;
    }
}
