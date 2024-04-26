/*
Count More than n/k Occurences
Easy
Given an array arr of size N and an element k. The task is to find the count of elements in the array that appear more than n/k times.

Example 1:
Input:
N = 8
arr = [3,1,2,2,1,2,3,3]
k = 4
Output: 
2
Explanation: 
In the given array, 3 and 2 are the only elements that appears more than n/k times.

Example 2:
Input:
N = 4
arr = [2,3,3,2]
k = 3
Output: 
2
Explanation: In the given array, 3 and 2 are the only elements that appears more than n/k times. So the count of elements are 2.
Your Task:
The task is to complete the function countOccurence() which returns count of elements with more than n/k times appearance.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 10^5
1 <= a[i] <= 10^9
1 <= k <= N
*/

// SOLUTION

class Solution {
    // Function to find all elements in array that appear more than n/k times.
    public int countOccurence(int[] arr, int n, int k) {
        // Brute Force
        int max = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            max = Math.max(max, arr[i]);
        }

        int temp[] = new int[max + 1];
        for (int i = 0; i < n; i++) {
            temp[arr[i]]++;
        }

        for (int i = 0; i < temp.length; i++) {
            if (temp[i] > (n / k)) {
                count++;
            }
        }
        return count;

        // Optimal
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int val : arr) {
            hm.put(val, hm.getOrDefault(val, 0) + 1);
        }

        int count = 0;
        for (int val : hm.keySet()) {
            if (hm.get(val) > (n / k)) {
                count++;
            }
        }

        // extra
        for (int val : hm.values()) {
            if (val > (n / k)) {
                count++;
            }
        }

        return count;
    }
}
