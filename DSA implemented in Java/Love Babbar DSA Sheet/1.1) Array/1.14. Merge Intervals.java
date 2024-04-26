/*
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
*/

// SOLUTION

class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) {
            return intervals;
        }

        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        // Integer.compare(int x, int y) is a static method in the Integer class in
        // Java. It compares two integer values x and y and returns:
        int[][] merged = new int[intervals.length][2];
        int index = 0;
        merged[0] = intervals[0];

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] > merged[index][1]) {
                merged[++index] = intervals[i];
            } else {
                merged[index][1] = Math.max(merged[index][1], intervals[i][1]);
            }
        }
        // Another way if you not use Arrays.copyOf
        /*
         * int[][] result = new int[index + 1][2];
         * for (int i = 0; i <= index; i++) {
         * result[i] = merged[i];
         * }
         */
        return Arrays.copyOf(merged, index + 1);
    }
}