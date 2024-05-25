"""
56. Merge Intervals

Medium

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4

"""

# SOLUTION

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ## Brute Force
        
        '''
        n = len(arr)
        arr.sort()
        ans = []
        
        for i in range(n):
            start = arr[i][0]
            end = arr[i][1]
        
            if ans and end <= ans[-1][1]:
                continue
        
            for j in range(i+1,n):
                if arr[j][0] <= end:
                    end = max(end,arr[j][1])
                else:
                    break
            ans.append([start,end])
        
        return ans
        '''

        ## Optimize

        if intervals is None:
            return intervals
        
        n = len(intervals)
        intervals.sort()
        ans = []

        ans.append(intervals[0])

        for i in range(1,n):
            if intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])

        return ans
        