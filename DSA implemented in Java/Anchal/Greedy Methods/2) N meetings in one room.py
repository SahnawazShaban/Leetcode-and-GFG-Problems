"""
N meetings in one room

Easy

There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?

Note: Start time of one chosen meeting can't be equal to the end time of the other chosen meeting.


Example 1:
Input:
N = 6
start[] = {1,3,0,5,8,5}
end[] =  {2,4,6,7,9,9}
Output: 
4
Explanation:
Maximum four meetings can be held with
given start and end timings.
The meetings are - (1, 2),(3, 4), (5,7) and (8,9)

Example 2:
Input:
N = 3
start[] = {10, 12, 20}
end[] = {20, 25, 30}
Output: 
1
Explanation:
Only one meetings can be held
with given start and end timings.

Your Task :
You don't need to read inputs or print anything. Complete the function maxMeetings() that takes two arrays start[] and end[] along with their size N as input parameters and returns the maximum number of meetings that can be held in the meeting room.


Expected Time Complexity : O(N*LogN)
Expected Auxilliary Space : O(N)


Constraints:
1 ≤ N ≤ 10^5
0 ≤ start[i] < end[i] ≤ 10^5

"""

# SOLUTION

class Solution:
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # Initialize count to track the number of non-overlapping meetings
        count = 1
        # Combine start and end times into tuples and create a list of meetings
        # meetings = list(zip(start, end))
        # or
        meetings = [(start[i], end[i]) for i in range(n)]
    
        # Sort the meetings based on their start times
        meetings.sort()
    
        # Iterate through the sorted meetings
        for i in range(n - 1):
            # Check if the end time of the current meeting overlaps with the start time of the next meeting
            if meetings[i][1] >= meetings[i + 1][0]:
                # If there is an overlap, update the end time of the next meeting to the minimum of the two
                meetings[i + 1] = (meetings[i][0], min(meetings[i][1], meetings[i + 1][1]))
            else:
                # If there is no overlap, increment the count of non-overlapping meetings
                count += 1
    
        # Return the count of non-overlapping meetings
        return count
        
'''
Time Complexity:

Sorting the list of meetings has a time complexity of O(n log n), where n is the number of meetings.
The subsequent iteration through the sorted meetings has a linear time complexity of O(n).
Therefore, the overall time complexity is dominated by the sorting step and is O(n log n).


Space Complexity:

The space complexity is primarily influenced by the creation of the meetings list, 
which stores tuples of start and end times. This list consumes O(n) space.
'''
