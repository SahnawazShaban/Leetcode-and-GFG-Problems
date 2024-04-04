/*
Largest prime factor
Medium
Given a number N, the task is to find the largest prime factor of that number.

Example 1:
Input:
N = 5
Output:
5
Explanation:
5 has 1 prime factor i.e 5 only.

Example 2:
Input:
N = 24
Output:
3
Explanation:
24 has 2 prime factors 2 and 3 in which 3 is greater.
Your Task:
You don't need to read input or print anything. Your task is to complete the function largestPrimeFactor() which takes an integer N as input parameters and returns an integer, largest prime factor of N.

Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(1)

Constraints:
2 <= N <= 10^9
*/

// SOLUTION

class Solution{
    static long largestPrimeFactor(int N) {
        int largest_prime = -1;
        
        while (N % 2 == 0){
            largest_prime = 2;
            N /= 2;
        }
        
        for (int i = 3; i<= Math.sqrt(N); i = i+2){
            while (N % i == 0){
                largest_prime = i;
                N /= i;
            }
        }
        
        if (N > 2){
            largest_prime = N;
        }
        
        return largest_prime;
    }
}
