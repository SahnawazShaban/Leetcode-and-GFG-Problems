"""
403. Frog Jump

Hard

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 
Example 1:
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:
Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
 

Constraints:
2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.

"""

# SOLUTION

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        mp = {stone: idx for idx, stone in enumerate(stones)}
        dp = [[-1]*(n+1) for i in range(n)]

        # curr_stone_index: The index of the current stone.
        # prev_jump: The jump value used to reach the previous stone.

        def solve(curr_stone_idx, prev_jump):
            if curr_stone_idx == n-1:
                return True

            if dp[curr_stone_idx][prev_jump] != -1:
                return dp[curr_stone_idx][prev_jump]

            result = False

            for next_jump in range(prev_jump-1, prev_jump+2):
                if next_jump > 0:
                    next_stone = stones[curr_stone_idx] + next_jump

                    if next_stone in mp:
                        result = result or solve(mp[next_stone], next_jump)

            dp[curr_stone_idx][prev_jump] = result

            return result

        if stones[1] != 1:
            return False

        return solve(0,0)


'''
Therefore, the combined time complexity is O(N^2) due to the nested loops and recursion, 
while the space complexity is O(N^2) because of the memoization table.
'''
