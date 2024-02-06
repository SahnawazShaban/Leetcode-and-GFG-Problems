"""
49. Group Anagrams

Medium

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

"""


# SOLUTION

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp_dict = {}
        ans = []
        for s in strs:
            sorted_word = ''.join(sorted(s))
            if sorted_word in temp_dict:
                ans[temp_dict[sorted_word]].append(s)
            else:
                temp_dict[sorted_word] = len(ans)
                ans.append([s]) # # Append a list containing s

        return ans
    

'''
Time Complexity:
Iterating through each string in the input list strs requires O(n) time, 
where n is the total number of characters in all strings combined.
Sorting each string takes O(klogk) time, where k is the maximum length of a string in strs.
For each sorted string, the dictionary lookup operation takes O(1) time on average.
Therefore, the overall time complexity is O(n * klogk) because of the sorting operation.

Space Complexity:
temp_dict stores mappings of sorted strings to their corresponding group index. 
The number of entries in temp_dict is bounded by the number of unique sorted strings, 
which is at most the number of strings in strs. Therefore, the space complexity of temp_dict is O(n).
ans stores the grouped anagrams. In the worst case, each string in strs is unique, 
so ans will contain n lists, each containing a single string. Therefore, the space complexity of ans is O(n).
Overall, the space complexity is O(n) due to the storage requirements of temp_dict and ans.

In summary:

Time Complexity: O(n * klogk)
Space Complexity: O(n)

Your code has an efficient time complexity due to the use of a dictionary for quick lookup and sorting strings. 
However, the space complexity could be improved slightly by optimizing the data structures used to store the grouped anagrams.
'''
    