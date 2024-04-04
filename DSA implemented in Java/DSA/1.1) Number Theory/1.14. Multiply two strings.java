/*
Multiply two strings
Medium
Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Example 1:
Input:
s1 = "0033"
s2 = "2"
Output:
66

Example 2:
Input:
s1 = "11"
s2 = "23"
Output:
253

Your Task: 
You don't need to read input or print anything. Your task is to complete the function multiplyStrings() which takes two strings s1 and s2 as input and returns their product as a string.

Expected Time Complexity: O(n1* n2)
Expected Auxiliary Space: O(n1 + n2); where n1 and n2 are sizes of strings s1 and s2 respectively.

Constraints:
1 ≤ length of s1 and s2 ≤ 10^3
*/

// SOLUTION

public class MultiplyString {
    public static void main(String[] args) {
        MultiplyString ms = new MultiplyString();

        // Test the method with two input strings
        String res = ms.multiplyStrings("11", "23");

        System.out.println("Result : " + res);
    }

    public String multiplyStrings(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();

        // Array to store the result of multiplication
        int[] result = new int[m + n];

        // Iterate through each digit of s1 in reverse order
        for (int i = m - 1; i >= 0; i--) {
            int carry = 0;
            int num1 = s1.charAt(i) - '0';

            // Iterate through each digit of s2 in reverse order
            for (int j = n - 1; j >= 0; j--) {
                int num2 = s2.charAt(j) - '0';

                // Multiply current digits and add it to the result array
                int sum = num1 * num2 + result[i + j + 1] + carry;
                result[i + j + 1] = sum % 10;
                carry = sum / 10;
            }

            // Add the remaining carry to the previous position
            result[i] += carry;
        }

        // Convert the result array to string
        StringBuilder sb = new StringBuilder();
        for (int digit : result) {
            // Skip leading zeroes
            if (sb.length() == 0 && digit == 0) {
                continue;
            }
            sb.append(digit);
        }

        // If the result is empty, return "0"
        if (sb.length() == 0) {
            return "0";
        }

        return sb.toString();
    }
}
