"""
451. Sort Characters By Frequency

Medium

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
 

Constraints:

1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.

"""


# SOLUTION

class Solution:
    def frequencySort(self, s: str) -> str:
        # Solution - 1
        temp_dict = {}
        for ele in s:
            temp_dict[ele] = temp_dict.get(ele, 0) + 1

        # Sort the dictionary by values (counts)
        sorted_chars = sorted(temp_dict, key=lambda x: temp_dict[x], reverse=True)
        # sorted_chars
        # Input: s = "tree"
        # output -> ['e', 't', 'r']

        '''
        temp_dict.items(): This part gets the items of the dictionary temp_dict as a list of key-value pairs (tuples).

        sorted(...): This function sorts the list of tuples based on a custom key. The key parameter specifies the function to extract a comparison key from each element. In this case, lambda x: x[1] is a lambda function that takes a tuple x and returns its second element (x[1]), which is the value of the key-value pair.

        reverse=True: This parameter indicates that the sorting should be done in descending order.

        dict(...): Finally, the sorted list of tuples is converted back into a dictionary using the dict constructor.

        So, the overall effect of this line is to create a new dictionary (sorted_dict) where the items are sorted based on their values (the second element of each tuple) in descending order.
        '''

        ans = ""
        for char in sorted_chars:
            ans += (char*temp_dict[char])

        return ans

        # ---------------------------

        # Solution - 2
        temp_dict = {}

        for ch in s:
            temp_dict[ch] = temp_dict.get(ch, 0) + 1

        sorted_list = sorted(temp_dict.items(), key = lambda x: x[1], reverse = True)

        ans = ""
        for i in range(len(temp_dict)):
            ans += (sorted_list[i][0]*sorted_list[i][1])

        return ans
