/*
Generate Parentheses
Medium

Given an integer N representing the number of pairs of parentheses, the task is to generate all combinations of well-formed(balanced) parentheses.

Example 1:
Input:
N = 3
Output:
((()))
(()())
(())()
()(())
()()()

Example 2:
Input:
N = 1
Output:
()

Your Task:  
You don't need to read input or print anything. Complete the function AllParenthesis() which takes N as input parameter and returns the list of balanced parenthesis.

Expected Time Complexity: O(2^N * N).
Expected Auxiliary Space: O(2*N*X), X = Number of valid Parenthesis.

Constraints:
1 ≤ N ≤ 12

*/

// SOLUTION

// Solution - 1
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> allParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        solve(n, n, "", ans);
        return ans;
    }

    private void solve(int open, int close, String op, List<String> ans) {
        if (open == 0 && close == 0) {
            ans.add(op);
            return;
        }

        if (open != 0) {
            String op1 = op + "(";
            solve(open - 1, close, op1, ans);
        }

        if (close > open) {
            String op2 = op + ")";
            solve(open, close - 1, op2, ans);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 3; // Example value for n
        List<String> result = solution.allParenthesis(n);
        for (String s : result) {
            System.out.println(s);
        }
    }
}

        
        // Time and Space Complexity
        
        // Time Complexity: O(2^n)
        // Space Complexity: O(2n + 2^n)
        
// ----------------------------------------------
// Solution - 2

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<String> allParenthesis(int n) {
        List<String> res = new ArrayList<>();
        dfs("", 0, 0, n, res);
        return res;
    }

    private void dfs(String s, int open, int close, int n, List<String> res) {
        if (s.length() == n * 2) {
            res.add(s);
            return;
        }
        if (open < n) {
            dfs(s + '(', open + 1, close, n, res);
        }
        if (close < open) {
            dfs(s + ')', open, close + 1, n, res);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n = 3; // Example value for n
        List<String> result = solution.allParenthesis(n);
        for (String s : result) {
            System.out.println(s);
        }
    }
}


/*
Time Complexity : The time complexity is determined by the number of recursive calls made by the `solve` function. In each recursive call, either an open parenthesis or a close parenthesis is added to the partial solution (`op`). The base case is reached when both the open and close counts are zero. In each recursive call, we either decrement the open count or the close count. Therefore, the total number of recursive calls is 2^n, where nnn is the input value.
As a result, the time complexity is O(2^n).

Space Complexity : The space complexity is determined by the depth of the recursive call stack and the space required to store the intermediate solutions. In each recursive call, a new string `op1` or `op2` is created to represent the partial solution. The maximum depth of the recursive call stack is 2n, as we decrement either the open count or the close count in each call.
Additionally, the space required to store the result (valid combinations) is proportional to the number of valid combinations, which is O(2^n).
Therefore, the overall space complexity is O(2n + 2^n).

In summary:

*   Time Complexity: O(2^n)
*   Space Complexity: O(2n + 2^n)
*/
        