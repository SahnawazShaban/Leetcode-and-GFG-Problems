/*
Sample Input 1:
m = 1
w = 3
Sample Output 1:
3
Explanation:
There is 1 man (m1) and 3 women (w1, w2, w3).
The valid combinations of 3 people, where at least one is a man and one is a woman, are:
(m1, w1, w2)
(m1, w1, w3)
(m1, w2, w3)
Total valid combinations = 3.

Sample Input 2:
m = 2
w = 2
Sample Output 2:
4
Explanation:
There are 2 men (m1, m2) and 2 women (w1, w2).
The valid combinations of 3 people are:
(m1, m2, w1)
(m1, m2, w2)
(m1, w1, w2)
(m2, w1, w2)
Total valid combinations = 4.

Sample Input 3:
m = 3
w = 3
Sample Output 3:
20
Explanation:
There are 3 men (m1, m2, m3) and 3 women (w1, w2, w3).
Valid combinations include choosing:
1 man and 2 women.
2 men and 1 woman.
There are 9 combinations with 1 man and 2 women, and 9 combinations with 2 men and 1 woman:
(m1, w1, w2)
(m1, w1, w3)
(m1, w2, w3)
(m2, w1, w2)
(m2, w1, w3)
(m2, w2, w3)
(m3, w1, w2)
(m3, w1, w3)
(m3, w2, w3)
(m1, m2, w1)
(m1, m2, w2)
(m1, m2, w3)
(m1, m3, w1)
(m1, m3, w2)
(m1, m3, w3)
(m2, m3, w1)
(m2, m3, w2)
(m2, m3, w3)
Total valid combinations = 18 + 2 combinations where all three members are different men or women = 20.
*/


//Solution

public class Solution {
    
    public static int diverseDeputation(int m, int w) {
        // Calculate total combinations of selecting 3 people from (m + w) people
        int totalWays = combination(m + w, 3);
        
        // Subtract combinations where all 3 are men
        if (m >= 3) {
            totalWays -= combination(m, 3);
        }
        
        // Subtract combinations where all 3 are women
        if (w >= 3) {
            totalWays -= combination(w, 3);
        }
        
        return totalWays;
    }
    
    // Helper function to calculate combinations C(n, k)
    private static int combination(int n, int k) {
        if (k > n) {
            return 0;
        }
        return factorial(n) / (factorial(k) * factorial(n - k));
    }
    
    // Helper function to calculate factorial
    private static int factorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }
        return n * factorial(n - 1);
    }
    
    public static void main(String[] args) {
        System.out.println(diverseDeputation(1, 3)); // Example input from the problem
    }
}
