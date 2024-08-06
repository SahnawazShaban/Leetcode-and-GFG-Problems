/*
Colorful Number
Hashing
easy
Asked In:
Problem Description
 
 

For Given Number A, find if it's a COLORFUL number or not.

COLORFUL number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different
Return 1 if A is a COLORFUL number, else return 0


Problem Constraints
0 <= A <= 10^9


Input Format
The first argument is an integer A.

Output Format
Return 1 if A is a COLORFUL number, else return 0


Example Input
A = 23

Example Output
1

Example Explanation
A = 23
2 3 23
2 -> 2
3 -> 3
23 -> 6
this number is a COLORFUL number since the product of every digit of a sub-sequence is different.

Output: 1
*/

// SOLUTION

public class Solution {
    public int colorful(int A) {
        // Convert the number to a string to easily access each digit
        String numStr = Integer.toString(A);
        
        // Initialize a set to store products of subsequences
        HashSet<Integer> products = new HashSet<>();
        
        // Length of the number string
        int n = numStr.length();
        
        // Generate all contiguous subsequences
        for (int i = 0; i < n; i++) {
            int product = 1;
            for (int j = i; j < n; j++) {
                product *= numStr.charAt(j) - '0';
                // If product already exists in the set, return 0 (not colorful)
                if (products.contains(product)) {
                    return 0;
                }
                products.add(product);
            }
        }
        
        // If all products are unique, return 1 (colorful)
        return 1;
    }
}
