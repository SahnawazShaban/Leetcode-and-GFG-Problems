"""
57. Insert Interval

Medium

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5

"""

# SOLUTION

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        n = len(intervals)
        intervals.sort()
        # [[1, 3], [2, 5], [6, 9]] - Sorted Intervals

        ans = []
        ans.append(intervals[0])

        for i in range(1, n):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
            
        return ans


'''
Time Complexity:
Overall: O(n log n)

Breakdown:
Appending newInterval: O(1)
Sorting intervals: O(n log n) (typically using a comparison-based sorting algorithm like merge sort or quick sort)
Iterating through intervals and merging: O(n)


Space Complexity: O(n)
intervals list: Stores up to n + 1 elements (original intervals + newInterval)
ans list: Stores up to n elements in the worst case
Temporary variables within the loop don't contribute significantly to space complexity


Key factors for time complexity:

Sorting the intervals dominates the time complexity due to its O(n log n) nature.
The merging process within the loop is linear, but its overall contribution is bounded by n.


Potential Optimization:

If the input intervals are already sorted, the initial sorting step could be avoided, reducing the overall time complexity to O(n). 
However, this optimization depends on the specific problem constraints and data distribution.
'''