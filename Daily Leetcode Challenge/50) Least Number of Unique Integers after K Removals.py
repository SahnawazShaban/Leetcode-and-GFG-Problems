"""
1481. Least Number of Unique Integers after K Removals

Medium

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length

"""


# SOLUTION

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        temp_dict = {}

        for val in arr:
            temp_dict[val] = temp_dict.get(val, 0) + 1

        sorted_list = sorted(temp_dict.items(), key = lambda x:x[1], reverse = False)
        # print(sorted_list) -> [(4, 1), (2, 1), (1, 2), (3, 3)]

        ans = len(sorted_list)

        for key, count in sorted_list:
            if count > k:
                break
            k -= count
            ans -= 1

        return ans

        # ----------------------------

        # SOLUTION - 2
        '''
        C = Counter(arr).most_common()
        res = len(C)
        for _, cnt in reversed(C):
            if cnt > k: 
                break
            k -= cnt
            res -= 1
        return res
        '''

        # -----------------------------
        # SOLUTION - 3

        '''
        c = Counter(arr)
        s = sorted(arr,key = lambda x:(c[x],x))
        return len(set(s[k:]))
        '''

        # --------------------------------
        # SOLUTION - 4

        '''
        hp = list(collections.Counter(arr).values())
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)
        return len(hp) + (k < 0) 
        '''