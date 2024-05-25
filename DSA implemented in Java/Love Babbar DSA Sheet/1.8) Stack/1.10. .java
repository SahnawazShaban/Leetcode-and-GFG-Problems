/*
 * Search Pattern (Rabin-Karp Algorithm)
 * Medium
 * Given two strings, one is a text string and other is a pattern string. The
 * task is to print the indexes of all the occurences of pattern string in the
 * text string. For printing, Starting Index of a string should be taken as 1.
 * The strings will only contain lowercase English alphabets ('a' to 'z').
 * 
 * Example 1:
 * Input:
 * text = "birthdayboy"
 * pattern = "birth"
 * Output:
 * [1]
 * Explanation:
 * The string "birth" occurs at index 1 in text.
 * 
 * Example 2:
 * Input:
 * text = "geeksforgeeks"
 * pattern = "geek"
 * Output:
 * [1, 9]
 * Explanation:
 * The string "geek" occurs twice in text, one starts are index 1 and the other
 * at index 9.
 * Your Task:
 * You don't need to read input or print anything. Your task is to complete the
 * function search() which takes the string text and the string pattern as input
 * and returns an array denoting the start indices (1-based) of substring
 * pattern in the string text.
 * 
 * Expected Time Complexity: O(|text| + |pattern|).
 * Expected Auxiliary Space: O(1).
 * 
 * Constraints:
 * 1<=|text|<=5*10^5
 * 1<=|pattern|<=|text|
 */

// SOLUTION

class Solution {

    ArrayList<Integer> search(String pattern, String text) {
        ArrayList<Integer> ans = new ArrayList<>();

        int n = text.length();
        int m = pattern.length();

        for (int i = 0; i < n - m + 1; i++) {
            if (text.substring(i, i + m).equals(pattern)) {
                ans.add(i + 1);
            }
        }
        return ans;
    }
}

// Time Complexity:
// The outer loop iterates n - m + 1 times, where n is the length of the text
// string and m is the length of the pattern string. This is because we iterate
// until n - m to ensure that we don't go out of bounds when extracting
// substrings of length m.
// Inside the loop, the equals() method is used to compare substrings of length
// m, which has a time complexity of O(m).
// Therefore, the overall time complexity of the method is O((n - m + 1) * m).

// Space Complexity:
// The space complexity is mainly determined by the ArrayList<Integer> ans,
// which stores the indices where the pattern occurs.
// The space complexity of the ans ArrayList is O(k), where k is the number of
// occurrences of the pattern in the text. In the worst case, where the pattern
// occurs at every possible position in the text, k would be (n - m + 1).
// Additionally, there are constant space requirements for variables n, m, i,
// and the pattern and text strings.
// Therefore, the overall space complexity is O(k).