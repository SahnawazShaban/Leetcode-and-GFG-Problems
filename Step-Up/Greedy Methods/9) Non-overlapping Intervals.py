"""
435. Non-overlapping Intervals

Medium

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 
Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4

"""

# SOLUTION

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Get the number of intervals
        n = len(intervals)
        
        # If there is only one interval, no overlaps can occur
        if n == 1:
            return 0

        # Sort intervals based on their end times
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        # [[1, 2], [2, 3], [1, 3], [3, 4]]

        # Initialize variables
        count = 0
        end = intervals[0][1]

        # Iterate through sorted intervals
        for i in range(1, n):
            # If the current interval overlaps with the previous one
            if intervals[i][0] < end:
                count += 1
            else:
                # Update the ending point if no overlap
                end = intervals[i][1]

        # Return the count of overlapping intervals
        return count
        