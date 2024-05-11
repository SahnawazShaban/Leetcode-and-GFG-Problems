/*
Reverse a String
Basic
You are given a string s. You need to reverse the string.

Example 1:
Input:
s = Geeks
Output: skeeG

Example 2:
Input:
s = for
Output: rof
Your Task:

You only need to complete the function reverseWord() that takes s as parameter and returns the reversed string.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000
*/

// SOLUTION

class Reverse {
    // Complete the function
    // str: input string
    public static String reverseWord(String str) {
        char[] ch = str.toCharArray();
        int len = str.length();

        int s = 0, e = len - 1;

        while (s < e) {
            char temp = ch[s];
            ch[s] = ch[e];
            ch[e] = temp;

            s++;
            e--;
        }

        return new String(ch);
    }
}

// ..........................................

class Reverse {
    // Complete the function
    // str: input string
    public static String reverseWord(String str) {
        int len = str.length();

        // Use StringBuilder to efficiently manipulate strings
        StringBuilder reversed = new StringBuilder(len);

        for (int i = len - 1; i >= 0; i--) {
            reversed.append(str.charAt(i));
        }

        return reversed.toString();
    }
}

// .........................................

class Reverse {
    // Complete the function
    // str: input string
    public static String reverseWord(String str) {
        // Base case: if the string is empty or has only one character, return the
        // string itself
        if (str.isEmpty() || str.length() == 1) {
            return str;
        } else {
            // Recursive case: reverse the substring starting from the second character and
            // append the first character at the end
            return reverseWord(str.substring(1)) + str.charAt(0);
        }
    }
}
