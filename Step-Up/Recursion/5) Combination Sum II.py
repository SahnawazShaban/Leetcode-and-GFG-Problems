'''
40. Combination Sum II

Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
 

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''

# SOLUTION

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        def backtrack(candidates, target, idx, temp):
            if idx == len(candidates):
                if temp not in result and target == 0:
                    result.append(temp[:])
                return
            
            if candidates[idx] <= target:
                if candidates[idx] not in temp:
                    temp.append(candidates[idx])

                    backtrack(candidates, target - candidates[idx], idx, temp)
                    temp.pop()

            backtrack(candidates, target, idx+1, temp)

        result = []
        candidates.sort()
        backtrack(candidates, target, 0, [])

        return result
        '''



        def backtrack(candidates, target, idx, temp):
            if target == 0:
                result.append(temp[:])
                return
            
            for i in range(idx, len(candidates)):
                # Skip duplicates
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                # Skip candidates that are too large
                if candidates[i] > target:
                    break  # Since the array is sorted, we can stop checking further

                temp.append(candidates[i])
                backtrack(candidates, target - candidates[i], i + 1, temp)
                temp.pop()

        result = []
        candidates.sort()
        backtrack(candidates, target, 0, [])

        return result

# -------------------------------------

# Using DFS

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i+1, path+[candidates[i]], cur+candidates[i])
        dfs(0, [], 0)
        return res
    