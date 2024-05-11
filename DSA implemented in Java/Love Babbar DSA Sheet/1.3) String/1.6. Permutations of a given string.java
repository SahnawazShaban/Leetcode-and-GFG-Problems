/*
1.
Permutations of a given string
Medium
Given a string S. The task is to print all unique permutations of the given string that may contain dulplicates in lexicographically sorted order. 

Example 1:
Input: ABC
Output:
ABC ACB BAC BCA CAB CBA
Explanation:
Given string ABC has permutations in 6 
forms as ABC, ACB, BAC, BCA, CAB and CBA.

Example 2:
Input: ABSG
Output:
ABGS ABSG AGBS AGSB ASBG ASGB BAGS 
BASG BGAS BGSA BSAG BSGA GABS GASB 
GBAS GBSA GSAB GSBA SABG SAGB SBAG 
SBGA SGAB SGBA
Explanation:
Given string ABSG has 24 permutations.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function find_permutation() which takes the string S as input parameter and returns a vector of string in lexicographical order.

Expected Time Complexity: O(n! * n)
Expected Space Complexity: O(n! * n)

Constraints:
1 <= length of string <= 5

...............................................

2.
567. Permutation in String
Medium
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 
Constraints:
1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
*/

// SOLUTION
// 1.
class Solution {
    public void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public List<String> find_permutation(String S) {
        List<String> ans = new ArrayList<>();
        // For example, if S is "ABC", S.toCharArray() will return ['A', 'B', 'C'],
        // providing an array representation of the characters in the string.
        char[] charArray = S.toCharArray();
        backtrack(charArray, ans, 0);
        Collections.sort(ans); // Sort the list of permutations
        return ans;
    }

    public void backtrack(char[] arr, List<String> ans, int idx) {
        if (idx == arr.length - 1) {
            ans.add(new String(arr));
        } else {
            for (int i = idx; i < arr.length; i++) {
                // shouldSwap method is a helper function used to determine whether swapping two
                // characters in the permutation process should occur to avoid generating
                // duplicate permutations.
                if (shouldSwap(arr, idx, i)) {
                    swap(arr, idx, i);
                    backtrack(arr, ans, idx + 1);
                    swap(arr, idx, i); // backtrack
                }
            }
        }
    }

    // eg. ABB
    // Helper method to check if swapping is necessary to avoid duplicates
    private boolean shouldSwap(char[] arr, int start, int end) {
        for (int i = start; i < end; i++) {
            if (arr[i] == arr[end]) {
                return false;
            }
        }
        return true;
    }
}

// .........................

//2.
class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] alpha = new int[26];

        int s1_len = s1.length();
        int s2_len = s2.length();

        for (int ch = 0; ch < s1_len; ch++) {
            alpha[s1.charAt(ch) - 'a']++;
        }

        int i = 0, j = 0;

        while (j < s2_len) {
            if (alpha[s2.charAt(j) - 'a'] > 0) {
                s1_len--;
            }

            alpha[s2.charAt(j) - 'a']--;
            j++;

            if (s1_len == 0) {
                return true;
            }

            if (j - i == s1.length()) {
                if (alpha[s2.charAt(i) - 'a'] >= 0) {
                    s1_len++;
                }
                alpha[s2.charAt(i) - 'a']++;
                i++;
            }
        }
        return false;
    }
}