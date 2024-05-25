/*
3. Longest Substring Without Repeating Characters
Medium
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:
0 <= s.length <= 5 * 10^4
*/

// SOLUTION

class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Brute Force
        int n = s.length();
        if (s == null || n == 0) {
            return 0;
        }

        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; i++) {
                if (uniqueElement(s, i, j)) {
                    ans = Math.max(ans, j - i);
                }
            }
        }
        return ans;
    }

    public boolean uniqueElement(String s, int start, int end) {
        Set<Character> st = new HashSet<>();

        for (int i = start; i < end; i++) {
            char ch = s.charAt(i);
            if (st.contains(ch)) {
                return false;
            }
            st.add(ch);
        }
        return true;

        // Brute Force:
        // Time Complexity: O(n^3)
        // Space Complexity: O(n)

        // -------------------------------------
        // Better
        int n = s.length();
        int maxLength = 0;
        Set<Character> charSet = new HashSet<>();
        int left = 0;

        for (int right = 0; right < n; right++) {
            if (!charSet.contains(s.charAt(right))) {
                charSet.add(s.charAt(right));
                maxLength = Math.max(maxLength, right - left + 1);
            } else {
                while (charSet.contains(s.charAt(right))) {
                    charSet.remove(s.charAt(left));
                    left++;
                }
                charSet.add(s.charAt(right));
            }
        }

        return maxLength;

        // Better:
        // Time Complexity: O(n)
        // Space Complexity: O(min(n,m)) where m is the size of the character set

        // -------------------------------------
        // Optimal

        HashMap<Character, Integer> hm = new HashMap<>();

        int n = s.length();
        int l = 0, r = 0;
        int result = 0;

        while (r < n) {
            char ch = s.charAt(r);
            if (hm.containsKey(ch)) {
                l = Math.max(l, hm.get(ch) + 1);
            }

            result = Math.max(result, r - l + 1);
            hm.put(s.charAt(r), r);
            r++;
        }
        return result;

        // Optimal (HashMap):
        // Time Complexity: O(n)
        // Space Complexity: O(m) where m is the size of the character set

        // -------------------------------------
        // Optimal

        int n = s.length();
        int maxLength = 0;
        int[] charIndex = new int[128];

        // Arrays.fill(charIndex, -1);
        for (int i = 0; i < charIndex.length; i++) {
            charIndex[i] = -1;
        }

        int left = 0;

        for (int right = 0; right < n; right++) {
            if (charIndex[s.charAt(right)] >= left) {
                left = charIndex[s.charAt(right)] + 1;
            }
            charIndex[s.charAt(right)] = right;
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;

        // Optimal (Array):
        // Time Complexity: O(n)
        // Space Complexity: O(m) where m is the size of the character set
    }
}

// Brute Force:
// Time Complexity: O(n^3)
// Space Complexity: O(n)

// Better:
// Time Complexity: O(n)
// Space Complexity: O(min(n,m)) where m is the size of the character set

// Optimal (HashMap):
// Time Complexity: O(n)
// Space Complexity: O(m) where m is the size of the character set

// Optimal (Array):
// Time Complexity: O(n)
// Space Complexity: O(m) where m is the size of the character set

// In summary, all solutions have linear time complexity, but their space
// complexities differ based on how they handle unique characters. The "Better"
// solution is the most efficient in terms of space when the character set is
// small, while the "Optimal (HashMap)" and "Optimal (Array)" solutions are
// preferred when dealing with larger character sets.
