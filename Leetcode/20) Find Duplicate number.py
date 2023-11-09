"""
287. Find the Duplicate Number

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2


Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?

"""

# SOLUTION

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arrP = []
        arrN = []
        for val in nums:
            if val < 0:
                arrN.append(val)
            else:
                arrP.append(val)
        
        j, k = 0, 0
        for i in range(n):
            if i%2 == 0:
                nums[i] = arrP[j]
                j += 1
            else:
                nums[i] = arrN[k]
                k += 1

        return nums
    
        '''
        The given code rearranges the elements in the input nums list such that positive numbers appear at even indices, and negative numbers appear at odd indices. This is achieved by separating the positive and negative numbers into two separate lists (arrP and arrN) and then filling the nums list by alternately taking elements from these two lists.
The time complexity of this code is O(n), where n is the length of the nums list. The code loops through the nums list once to separate positive and negative numbers and once again to rearrange the elements, both of which are linear operations.
The space complexity is also O(n) because it uses two additional lists, arrP and arrN, to store the positive and negative numbers. The size of these lists depends on the number of positive and negative numbers in the nums list, which can be at most n.
Overall, the code has an efficient time and space complexity for rearranging the elements in the desired manner.
        '''

        # ------------------------------------

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        temp_dict = {}

        for val in nums:
            temp_dict[val] = temp_dict.get(val,0)+1
        
        for key, count in temp_dict.items():
            if count > 1:
                duplicate = key
        
        return duplicate
        

        # ------------------------------------------------------------------------------------

        '''
        Comprehensive Guide to Solving "Find the Duplicate Number"
        Introduction & Problem Statement
        Given an array of integers, nums\text{nums}nums, containing n+1n + 1n+1 integers where each integer is in the range [1,n][1, n][1,n] inclusive, find the one repeated number in the array. The challenge lies in solving the problem without modifying the array nums\text{nums}nums and using only constant extra space. This problem is a classic example of array manipulation and number theory combined, making it an interesting problem to tackle.

        Key Concepts and Constraints
        What Makes This Problem Unique?
        Array Representation:
        The array contains n+1n + 1n+1 integers, each falling within the range [1,n][1, n][1,n].

        Single Duplication:
        Only one integer is repeated in the array, and it can be repeated more than once.

        Constraints:

        Array length: n+1n + 1n+1, where 1≤n≤1051 \leq n \leq 10^51≤n≤10 
        5
        
        1≤nums[i]≤n1 \leq \text{nums}[i] \leq n1≤nums[i]≤n
        Six Primary Strategies to Solve the Problem:
        Set/Hash Table: Use a hash table to track the numbers that have appeared so far.
        Count Array: Use an auxiliary array to count the frequency of each number.
        Marking in Array: Negate the value at the index corresponding to each number in the array.
        Floyd's Cycle Detection (Fast-Slow Pointers): Treat the array as a linked list to find a cycle.
        Binary Search: Count the numbers less than or equal to the middle element to find the duplicate.
        Sort: Sort the array and check adjacent elements for duplicates.
        In-Depth Strategies for Finding the Duplicate Number in an Array
        Live Coding & comparing 6 Approaches


        1. Set/Hash Table Approach
        Detailed Logic:
        Initialize an empty set seen.
        Traverse through the array nums.
        For each element num in nums, check if it exists in seen.
        If it does, return num as the duplicate.
        Otherwise, add num to seen.
        Pros:
        Extremely straightforward to implement.
        No need to sort or modify the original array.
        Cons:
        This approach requires extra space for the set, which violates the problem's constraint of constant extra space.
        Time and Space Complexity:
        Time Complexity: O(n)O(n)O(n) because we iterate through the array once.
        Space Complexity: O(n)O(n)O(n) for storing the set.
        Code Set
        class Solution:
            def findDuplicate(self, nums: List[int]) -> int:
                seen = set()
                for num in nums:
                    if num in seen:
                        return num
                    seen.add(num)


        2. Count Array Approach
        Detailed Logic:
        Initialize an auxiliary count array cnt with zeros. Its size will be n+1n+1n+1 to accommodate all possible numbers.
        Traverse through the array nums.
        For each element num in nums, increment cnt[num] by 1.
        Check if cnt[num] exceeds 1; if yes, return num as the duplicate.
        Pros:
        Implementation is simple and direct.
        Cons:
        Extra space is used for the count array, which contradicts the constraint of constant extra space.
        Time and Space Complexity:
        Time Complexity: O(n)O(n)O(n) due to a single pass through the array.
        Space Complexity: O(n)O(n)O(n) for the count array.
        Code Count
        class Solution:
            def findDuplicate(self, nums: List[int]) -> int:
                cnt = [0] * (len(nums) + 1)
                for num in nums:
                    cnt[num] += 1
                    if cnt[num] > 1:
                        return num
                return len(nums)


        3. Marking in Array Approach
        Detailed Logic:
        Traverse the array nums.
        For each element num, take its absolute value as an index (idx = abs(num)).
        If nums[idx] is negative, then idx is the duplicate number.
        Otherwise, negate nums[idx].
        Pros:
        Doesn't use any extra space other than the input array.
        Cons:
        Modifies the original array, which is disallowed by the problem constraints.
        Time and Space Complexity:
        Time Complexity: O(n)O(n)O(n) for a single pass through the array.
        Space Complexity: O(1)O(1)O(1) as no extra space is used.
        Code Mark
        class Solution:
            def findDuplicate(self, nums: List[int]) -> int:
                for num in nums:
                    idx = abs(num)
                    if nums[idx] < 0:
                        return idx
                    nums[idx] = -nums[idx]
                return len(nums)


        4. Fast-Slow Pointers Approach (Floyd's Cycle Detection)
        Detailed Logic Behind the Fast-Slow Pointers Approach
        Step 1: Initialize Pointers
        First, we initialize two pointers, slow and fast, both set to nums[0]. This is the starting point for both pointers, and it's done to set up the conditions for Floyd's cycle detection algorithm.

        Step 2: Detect a Cycle
        In this step, we enter a while loop where the slow pointer moves one step at a time (slow = nums[slow]), while the fast pointer moves two steps (fast = nums[nums[fast]]). The loop continues until both pointers meet at some point within the cycle. Note that this meeting point is not necessarily the duplicate number; it's just a point inside the cycle.

        Why does this happen? Because there is a duplicate number, there must be a cycle in the 'linked list' created by following nums[i] as next elements. Once a cycle is detected, the algorithm breaks out of this loop.

        Step 3: Find the Start of the Cycle (Duplicate Number)
        After identifying a meeting point inside the cycle, we reinitialize the slow pointer back to nums[0]. The fast pointer stays at the last meeting point. Now, we enter another while loop where both pointers move one step at a time. The reason behind this is mathematical: according to Floyd's cycle detection algorithm, when both pointers move at the same speed, they will eventually meet at the starting point of the cycle. This is the duplicate number we are looking for.

        Step 4: Return the Duplicate Number
        Finally, when the slow and fast pointers meet again, the meeting point will be the duplicate number, and we return it as the output.

        Pros:
        Adheres to the constant space constraint.
        Doesn't modify the original array.
        Cons:
        The logic can be slightly tricky to grasp initially.
        Time and Space Complexity:
        Time Complexity: O(n)O(n)O(n), where nnn is the length of the array.
        Space Complexity: O(1)O(1)O(1) as no extra space is required.
        Code Fast Slow Pointers
        class Solution:
            def findDuplicate(self, nums: List[int]) -> int:
                slow = nums[0]
                fast = nums[0]

                while True:
                    slow = nums[slow]
                    fast = nums[nums[fast]]
                    if slow == fast:
                        break

                slow = nums[0]
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                    
                return slow


        5. Binary Search Approach
        Detailed Logic:
        Initialize low to 1 and high to nnn.
        Run a binary search loop until low < high:
        Calculate mid as the midpoint between low and high.
        Count elements in the array that are less than or equal to mid.
        If the count is greater than mid, set high = mid. Otherwise, set low = mid + 1.
        Pros:
        No modification to the original array.
        Cons:
        Somewhat more complex to understand due to binary search mechanics.
        Time and Space Complexity:
        Time Complexity: O(nlog⁡n)O(n \log n)O(nlogn) due to binary search combined with array scanning.
        Space Complexity: O(1)O(1)O(1) as no extra space is needed.
        Code Binary Search
        class Solution:
            def findDuplicate(self, nums: List[int]) -> int:
                low, high = 1, len(nums) - 1
                
                while low < high:
                    mid = (low + high) // 2
                    count = 0
                    for num in nums:
                        if num <= mid:
                            count += 1
                    if count > mid:
                        high = mid
                    else:
                        low = mid + 1
                        
                return low


        6. Sort Approach
        Detailed Logic:
        Sort the nums array in ascending order.
        Traverse the sorted array and compare adjacent elements.
        If two adjacent elements are equal, return one of them as the duplicate.
        If no duplicate is found, return the length of the array (this should not happen under the problem constraints).
        Pros:
        Simple to understand and implement.
        Utilizes Python's efficient built-in sorting algorithm.
        Cons:
        Modifies the original array by sorting it.
        Not the most time-efficient solution for this problem.
        Time and Space Complexity:
        Time Complexity: O(nlog⁡n)O(n \log n)O(nlogn) due to sorting.
        Space Complexity: O(1)O(1)O(1) if sorting is done in-place, otherwise O(n)O(n)O(n).
        Code Sort
        class Solution:
            def findDuplicate(self, nums: List[int]) -> int:
                nums.sort()
                for i in range(1, len(nums)):
                    if nums[i] == nums[i-1]:
                        return nums[i]
                return len(nums)
                '''