/*
Longest Sub-Array with Sum K
Medium
Given an array containing N integers and an integer K., Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.


Example 1:
Input :
A[] = {10, 5, 2, 7, 1, 9}
K = 15
Output : 4
Explanation:
The sub-array is {5, 2, 7, 1}.

Example 2:
Input : 
A[] = {-1, 2, 3}
K = 6
Output : 0
Explanation: 
There is no such sub-array with sum 6.
Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function lenOfLongSubarr() that takes an array (A), sizeOfArray (n),  sum (K)and returns the required length of the longest Sub-Array. The driver code takes care of the printing.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1<=N<=10^5
-10^5<=A[i], K<=10^5
*/

// SOLUTION

class Solution {
    // Function for finding maximum and value pair
    public static int lenOfLongSubarr(int A[], int N, int K) {
        // Solution - 1 - 0(n^2)

        int sum = 0, ans = Integer.MIN_VALUE;

        for (int i = 0; i < N; i++) {
            sum = 0;
            for (int j = i; j < N; j++) {
                sum += A[j];

                if (sum == K) {
                    ans = Math.max(ans, j - i + 1);
                }
            }
        }
        return ans;

        // --------------------------------------------------------

        // Solution - 2 - O(n)
        int preSum = 0;
        int maxLen = 0;
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int i = 0; i < N; i++) {
            preSum += A[i];

            if (preSum == K) {
                maxLen = Math.max(maxLen, i + 1);
            }

            int diff = preSum - K;

            if (hm.containsKey(diff)) {
                maxLen = Math.max(maxLen, i - hm.get(diff));
            }

            if (!hm.containsKey(preSum)) {
                hm.put(preSum, i);
            }
        }
        return maxLen;
    }
}

/*
 * Let's revisit the time and space complexity analysis for the line if
 * (hm.containsKey(diff)):
 * 
 * Time Complexity:
 * 
 * The containsKey() operation in a HashMap has an average-case time complexity
 * of O(1). This is because, in a well-distributed hash table, the average time
 * to look up an element is constant regardless of the number of elements in the
 * map.
 * 
 * However, in the worst-case scenario, when there are many hash collisions or
 * the load factor is high, all keys might end up in the same bucket, making the
 * lookup operation linear in the number of elements in that bucket. In such a
 * case, the time complexity could degrade to O(n), where n is the number of
 * elements in the bucket.
 * 
 * Yet, for most practical cases, assuming a good hashing function and a
 * reasonably low load factor, the average-case time complexity remains O(1).
 * 
 * 
 * Space Complexity:
 * 
 * The space complexity for the HashMap hm is O(N), where N is the number of
 * distinct prefix sums encountered while iterating through the input array A.
 * This is because the HashMap may store at most N distinct prefix sums and
 * their corresponding indices.
 * Additionally, other variables like preSum, maxLen, and loop variables (i)
 * contribute only a constant amount of space and do not depend on the input
 * size.
 * 
 * 
 * Overall:
 * 
 * Time Complexity: O(1) on average, with a worst-case scenario of O(n) due to
 * hash collisions.
 * Space Complexity: O(N), where N is the number of distinct prefix sums
 * encountered while iterating through the input array.
 */