/*
Check if strings are rotations of each other or not
Easy
You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.

Note: The characters in the strings are in lowercase.

Example 1:
Input:
geeksforgeeks
forgeeksgeeks
Output: 
1
Explanation: s1 is geeksforgeeks, s2 is
forgeeksgeeks. Clearly, s2 is a rotated
version of s1 as s2 can be obtained by
left-rotating s1 by 5 units.

Example 2:
Input:
mightandmagic
andmagicmigth
Output: 
0
Explanation: Here with any amount of
rotation s2 can't be obtained by s1.
Your Task:
You don't have to read or print anything. The task is to complete the function areRotations() which takes two strings, s1 and s2 as inputs and checks if the two strings are rotations of each other. The function returns true if s1 can be obtained by rotating s2, else it returns false.

Expected Time Complexity: O( |s1| ).
Expected Space Complexity: O( |s1| ).

Constraints:
1 <= |s1|, |s2| <= 10^5
*/

// SOLUTION

class Solution {
    public static boolean areRotations(String s1, String s2) {
        // Solution - 0
        if (s1.length() != s2.length())
            return false;

        int n = s1.length();
        // Check if s2 is a substring of s1 concatenated with itself
        for (int i = 0; i < n; i++) {
            boolean isRotation = true;
            for (int j = 0; j < n; j++) {
                if (s1.charAt((i + j) % n) != s2.charAt(j)) {
                    isRotation = false;
                    break;
                }
            }
            if (isRotation)
                return true;
        }
        return false;

        // Solution - 1
        String str = s1 + s1;
        int i = 0;
        int j = 0;
        while (i < str.length() && j < s2.length()) {
            if (str.charAt(i) == s2.charAt(j)) {
                i++;
                j++;
            } else {
                i++;
            }
        }

        return j == s2.length();

        // Solution - 2
        String ans = s1 + s1;
        return ((s1.length() == s2.length()) && (ans.indexOf(s2) != -1));

        // Solution - 3
        if (s1.length() != s2.length())
            return false;

        // Concatenate s1 with itself
        String concatenated = s1 + s1;

        // Check if s2 is a substring of the concatenated string
        return concatenated.contains(s2);
    }
}
