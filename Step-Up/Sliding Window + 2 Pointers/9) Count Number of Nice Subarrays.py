"""
1248. Count Number of Nice Subarrays

Medium

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.


Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length

"""

# SOLUTION

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Solution - 1
        n = len(nums)
        r = l = 0
        ans = count = 0
        odd = 0

        while r < n:
            if nums[r] % 2 != 0:
                odd += 1
                count = 0

            while odd == k:
                count += 1
                odd -= (nums[l]&1)
                l += 1
            
            ans += count
            r += 1

        return ans

        # --------------------------------
        # Solution - 2
        '''
        right ,left = 0,0
        ans = 0 
        odd_cnt = 0
        ans = 0
        cur_sub_cnt = 0
        for right in range(len(nums)):
            
            if nums[right]%2 == 1:
                odd_cnt += 1
                cur_sub_cnt = 0
                
            while odd_cnt == k:
                if nums[left]%2 == 1:
                    odd_cnt -= 1
                cur_sub_cnt += 1
                left += 1
                
            ans += cur_sub_cnt
            
        return ans  
        '''

        # solution - 3
        '''
        dic = { 0: 1 }
		cnt = res = 0
		for idx, num in enumerate(nums):
			if num % 2 == 1:
				cnt += 1

			if cnt - k in dic:
				res += dic[cnt-k]

			dic[cnt] = dic.get(cnt, 0) + 1

		return res

        ----------------------

        Time Complexity:
        The time complexity of the provided code is O(N), where N is the length of the input array nums. The for loop iterates through each element of the array exactly once, and the operations inside the loop (dictionary updates and checks) take constant time.

        Space Complexity:
        The space complexity is O(N) in the worst case. This is because the dictionary (dic) can have up to N distinct keys in the worst case, where each key corresponds to a different count of odd numbers encountered. The values in the dictionary are counts, and at most, you will have one entry for each count, resulting in a total space usage proportional to the length of the input array.

        In summary:

        Time complexity: O(N)
        Space complexity: O(N)
        '''
        
'''
The time complexity of the provided code is O(N), where N is the length of the input array nums. This is because the code uses two pointers (l and r) that traverse the array from left to right, and the inner while loop runs at most N times in total. Each pointer move and each check in the while loop takes constant time.

The space complexity is O(1) because the code uses a constant amount of extra space regardless of the size of the input array. The variables n, r, l, ans, count, and odd all occupy constant space.

***************

The worst-case time complexity of the provided code is still O(N), where N is the length of the input array nums. This is because each element in the array is processed by the two pointers exactly once. The inner while loop might seem like it could result in a higher time complexity, but the key observation is that the pointers l and r each move from left to right, and each element is considered at most twice (once for the left pointer and once for the right pointer).

Therefore, the overall worst-case time complexity is still linear in the size of the input array.
'''
