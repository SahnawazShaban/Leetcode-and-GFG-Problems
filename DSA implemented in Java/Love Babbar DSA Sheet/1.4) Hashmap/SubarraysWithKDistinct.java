/*
Search an element in sorted and rotated array
Easy
Given a sorted and rotated array A of N distinct elements which are rotated at some point, and given an element K. The task is to find the index of the given element K in array A.

Example 1:
Input:
N = 9
A[] = {5,6,7,8,9,10,1,2,3}
K = 10
Output: 5
Explanation: 10 is found at index 5.

Example 2:
Input:
N = 3
A[] = {3,1,2}
K = 1
Output: 1
User Task:
Complete Search() function and return the index of the element K if found in the array. If the element is not present, then return -1.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 10^7
0 ≤ Ai ≤ 10^8
1 ≤ K ≤ 10^8
*/

// SOLUTION
import java.util.*;

class SubarraysWithKDistinct {
    static int subarraysWithKDistinctBetter(int[] nums, int k) {
        int count = 0;
        int windowStart = 0;
        HashMap<Integer, Integer> charFreq = new HashMap<>();
        for (int windowEnd = 0; windowEnd < nums.length; windowEnd++) {
            charFreq.put(nums[windowEnd], charFreq.getOrDefault(nums[windowEnd], 0) + 1);
            while (charFreq.size() > k) {
                charFreq.put(nums[windowStart], charFreq.get(nums[windowStart]) - 1);
                if (charFreq.get(nums[windowStart]) == 0) {
                    charFreq.remove(nums[windowStart]);
                }
                windowStart++;
            }
            if (charFreq.size() == k) {
                count += windowEnd - windowStart + 1;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int[] nums = {1,2,1,3,4};

        int ans = subarraysWithKDistinctBetter(nums, 3);

        System.out.println(ans);
    }

}
