"""
1642. Furthest Building You Can Reach

Medium

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.


Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

Example 2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
 

Constraints:

1 <= heights.length <= 10^5
1 <= heights[i] <= 10^6
0 <= bricks <= 10^9
0 <= ladders <= heights.length

"""


# SOLUTION
import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(len(heights) - 1):
            jump_len = heights[i + 1] - heights[i]
            
            if jump_len > 0:
                heapq.heappush(pq, jump_len)

                if len(pq) > ladders:
                    bricks -= heapq.heappop(pq)
                    if bricks < 0:
                        return i
        return len(heights) - 1

'''
/***************************************************************** PYTHON *****************************************************************/
//MEMORY LIMIT EXCEED - Not Accepted
//T.C : Without Memoization - O(2^(bricks + ladders)), With memoization - O(bricks * ladders)
//S.C : O(bricks * ladders) when we use memoization dp array

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        t = [[-1] * (ladders + 1) for _ in range(bricks + 1)]
        
        def solve(idx, bricks, ladders):
            if idx == n - 1:  # we reached the last building and no need to move further
                return 0
            
            if t[bricks][ladders] != -1:
                return t[bricks][ladders]
            
            if heights[idx] >= heights[idx + 1]:  # No need to use anything. Just move ahead
                t[bricks][ladders] = 1 + solve(idx + 1, bricks, ladders)
            else:
                byBrick = byLadder = 0
                if bricks >= heights[idx + 1] - heights[idx]:
                    byBrick = 1 + solve(idx + 1, bricks - (heights[idx + 1] - heights[idx]), ladders)
                    
                if ladders > 0:
                    byLadder = 1 + solve(idx + 1, bricks, ladders - 1)
                    
                t[bricks][ladders] = max(byBrick, byLadder)
            
            return t[bricks][ladders]
        
        return solve(0, bricks, ladders)


# ---------------------


//(GREEDY - FAIL. WRONG APPROACH. SEE below to find out why ?)
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        //greedily I'll use bricks because ladder helps me to jump to next
	//building irrespective of the height difference
        
        int n = heights.size();
        int i = 0;
        for( ; i<n-1 ; i++) {
            if(heights[i] >= heights[i+1]) {
                continue;
            }
            
            int diff = heights[i+1] - heights[i];
            if(bricks >= diff) {
                bricks -= diff;
                continue;
            }
            
            if(ladders > 0) {
                ladders--;
            } else
                break;
        }
        return i;
    }
};

Why above fails ?
Let's take an example :
[1,5,1,2,3,4,10000]
4
1
Initially:
bricks = 4
ladder = 1

        For, 1->5
        If I use bricks,
        bricks  = 4 - (5-1) = 0
        ladders = 1
        
        Now, 
        5->1 costs nothing
        
        For, 1->2
        I will use my only ladder
        bricks  = 0
        ladders = 0
        
        So, i reached till 2 (i.e. index 3 only) WRONG ANSWER
        
        -----------------------
        Now, if i had used ladder from 1->5, let's see what difference it
		would have created
        For, 1->5
        If I use ladder this time,
        bricks  = 4
        ladders = 0
        
        Now, 
        5->1 costs nothing
        
        For, 1->2
        I will use bricks
        bricks  = 4 - (2-1) = 3
        ladders = 0
        
        Now, for 2->3, I have bricks which can help me (as I need only (3-2) brick out of 3 bricks available)
        bricks  = 3 - (3-2) = 2
        ladders = 0
        
        For 3->4, I have bricks which can help me (as I need only (4-3) brick out of 2 bricks available)
        bricks  = 2 - (4-3) = 1
        ladders = 0
        
        Now, I can't go to 1000 from 4.
        So, I reached till 4 (i.e. index 5) RIGHT ANSWER
        
        So, what to do ?
        Just keep track of maximum amount of bricks you had used in past (say maxBricks). 
        Before, using a ladder, have look that the curr difference(diff = heights[i+1]-heights[i]) is smaller
        than last maximum amount of bricks you had used. So, we can regain those bricks and use a ladder    
        instead in the past. This way, you saved (maxBricks - diff) amount of bricks which can be used later



/***************************************************************** C++ *****************************************************************/
//Accepted Approach
//Using Lazy Greedy
//T.C : O(nlogn)
//S.C : O(n)
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {      
        int n = heights.size();
    
        priority_queue<int> pq;
        
        int i = 0;
        for(;i < n-1;i++) {
            if(heights[i] >= heights[i+1]) {
                continue;
            }
            
            int diff = heights[i+1]-heights[i];
            if(diff <= bricks) {
                bricks -= diff;
                pq.push(diff); //I used diff bricks here (keep track of it)
            } else if(ladders > 0) {
                if(!pq.empty()) {
                    int max_bricks_past = pq.top();
                    if(max_bricks_past > diff) {
                        //it means i unneccasrily used huge bricks in past. Let's get it back
                        bricks += max_bricks_past;
                        pq.pop();
                        pq.push(diff);
                        bricks -= diff;
                    }
                }
                ladders--; //either used in past or present
            } else {
                break;
            }
        }
        return i;
    }
};


//Approach-2 (Recursion + Memoization) - Memory Limit Exceed due to high constraint
//Link - https://github.com/MAZHARMIK/Interview_DS_Algo/blob/master/DP/Furthest%20Building%20You%20Can%20Reach.cpp


/***************************************************************** PYTHON *****************************************************************/
//Accepted Approach
//Using Lazy Greedy
//T.C : O(nlogn)
//S.C : O(n)

import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []  # Priority queue to track height differences
        
        for i in range(len(heights) - 1):
            if heights[i] >= heights[i + 1]:  # If current building height is greater or equal, continue
                continue
            diff = heights[i + 1] - heights[i]  # Calculate height difference between adjacent buildings
            bricks -= diff  # Use bricks to cover the height difference
            heapq.heappush(pq, -diff)  # Push negative difference to make it a max-heap
            
            if bricks < 0:  # If bricks are not enough
                bricks += -heapq.heappop(pq)  # Retrieve the maximum height difference used
                if ladders > 0:  # If ladders are available, use ladder to cover height difference
                    ladders -= 1
                else:  # If no more ladders available, return furthest reachable index
                    return i

        return len(heights) - 1  # Return the index of the last building if all are reachable

'''
