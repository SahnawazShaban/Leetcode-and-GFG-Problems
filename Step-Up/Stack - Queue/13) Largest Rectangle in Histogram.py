"""
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

"""

# SOLUTION

class Solution:
    # Solution - 1
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Nearest Smallest to left
        def NSL(heights, stack, left):
            n = len(heights)
            # Assume there is no element before the first index, so just assume -1.
            psuedo_idx = -1
            # Every element you detect in the stack easily from the left side, but try to understand it by drawing the diagram.
            for i in range(n):
                if len(stack) == 0:
                    left.append(psuedo_idx)

                elif stack and stack[-1][0] < heights[i]:
                    left.append(stack[-1][1])

                elif stack and stack[-1][0] >= heights[i]:

                    while stack and stack[-1][0] >= heights[i]:
                        stack.pop()

                    if len(stack) == 0:
                        left.append(psuedo_idx)
                    else:
                        left.append(stack[-1][1])

                stack.append((heights[i], i))

            return left

        # Nearest Smallest to right
        def NSR(heights,stack,right):
            n = len(heights)
            # Assume there is no element after the last index, so just assume (last_idx + 1 = n).
            psuedo_idx = n
            # Every element you detect in the stack easily from the right side, but try to understand it by drawing the diagram.
            for i in range(n-1,-1,-1):
                if len(stack) == 0:
                    right.append(psuedo_idx)

                elif stack and stack[-1][0] < heights[i]:
                    right.append(stack[-1][1])

                elif stack and stack[-1][0] >= heights[i]:

                    while stack and stack[-1][0] >= heights[i]:
                        stack.pop()

                    if len(stack) == 0:
                        right.append(psuedo_idx)
                    else:
                        right.append(stack[-1][1])

                stack.append((heights[i],i))
            right.reverse()

            return right

        left = []
        NSL(heights, [], left)

        right = []
        NSR(heights,[],right)

        n = len(heights)
        width = [0]*n
        for i in range(n):
            width[i] = right[i] - left[i] - 1

        area = [0]*n
        for i in range(n):
            area[i] = heights[i]*width[i]

        ans = max(area)

        return ans
    
        '''
        Time Complexity: O(N)

        The NSL and NSR functions each iterate through the given heights array once, making their time complexity O(N).
        The subsequent loop for calculating width and area also iterates through the heights array once.
        Overall, the time complexity is dominated by the linear iteration through the heights array, resulting in O(N).

        
        Space Complexity: O(N)

        The space complexity is dominated by the storage of the NSL and NSR arrays, which have a length of N.
        The space used by the stack is also proportional to the input size.
        Overall, the space complexity is O(N).
        '''

        # This is for understanding
        '''
        print("Pair Stack : ")
        int_pair_stack = []

        # Push pairs onto the stack
        int_pair_stack.append((1, 2))
        int_pair_stack.append((3, 4))
        int_pair_stack.append((5, 6))

        print(int_pair_stack)  # [(1, 2), (3, 4), (5, 6)]
        print(int_pair_stack[1])  # (3, 4)
        print(int_pair_stack[2])  # (5, 6)
        print(int_pair_stack[1][0])  # 3
        print(int_pair_stack[-1][1])  # 4
        '''

        # -----------------------------------------------

        # Solution - 2
        '''
        def largestRectangleArea(self, heights: List[int]) -> int:
            if len(heights) == 1: return heights[0]
            stack = []
            maxA = 0
            heights.append(0)
            for i, h in enumerate(heights):
                if stack and h == stack[-1][1]:
                    continue
                startidx = i
                while stack and h < stack[-1][1]:
                    startidx, size = stack.pop()
                    maxA = max(maxA, size*(i-startidx))
                stack.append((startidx, h))
                
            return maxA
        '''

        # -----------------------------------------

        # Solution - 3
        '''
        def largestRectangleArea(self, heights: List[int]) -> int:
            max_square = 0
            stack = []
            for i, val in enumerate(heights):
                if not stack:
                    stack.append((val, i))
                    continue
                if stack[-1][0] <= val:
                    stack.append((val, i))
                else:
                    while stack and stack[-1][0] > val:
                        n, idx = stack.pop()
                        max_square = max(max_square, (i-idx) * n)
                    stack.append((val, idx))
            if stack:
                for val, index in stack:
                    max_square = max(max_square, (len(heights)-index) * val)
            return max_square
        '''
