/*
Longest consecutive subsequence
Medium
Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
 

Example 1:
Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here are 1, 2, 3, 4, 5, 6. 
These 6 numbers form the longest consecutive subsquence.

Example 2:
Input:
N = 7
a[] = {1,9,3,10,4,20,2}
Output:
4
Explanation:
1, 2, 3, 4 is the longest consecutive subsequence.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findLongestConseqSubseq() which takes the array arr[] and the size of the array as inputs and returns the length of the longest subsequence of consecutive integers. 

Expected Time Complexity: O(R), where R is the maximum integer in the array.
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 10^5
0 <= a[i] <= 10^5

// ---------------------------------------------

128. Longest Consecutive Sequence
Medium
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
*/

// SOLUTION

class Solution {
    // arr[] : the input array
    // N : size of the array arr[]

    // Function to return length of longest subsequence of consecutive integers.
    static int findLongestConseqSubseq(int arr[], int N) {
        // Solution - 1

        Arrays.sort(arr);
        int count = 1;
        int res = 1;

        for (int i = 1; i < N; i++) {
            if (arr[i] == arr[i - 1] + 1) {
                count++;
            } else if (arr[i] != arr[i - 1]) {
                count = 1;
            }

            res = Math.max(res, count);
        }

        return res;

        // Solution - 2 - Using HashMap

        HashSet<Integer> vals = new HashSet<>();
        int ans = 0;
        for (int i = 0; i < N; i++) {
            vals.add(arr[i]);
        }

        for (int i = 0; i < N; i++) {
            if (!vals.contains(arr[i] - 1)) {
                int j = arr[i];
                while (vals.contains(j)) {
                    j++;
                }
                if (ans < j - arr[i]) {
                    ans = j - arr[i];
                }
            }
        }
        return ans;
    }
}

// .......................................

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0 || nums == null) {
            return 0;
        }

        HashSet<Integer> ms = new HashSet<>();
        int longestStreak = 0;
        int count = 1;

        for (int num : nums) {
            ms.add(num);
        }

        for (int num : nums) {
            if (!ms.contains(num - 1)) {
                int ele = num;
                count = 1;

                while (ms.contains(ele + 1)) {
                    ele++;
                    count++;
                }

                longestStreak = Math.max(longestStreak, count);
            }
        }
        return longestStreak;
    }
}

// Extra
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        // Count the frequency of each element
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        int longestStreak = 0;

        for (int num : frequencyMap.keySet()) {
            // Check if current number is the start of a sequence
            if (!frequencyMap.containsKey(num - 1)) {
                int currentNum = num;
                int currentStreak = frequencyMap.get(num);

                while (frequencyMap.containsKey(currentNum + 1)) {
                    currentNum++;
                    currentStreak += frequencyMap.get(currentNum);
                }

                longestStreak = Math.max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
}
