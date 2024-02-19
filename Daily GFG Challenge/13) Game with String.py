"""
Game with String

Medium

Given a string s of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of k characters. The value of a string is defined as the sum of squares of the count of each distinct character present in the string. 

Example 1:
Input: 
s = abccc, k = 1
Output: 
6
Explaination:
We remove c to get the value as 1^2 + 1^2 + 2^2

Example 2:
Input: 
s = aabcbcbcabcc, k = 3
Output: 
27
Explaination: 
We remove two 'c' and one 'b'. Now we get the value as 3^2 + 3^2 + 3^2.

Your Task:
You do not need to read input or print anything. Your task is to complete the function minValue() which takes s and k as input parameters and returns the minimum possible required value.

Expected Time Complexity: O(n+klog(p))  where n is the length of string and p is number of distinct alphabets and k number of alphabets to be removed. 
Expected Auxiliary Space: O(n)

Constraints:
0 ≤ k ≤ |string length| ≤ 10^5
"""

# Solution

class Solution:
    def minValue(self, s, k):
        
        temp_dict = {}
        
        for ch in s:
            temp_dict[ch] = temp_dict.get(ch, 0) + 1
            
        dict_list = []
        for val in temp_dict.values():
            dict_list.append(val)
            
            
        dict_list.sort(reverse = True)
        # print(dict_list)
        
        while k != 0:
            dict_list[0] -= 1
            dict_list.sort(reverse = True)
            
            # print(dict_list)
            k -= 1
        
        ans = 0
        
        for val in dict_list:
            ans += (val**2)
            
        return ans
    

# -------------------------------

import heapq
import math
class Solution:
    def minValue(self, s, k):
        # code here
        arr = [0]*26
        for c in s:
            arr[ord(c) - ord("a")]-=1
        heapq.heapify(arr)
        while k>0:
            ele = heapq.heappop(arr)
            ele += 1
            k -= 1
            heapq.heappush(arr,ele)
        res = 0
        for e in arr:
            res += math.pow(-e,2)
        return int(res)
    