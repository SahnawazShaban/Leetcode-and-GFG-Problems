/*
LCM And GCD
Basic
Given two numbers A and B. The task is to find out their LCM and GCD.

Example 1:
Input:
A = 5 , B = 10
Output:
10 5
Explanation:
LCM of 5 and 10 is 10, while
thier GCD is 5.

Example 2:
Input:
A = 14 , B = 8
Output:
56 2
Explanation:
LCM of 14 and 8 is 56, while
thier GCD is 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function lcmAndGcd() which takes an Integer N as input and returns a List of two Integers, the required LCM and GCD.

Expected Time Complexity: O(log(min(A, B))
Expected Auxiliary Space: O(1)

Constraints:
1 <= A,B <= 10^9
*/

// SOLUTION

class Solution {
    static Long find(Long x , Long y) {
        if(x == 0){
            return y;
        }
        if(y == 0){
            return x;
        }
        
        return find(y, x%y);
    }
    
    static Long[] lcmAndGcd(Long A, Long B){
        Long ans[] = new Long[2];
        
        ans[1] = find(A,B);
        ans[0] = (A*B)/ans[1];
        
        return ans;
    }
};