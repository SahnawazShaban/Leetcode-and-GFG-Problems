"""
Aggressive Cows

Medium

banner
You are given an array consisting of n integers which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. You are given the task of assigning stalls to k cows such that the minimum distance between any two of them is the maximum possible.
The first line of input contains two space-separated integers n and k.
The second line contains n space-separated integers denoting the position of the stalls.

Example 1:

Input:
n=5 
k=3
stalls = [1 2 4 8 9]
Output:
3
Explanation:
The first cow can be placed at stalls[0], 
the second cow can be placed at stalls[2] and 
the third cow can be placed at stalls[3]. 
The minimum distance between cows, in this case, is 3, 
which also is the largest among all possible ways.


Example 2:

Input:
n=5 
k=3
stalls = [10 1 2 7 5]
Output:
4
Explanation:
The first cow can be placed at stalls[0],
the second cow can be placed at stalls[1] and
the third cow can be placed at stalls[4].
The minimum distance between cows, in this case, is 4,
which also is the largest among all possible ways.
Your Task:
Complete the function int solve(), which takes integer n, k, and a vector stalls with n integers as input and returns the largest possible minimum distance between cows.

Expected Time Complexity: O(n*log(10^9)).
Expected Auxiliary Space: O(1).

Constraints:
2 <= n <= 10^5
2 <= k <= n
0 <= stalls[i] <= 10^9

"""

# SOLUTION

class Solution:
    # Without using any inbuilt function

    # Brute force
    def sortArray(arr):
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key

        return arr

    def canWePlace(arr,dist,cows):
        capacity = 1
        last = arr[0]

        for i in range(1,len(arr)):
            if arr[i]-last >= dist:
                capacity += 1
                last = arr[i]

        return capacity >= cows

    def aggresiveCow(arr,cows):
        n = len(arr)
        sortArray(arr)

        for i in range(1,arr[n-1]):
            if canWePlace(arr,i,cows):
                continue
            else:
                return i-1
            
    # ---------------------------------------

    # Optimal Approach : Binary
    def sortArray(arr):
        n = len(arr)
        for i in range(1,n):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1

            arr[j+1] = key

        return arr
    
    def canWePlace(self,stalls,mid,k):
        n = len(stalls)
        countCow = 1
        last = stalls[0]
        
        for i in range(1,n):
            if stalls[i]-last >= mid:
                countCow += 1
                last = stalls[i]
        
        return countCow >= k
        
    def solve(self,n,k,stalls):
        # stalls.sort()
        sortArray(arr)
        low, high = 0, stalls[n-1]
        
        while low <= high:
            mid = low + (high-low)//2
            
            if self.canWePlace(stalls,mid,k):
                low = mid + 1
            else:
                high = mid - 1
        
        return high
