/*
84. Largest Rectangle in Histogram
Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
*/

// SOLUTION

// Solution 1: Using Nearest Smaller to Left (NSL) and Nearest Smaller to Right (NSR)

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

class Solution {
    public int largestRectangleArea(int[] heights) {
        // Nearest Smallest to Left
        List<Integer> NSL(int[] heights) {
            Stack<int[]> stack = new Stack<>();
            List<Integer> left = new ArrayList<>();
            int psuedo_idx = -1;
            int n = heights.length;

            for (int i = 0; i < n; i++) {
                if (stack.isEmpty()) {
                    left.add(psuedo_idx);
                } else if (stack.peek()[0] < heights[i]) {
                    left.add(stack.peek()[1]);
                } else {
                    while (!stack.isEmpty() && stack.peek()[0] >= heights[i]) {
                        stack.pop();
                    }
                    if (stack.isEmpty()) {
                        left.add(psuedo_idx);
                    } else {
                        left.add(stack.peek()[1]);
                    }
                }
                stack.push(new int[]{heights[i], i});
            }
            return left;
        }

        // Nearest Smallest to Right
        List<Integer> NSR(int[] heights) {
            Stack<int[]> stack = new Stack<>();
            List<Integer> right = new ArrayList<>();
            int n = heights.length;
            int psuedo_idx = n;

            for (int i = n - 1; i >= 0; i--) {
                if (stack.isEmpty()) {
                    right.add(psuedo_idx);
                } else if (stack.peek()[0] < heights[i]) {
                    right.add(stack.peek()[1]);
                } else {
                    while (!stack.isEmpty() && stack.peek()[0] >= heights[i]) {
                        stack.pop();
                    }
                    if (stack.isEmpty()) {
                        right.add(psuedo_idx);
                    } else {
                        right.add(stack.peek()[1]);
                    }
                }
                stack.push(new int[]{heights[i], i});
            }
            Collections.reverse(right);
            return right;
        }

        List<Integer> left = NSL(heights);
        List<Integer> right = NSR(heights);
        int n = heights.length;
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            int width = right.get(i) - left.get(i) - 1;
            int area = heights[i] * width;
            maxArea = Math.max(maxArea, area);
        }

        return maxArea;
    }
} 

// Solution 2: Optimized Stack-Based Approach

class Solution {
    public int largestRectangleArea(int[] heights) {
        if (heights.length == 1) return heights[0];

        Stack<int[]> stack = new Stack<>();
        int maxA = 0;
        heights = Arrays.copyOf(heights, heights.length + 1);

        for (int i = 0; i < heights.length; i++) {
            int h = heights[i];
            if (!stack.isEmpty() && h == stack.peek()[1]) {
                continue;
            }
            int startIdx = i;
            while (!stack.isEmpty() && h < stack.peek()[1]) {
                int[] pair = stack.pop();
                startIdx = pair[0];
                maxA = Math.max(maxA, pair[1] * (i - startIdx));
            }
            stack.push(new int[]{startIdx, h});
        }

        return maxA;
    }
}

//Solution 3: Stack-Based Approach with Simplified Logic

class Solution {
    public int largestRectangleArea(int[] heights) {
        int maxSquare = 0;
        Stack<int[]> stack = new Stack<>();

        for (int i = 0; i < heights.length; i++) {
            int val = heights[i];
            if (stack.isEmpty() || stack.peek()[0] <= val) {
                stack.push(new int[]{val, i});
            } else {
                while (!stack.isEmpty() && stack.peek()[0] > val) {
                    int[] pair = stack.pop();
                    int height = pair[0];
                    int index = pair[1];
                    maxSquare = Math.max(maxSquare, (i - index) * height);
                }
                stack.push(new int[]{val, stack.isEmpty() ? 0 : stack.peek()[1]});
            }
        }

        while (!stack.isEmpty()) {
            int[] pair = stack.pop();
            int height = pair[0];
            int index = pair[1];
            maxSquare = Math.max(maxSquare, (heights.length - index) * height);
        }

        return maxSquare;
    }
}