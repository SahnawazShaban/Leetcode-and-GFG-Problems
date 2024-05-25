'''
39. Combination Sum

Medium

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 
Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40

'''

# SOLUTION

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def targetCombination(candidates, target, idx, temp):
            if idx == len(candidates):
                if target == 0:
                    result.append(temp[:])
                return

            if candidates[idx] <= target:
                temp.append(candidates[idx])
                # same index
                targetCombination(candidates, target - candidates[idx], idx, temp)
                temp.pop()

            targetCombination(candidates, target, idx+1, temp)

        result = []
        targetCombination(candidates, target, 0, [])

        return result
    

# Using DFS
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target: 
                return
            
            if cur == target:
                res.append(path)
                return
            
            for i in range(idx, len(candidates)):
                dfs(i, path+[candidates[i]], cur+candidates[i])

        dfs(0, [], 0)
        return res




# practice
def combinationSum(idx, arr, target, ds):
    if idx == len(arr):
        if target == 0:
            ans.append(ds[:])
        return

    if arr[idx] <= target:  # pick condition
        ds.append(arr[idx])
        combinationSum(idx, arr, target - arr[idx], ds)
        ds.pop()

    combinationSum(idx + 1, arr, target, ds)


arr = [2, 3, 6, 7]
ans = []
combinationSum(0, arr, 12, [])
print(ans)
