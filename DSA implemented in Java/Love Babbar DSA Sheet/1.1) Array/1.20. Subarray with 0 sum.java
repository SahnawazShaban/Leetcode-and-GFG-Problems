/*
Subarray with 0 sum
Medium
Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. You just need to return true/false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the driver code.

Example 1:
Input:
n = 5
arr = {4,2,-3,1,6}
Output: 
Yes
Explanation: 
2, -3, 1 is the subarray with sum 0.

Example 2:
Input:
n = 5
arr = {4,2,0,1,6}
Output: 
Yes
Explanation: 
0 is one of the element in the array so there exist a subarray with sum 0.
Your Task:
You only need to complete the function subArrayExists() that takes array and n as parameters and returns true or false.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= n <= 104
-10^5 <= a[i] <= 10^5
*/

// SOLUTION

class Solution {
    // Function to check whether there is a subarray present with 0-sum or not.
    static boolean findsum(int arr[], int n) {
        // Solution - 1
        int sum = 0;
        int ans = 0;

        HashMap<Integer, Integer> mp = new HashMap<>();

        for (int i = 0; i < n; i++) {
            sum += arr[i];
            if (sum == 0) {
                ans++;
            }

            if (mp.containsKey(sum)) {
                ans += mp.get(sum);
            }

            if (!mp.containsKey(sum)) {
                mp.put(sum, 0);
            }

            mp.put(sum, mp.get(sum) + 1);
        }

        return ans >= 1;

        // ..............................................

        // Solution - 2
        int ans = 0;
        int prefixSum = 0;
        HashMap<Integer, Integer> mp = new HashMap<>();
        mp.put(0, 1);

        for (int i = 0; i < n; i++) {
            prefixSum += arr[i];

            if (mp.containsKey(prefixSum)) {
                ans += mp.get(prefixSum);
            }

            mp.put(prefixSum, mp.getOrDefault(prefixSum, 0) + 1);
        }
        return ans >= 1;
    }
}
