"""
Job Sequencing Problem

Medium

Given a set of N jobs where each jobi has a deadline and profit associated with it.

Each job takes 1 unit of time to complete and only one job can be scheduled at a time. We earn the profit associated with job if and only if the job is completed by its deadline.

Find the number of jobs done and the maximum profit.

Note: Jobs will be given in the form (Jobid, Deadline, Profit) associated with that Job. Deadline of the job is the time before which job needs to be completed to earn the profit.


Example 1:
Input:
N = 4
Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
Output:
2 60
Explanation:
Job1 and Job3 can be done with
maximum profit of 60 (20+40).

Example 2:
Input:
N = 5
Jobs = {(1,2,100),(2,1,19),(3,2,27),
        (4,1,25),(5,1,15)}
Output:
2 127
Explanation:
2 jobs can be done with
maximum profit of 127 (100+27).

Your Task :
You don't need to read input or print anything. Your task is to complete the function JobScheduling() which takes an integer N and an array of Jobs(Job id, Deadline, Profit) as input and returns the count of jobs and maximum profit as a list or vector of 2 elements.


Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(N)


Constraints:
1 <= N <= 10^5
1 <= Deadline <= N
1 <= Profit <= 500

"""

# SOLUTION

from heapq import heappush, heappop
        
class Solution:
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        # Sort jobs by increasing deadline
        Jobs.sort(key=lambda j: j.deadline)  # Time complexity: O(n log n)
    
        total = 0  # Total profit earned
        h = []  # Min-heap to store profits of scheduled jobs
    
        for j in Jobs:
            # Add the current job's profit to the total
            total += j.profit
            heappush(h, j.profit)  # Add profit to the heap
    
            # If we've scheduled more jobs than the current deadline allows:
            while len(h) > j.deadline:
                # Remove the job with the lowest profit to make space
                total -= heappop(h)
    
        # Return the number of scheduled jobs and the total profit
        return len(h), total

# Time Complexity: O(n log n)
# Space Complexity: O(n)