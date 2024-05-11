/*
387. First Unique Character in a String
Easy
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.

*/

//SOLUTION

class Solution {
    public int firstUniqChar(String s) {
        //Solution - 1
        int[] count = new int[26];

        int n = s.length();
        int j = 0;

        for (int i = 0; i < n; i++) {
            count[s.charAt(i) - 'a']++;

            while (j <= i && count[s.charAt(j) - 'a'] > 1) {
                j++;
            }
        }
        return j == n ? -1 : j;

        // -----------------------------------

        //Solution - 2
        int freq[] = new int[26];
        for (int i = 0; i < s.length(); i++)
            freq[s.charAt(i) - 'a']++;
        for (int i = 0; i < s.length(); i++)
            if (freq[s.charAt(i) - 'a'] == 1)
                return i;
        return -1;
    }
}