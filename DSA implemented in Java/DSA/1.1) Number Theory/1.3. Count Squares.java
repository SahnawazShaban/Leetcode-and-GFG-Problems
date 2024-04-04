/*
Count Squares
Basic
Consider a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on. You are given a number N, you have to output the number of integers less than N in the sample space S.

Example 1:
Input :
N = 9
Output:
2
Explanation:
1 and 4 are the only Perfect Squares
less than 9. So, the Output is 2.

Example 2:
Input :
N = 3
Output:
1
Explanation:
1 is the only Perfect Square
less than 3. So, the Output is 1.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function countSquares() which takes an Integer N as input and returns the answer.


Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)


Constraints:
1 <= N <= 10^8

*/

// SOLUTION

class Solution {
    static int countSquares(int N) {
        
        int count = 0;
        for (int i=1; i<=Math.sqrt(N); i++){
            if (i*i < N){
                count++;
            }
        }
        
        return count;
    }
}