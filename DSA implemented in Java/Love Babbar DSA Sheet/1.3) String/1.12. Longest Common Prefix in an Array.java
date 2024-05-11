/*
Longest Common Prefix in an Array
Easy
Given an array of N strings, find the longest common prefix among all strings present in the array.

Example 1:
Input:
N = 4
arr[] = {geeksforgeeks, geeks, geek, geezer}
Output: gee
Explanation: "gee" is the longest common prefix in all the given strings.

Example 2:
Input: 
N = 2
arr[] = {hello, world}
Output: -1
Explanation: There's no common prefix in the given strings.

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestCommonPrefix() which takes the string array arr[] and its size N as inputs and returns the longest common prefix common in all the strings in the array. If there's no prefix common in all the strings, return "-1".


Expected Time Complexity: O(N*min(|arri|)).
Expected Auxiliary Space: O(min(|arri|)) for result.


Constraints:
1 ≤ N ≤ 10^3
1 ≤ |arri| ≤ 10^3
*/

// SOLUTION

class Solution {
    String longestCommonPrefix(String arr[], int n) {
        // with inbuild function
        int minLen = Integer.MAX_VALUE;
        String res = "";

        for (int i = 0; i < n; i++)
            minLen = Math.min(minLen, arr[i].length());

        for (int i = 0; i < minLen; i++) {

            char it = arr[0].charAt(i);
            int flag = 0;

            for (int j = 0; j < n; j++) {
                char ch = arr[j].charAt(i);
                if (ch != it) {
                    flag = 1;
                    break;
                }
            }

            if (flag == 1) {
                if (res.length() == 0)
                    return "-1";
                else
                    return res;
            } else
                res += it;
        }

        return res;

        // -------------------------------------

        // Using inbuild function
        String result = arr[0];
        for (int i = 1; i < n; i++) {
            while (arr[i].indexOf(result) != 0) {
                result = result.substring(0, result.length() - 1);
                if (result.isEmpty()) {
                    return "-1";
                }
            }
        }
        return result;
    }
}
