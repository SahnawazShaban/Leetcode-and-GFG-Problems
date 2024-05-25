/*
Smallest window containing 0, 1 and 2
Easy
Given a string S consisting of the characters 0, 1 and 2. Your task is to find the length of the smallest substring of string S that contains all the three characters 0, 1 and 2. If no such substring exists, then return -1.

Example 1:
Input:
S = 10212
Output:
3
Explanation:
The substring 102 is the smallest substring that contains the characters 0, 1 and 2.

Example 2:
Input: 
S = 12121
Output:
-1
Explanation: 
As the character 0 is not present in the
string S, therefor no substring containing
all the three characters 0, 1 and 2
exists. Hence, the answer is -1 in this case.
Your Task:
Complete the function smallestSubstring() which takes the string S as input, and returns the length of the smallest substring of string S that contains all the three characters 0, 1 and 2.

Expected Time Complexity: O( length( S ) )
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ length( S ) ≤ 10^5
All the characters of String S lies in the set {'0', '1', '2'}

Company Tags:
Paytm
*/

// SOLUTION

class Solution {
    public int smallestSubstring(String S) {
        int n = S.length();
        int[] ans = { 0, 0, 0 };
        int count = 0;

        int i = 0, j = 0;
        int result = Integer.MAX_VALUE;

        while (i < n) {

            if (S.charAt(i) == '0') {
                ans[0]++;
            } else if (S.charAt(i) == '1') {
                ans[1]++;
            } else {
                ans[2]++;
            }

            while (ans[0] > 0 && ans[1] > 0 && ans[2] > 0 && i - j + 1 >= 3) {
                result = Math.min(result, i - j + 1);

                if (S.charAt(j) == '0') {
                    ans[0]--;
                } else if (S.charAt(j) == '1') {
                    ans[1]--;
                } else {
                    ans[2]--;
                }

                j++;
            }
            i++;
        }
        return result == Integer.MAX_VALUE ? -1 : result;
    }
};