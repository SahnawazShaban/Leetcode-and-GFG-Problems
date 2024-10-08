/*
Next Greater Element
Medium

Given an array arr[ ] of size N having elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Example 1:
Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.

Example 2:
Input: 
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
Explanation:
In the array, the next larger element to 
6 is 8, for 8 there is no larger elements 
hence it is -1, for 0 it is 1 , for 1 it 
is 3 and then for 3 there is no larger 
element on right and hence -1.

Your Task:
This is a function problem. You only need to complete the function nextLargerElement() 
that takes list of integers arr[ ] and N as input parameters and returns list of integers 
of length N denoting the next greater elements for all the corresponding elements in the input array.

Expected Time Complexity : O(N)
Expected Auxiliary Space : O(N)

Constraints:
1 ≤ N ≤ 10^6
0 ≤ Ai ≤ 10^(18)

*/

// SOLUTION

import java.util.Stack;

class Solution {
    
    // Solution 1 - Brute Force
    public int[] nextLargerElementBruteForce(int[] arr, int n) {
        for (int i = 0; i < n - 1; i++) {
            boolean flag = true;
            for (int j = i + 1; j < n; j++) {
                if (arr[i] < arr[j]) {
                    arr[i] = arr[j];
                    flag = false;
                    break;
                }
            }
            if (flag) {
                arr[i] = -1;
            }
        }
        arr[n - 1] = -1;
        return arr;
    }

    // Solution 2 - Better (Stack-based)
    public int[] nextLargerElement(int[] arr, int n) {
        if (n == 0) {
            return new int[0];
        }

        if (n == 1) {
            return new int[]{-1};
        }

        Stack<Integer> stack = new Stack<>();
        stack.push(arr[n - 1]);

        for (int i = n - 2; i >= 0; i--) {
            int temp = arr[i];

            while (!stack.isEmpty() && temp >= stack.peek()) {
                stack.pop();
            }

            if (stack.isEmpty()) {
                arr[i] = -1;
            } else {
                arr[i] = stack.peek();
            }

            stack.push(temp);
        }

        arr[n - 1] = -1;

        return arr;
    }
}

/*
Time Complexity:
The time complexity is O(n), where n is the size of the input array. In the worst case, you iterate through each element in the array once. Within each iteration, the while loop (inside the for loop) may cause some elements to be popped from the stack, but each element is processed at most once.

Space Complexity:
The space complexity is also O(n). In the worst case, the stack can have at most n elements, where n is the size of the input array. This occurs when the array is sorted in non-decreasing order.

Additionally, the result array arr is modified in-place, and its space complexity is O(1) because it doesn't depend on the size of the input but only on a constant number of variables.
*/
