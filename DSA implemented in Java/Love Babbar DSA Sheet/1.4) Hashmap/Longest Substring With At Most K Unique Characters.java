/*
Longest Substring With At Most K Unique Characters

Summary
Brute Force Approach:
Time Complexity: O(n^3)
Space Complexity: O(n)

Optimal Approach:
Time Complexity: O(n)
Space Complexity: O(k)
*/

// SOLUTION

// Brute Force Approach

/*
import java.util.HashSet;
import java.util.Set;

public class LongestSubstringWithKUniqueCharacters {

    public static String longestSubstringWithAtMostKUniqueCharsBruteForce(String s, int k) {
        int n = s.length();
        String longestSubstr = "";

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                String substr = s.substring(i, j);
                if (hasAtMostKUniqueChars(substr, k) && substr.length() > longestSubstr.length()) {
                    longestSubstr = substr;
                }
            }
        }
        return longestSubstr;
    }

    private static boolean hasAtMostKUniqueChars(String s, int k) {
        Set<Character> uniqueChars = new HashSet<>();
        for (char c : s.toCharArray()) {
            uniqueChars.add(c);
        }
        return uniqueChars.size() <= k;
    }

    public static void main(String[] args) {
        String s = "eceba";
        int k = 2;
        System.out.println("Brute Force Approach: " + longestSubstringWithAtMostKUniqueCharsBruteForce(s, k)); // Output: "ece"
    }
}
*/

//Optimal Approach

import java.util.HashMap;
import java.util.Map;

public class LongestSubstringWithKUniqueCharacters {

    public static String longestSubstringWithExactKUniqueCharsOptimal(String s, int k) {
        int n = s.length();
        if (n == 0 || k == 0) return "";

        Map<Character, Integer> charCountMap = new HashMap<>();
        int maxLen = 0, left = 0;
        String longestSubstr = "";

        for (int right = 0; right < n; right++) {
            char c = s.charAt(right);
            charCountMap.put(c, charCountMap.getOrDefault(c, 0) + 1);

            while (charCountMap.size() > k) {
                char leftChar = s.charAt(left);
                charCountMap.put(leftChar, charCountMap.get(leftChar) - 1);
                if (charCountMap.get(leftChar) == 0) {
                    charCountMap.remove(leftChar);
                }
                left++;
            }

            if (charCountMap.size() == k && right - left + 1 > maxLen) {
                maxLen = right - left + 1;
                longestSubstr = s.substring(left, right + 1);
            }
        }
        return longestSubstr;
    }

    public static void main(String[] args) {
        String s = "eceba";
        int k = 2;
        System.out.println("Optimal Approach (Exactly K): " + longestSubstringWithExactKUniqueCharsOptimal(s, k)); // Output: "ece"
    }
}


