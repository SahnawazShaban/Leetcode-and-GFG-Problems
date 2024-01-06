"""
1235. Maximum Profit in Job Scheduling

Hard

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 
Example 1:
Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:
Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.

Example 3:
Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""


# Solution 

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Sorting jobs based on start time
        sorted_jobs = sorted(list(zip(startTime, endTime, profit)))

        # Heap to track ongoing jobs with end times and accumulated profits
        job_heap = []
        current_profit, max_profit = 0, 0

        # Iterating through sorted jobs
        for start_time, end_time, job_profit in sorted_jobs:
            # Popping jobs that have already ended from the heap
            while job_heap and job_heap[0][0] <= start_time:
                popped_end_time, popped_tmp_profit = heapq.heappop(job_heap)
                current_profit = max(current_profit, popped_tmp_profit)
            
            # Pushing the current job onto the heap with updated profit
            heapq.heappush(job_heap, (end_time, current_profit + job_profit))
            
            # Updating the maximum profit
            max_profit = max(max_profit, current_profit + job_profit)

        # Returning the maximum profit
        return max_profit

'''
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

# Combining lists into tuples and sorting by start time
sorted_jobs = sorted(list(zip(startTime, endTime, profit)))

# Resulting sorted list of tuples
# sorted_jobs = [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]
'''

'''
Time Complexity:

Sorting the jobs takes O(n log n), where n is the number of jobs.
The loop iterates through each job once, and within the loop, there are heap operations and constant time operations. Therefore, the overall time complexity is O(n log n).


Space Complexity:

The space complexity is influenced by the sorted_jobs list and the job_heap heap.
The sorted_jobs list requires O(n) space.
The job_heap heap can have at most n elements (for each job). Therefore, the space complexity is O(n).
'''
