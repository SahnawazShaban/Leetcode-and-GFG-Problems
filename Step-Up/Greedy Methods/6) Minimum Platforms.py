"""
Minimum Platforms

Medium

Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. Arrival and departure time can never be the same for a train but we can have arrival time of one train equal to departure time of the other. At any given instance of time, same platform can not be used for both departure of a train and arrival of another train. In such cases, we need different platforms.


Example 1:
Input: n = 6 
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation: 
Minimum 3 platforms are required to 
safely arrive and depart all trains.

Example 2:
Input: n = 3
arr[] = {0900, 1100, 1235}
dep[] = {1000, 1200, 1240}
Output: 1
Explanation: Only 1 platform is required to 
safely manage the arrival and departure 
of all trains. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function findPlatform() which takes the array arr[] (denoting the arrival times), array dep[] (denoting the departure times) and the size of the array as inputs and returns the minimum number of platforms required at the railway station such that no train waits.

Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (this may be > 59).


Expected Time Complexity: O(nLogn)
Expected Auxiliary Space: O(n)


Constraints:
1 ≤ n ≤ 50000
0000 ≤ A[i] ≤ D[i] ≤ 2359

"""

# SOLUTION

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # Sort arrival and departure times for efficient comparison
        arr.sort()
        dep.sort()
    
        # Initialize variables for tracking train counts and platforms
        i = 0  # Index for iterating through arrival times
        j = 0  # Index for iterating through departure times
        count = 0  # Current number of trains at the station
        ans = 0  # Minimum number of platforms needed so far
    
        # Iterate through arrival and departure times simultaneously
        while i < n and j < n:
            # If a train is departing before or at the same time as the next arrival:
            if arr[i] >= dep[j]:
                # Reduce the count of trains at the station
                count -= 1
                # Move to the next departure time
                j += 1
            else:
                # A train is arriving:
                # Increase the count of trains at the station
                count += 1
                # Move to the next arrival time
                i += 1
    
            # Update the minimum platform count if needed
            ans = max(ans, count)
    
        # Return the minimum number of platforms required
        return ans
    