/*
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
*/

// SOLUTION

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
