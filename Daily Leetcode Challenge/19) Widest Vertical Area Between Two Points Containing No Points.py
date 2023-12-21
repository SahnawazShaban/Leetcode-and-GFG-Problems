"""
1637. Widest Vertical Area Between Two Points Containing No Points

Medium

Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.


Example 1:
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.

Example 2:
Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3
 

Constraints:

n == points.length
2 <= n <= 10^5
points[i].length == 2
0 <= xi, yi <= 10^9

"""


# Solution 

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # Sort the points based on their x-coordinates
        points.sort()

        # length of points
        n = len(points)

        # Initialize a variable to store the maximum width
        maxi = 0

        # NOTE : I skip 1 like (n-1) because inside the loop I need (i+1) element.
        for i in range(n-1):
            # Calculate the width between consecutive points along the x-axis
            width = points[i+1][0] - points[i][0]

            # Update the maximum width if the current width is greater
            maxi = max(maxi, width)

        # Return the maximum width
        return maxi

'''
Time Complexity:
The time complexity of this code is dominated by the sorting operation, which has a time complexity of O(n log n), where n is the number of points. The subsequent iteration through the sorted points takes O(n) time. Therefore, the overall time complexity is O(n log n).

Space Complexity:
The space complexity is O(n), where n is the number of points. This is due to the storage of the sorted points.
'''

