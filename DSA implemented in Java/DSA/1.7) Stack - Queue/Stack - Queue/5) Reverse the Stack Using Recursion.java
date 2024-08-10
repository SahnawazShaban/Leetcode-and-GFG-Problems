/*
Reverse a Stack
Medium

You are given a stack St. You have to reverse the stack using recursion.

Example 1:
Input:
St = {3,2,1,7,6}
Output:
{6,7,1,2,3}
Explanation:
Input stack after reversing will look like the stack in the output.

Example 2:
Input:
St = {4,3,9,6}
Output:
{6,9,3,4}
Explanation:
Input stack after reversing will look like the stack in the output.

Your Task:
You don't need to read input or print anything. Your task is to complete the function Reverse() which takes the stack St as input and reverses the given stack.

Expected Time Complexity: O(N^2)
Expected Auxiliary Space: O(1)

Constraints:
1 <= size of the stack <= 10^4
-10^9 <= Each element of the stack <= 10^9
Sum of N over all test cases doesn't exceeds 10^6
Array may contain duplicate elements. 
*/

// SOLUTION

class Solution {
    public char[] reverse(char[] St) {
        // Two Pointer Approach
        reverseList(0, St.length - 1, St);
        return St;
    }

    private void reverseList(int left, int right, char[] St) {
        if (left >= right) {
            return;
        }

        // Swap the characters at the left and right indices
        char temp = St[left];
        St[left] = St[right];
        St[right] = temp;

        // Recursive call to reverse the remaining elements
        reverseList(left + 1, right - 1, St);
    }
}

    
/*
Time Complexity:
The time complexity of the revList function is determined by the number of recursive calls it makes. With each recursive call, the function swaps two elements in the string. The base case is reached when the left pointer is greater than or equal to the right pointer, indicating that the recursion should stop.

The number of recursive calls is directly proportional to the number of swaps required to reverse the string. For a string of length n, this algorithm performs n/2 swaps. Therefore, the time complexity is O(n).

Space Complexity:
The space complexity of the revList function is determined by the depth of the recursive call stack. With each recursive call, a constant amount of space is used for function parameters and local variables. The maximum depth of the recursive call stack is equal to the maximum recursion depth, which is O(n) for this algorithm.

Therefore, the overall space complexity is O(n).

In summary:
Time Complexity: O(n)
Space Complexity: O(n).
*/
