"""
1578. Minimum Time to Make Rope Colorful

Medium

Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.

 

Example 1:
Input: colors = "abaac", neededTime = [1,2,3,4,5]
Output: 3
Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
Bob can remove the blue balloon at index 2. This takes 3 seconds.
There are no longer two consecutive balloons of the same color. Total time = 3.

Example 2:
Input: colors = "abc", neededTime = [1,2,3]
Output: 0
Explanation: The rope is already colorful. Bob does not need to remove any balloons from the rope.

Example 3:
Input: colors = "aabaa", neededTime = [1,2,3,4,1]
Output: 2
Explanation: Bob will remove the ballons at indices 0 and 4. Each ballon takes 1 second to remove.
There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.
 

Constraints:

n == colors.length == neededTime.length
1 <= n <= 10^5
1 <= neededTime[i] <= 10^4
colors contains only lowercase English letters.

"""


# Solution 

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        # Initialize the answer variable to store the minimum cost
        ans = 0
        
        # Initialize the pointer 'prev' to keep track of the previous index
        prev = 0

        # Iterate through the colors and their corresponding neededTime
        for i in range(1, len(colors)):
            # Check if the color at the current index is different from the color at the previous index
            if colors[prev] != colors[i]:
                # If different, update 'prev' to the current index
                prev = i
            else:
                # If colors are the same, add the minimum cost between the two indices to the answer
                ans += min(neededTime[prev], neededTime[i])

                # Update 'prev' to the index with the smaller cost
                if neededTime[prev] < neededTime[i]:
                    prev = i

        # Return the total minimum cost
        return ans 
        
'''
Time Complexity:
The algorithm iterates through the given 'colors' and 'neededTime' arrays once, resulting in a time complexity of O(N), where N is the length of the 'colors' array.

Space Complexity:
The space complexity is O(1) since the algorithm uses a constant amount of extra space regardless of the input size. The only variables used are 'ans' and 'prev'.
'''