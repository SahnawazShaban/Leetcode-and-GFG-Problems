/*
Prime Number
Basic
For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

Example 1:

Input:
N = 5
Output:
1
Explanation:
5 has 2 factors 1 and 5 only.

Example 2:
Input:
N = 25
Output:
0
Explanation:
25 has 3 factors 1, 5, 25

Your Task:
You don't need to read input or print anything. Your task is to complete the function isPrime() which takes an integer N as input parameters and returns an integer, 1 if N is a prime number or 0 otherwise.
 
Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^9
*/

// SOLUTION

class Solution{
    static int isPrime(int N){
        if (N <= 1){
            return 0;
        }
        
        for (int i = 2; i<=Math.sqrt(N); i++){
            if(N%i == 0){
                return 0;
            }
        }
        return 1;
    }
}