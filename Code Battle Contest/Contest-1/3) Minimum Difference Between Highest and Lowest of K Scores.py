"""
3. Minimum Difference Between Highest and Lowest of K Scores
Easy
You are given a list of scores for a game. The game has a total of n rounds. Each score[i] represents the score of the player in the ith round.

You are also given an integer k, which represents the number of rounds the player can choose to play.

Return the minimum possible difference between the highest and lowest scores the player can achieve after playing k rounds.

Example 1:
Input
6 3
90 91 92 93 94 95

Output
2

Explaination:

The input scores are [90, 91, 92, 93, 94, 95].

The player can choose to play 3 rounds out of the 6 rounds.

The minimum possible difference between the highest and lowest scores the player can achieve after playing 3 rounds is 2, which can be obtained by playing rounds 90, 91, and 92.

Therefore, the output is 2.

Constraints:

The length of the input list scores is between 1 and 1000.
1 <= score[i] <= 10^5

The value of k is between 1 and the length of scores (inclusive).

Input Format:
A list of integers scores representing the scores of the player in each round (1 <= scores.length <= 1000).

An integer k representing the number of rounds the player can choose to play (1 <= k <= scores.length).

Output Format:
An integer representing the minimum possible difference between the highest and lowest scores the player can achieve after playing k rounds.

"""


# Solution 

## Sliding Window Problem

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n < k:
            return 0

        nums.sort()

        window = []
        window_max = 0
        ans = float('inf')
        for i in range(n+1):
            if k > 0:
                window.append(nums[i])
                k -= 1
                continue
            
            window_max = window[len(window)-1] - window[0]
            ans = min(ans,window_max)

            if i == n:
                break
            
            window.pop(0)
            window.append(nums[i])

        return ans

        # ---------------------------------------

        if len(nums) <= 1:
            return 0

        nums = sorted(nums)
        res = nums[k-1] - nums[0]

        for i in range(k, len(nums)):
            res = min(res, nums[i] - nums[i - k + 1])

        return res

        # ----------------------------------------

        n = len(scores)
        scores.sort()
        l,r = 0,k-1
        ans = float('inf')

        while r < n:
            ans = min(ans,scores[r]-scores[l])
            l += 1
            r += 1

        return ans

