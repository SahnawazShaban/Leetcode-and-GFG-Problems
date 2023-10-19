"""
Multiply two strings
Medium
Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Example 1:

Input:
s1 = "0033"
s2 = "2"
Output:
66
Example 2:

Input:
s1 = "11"
s2 = "23"
Output:
253
Your Task: You don't need to read input or print anything. Your task is to complete the function multiplyStrings() which takes two strings s1 and s2 as input and returns their product as a string.

Expected Time Complexity: O(n1* n2)
Expected Auxiliary Space: O(n1 + n2); where n1 and n2 are sizes of strings s1 and s2 respectively.

Constraints:
1 ≤ length of s1 and s2 ≤ 103

"""

# SOLUTION

class Solution:
    def multiplyStrings(self,s1,s2):
        # Check if either of the input strings is negative.
        is_negative = False
        if s1[0] == '-':
            is_negative = not is_negative
            s1 = s1[1:]
        if s2[0] == '-':
            is_negative = not is_negative
            s2 = s2[1:]

        # Initialize a list to store the product.
        result = [0] * (len(s1) + len(s2))

        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                # Calculate the product and add it to the appropriate position.
                prod = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                cur = prod + result[i + j + 1]
                result[i + j + 1] = cur % 10
                result[i + j] += cur // 10

        # Remove leading zeros from the result.
        while result and result[0] == 0:
            result.pop(0)

        # Convert the list of digits into a string.
        if not result:
            return "0"
        if is_negative:
            return "-" + "".join(map(str, result))
        return "".join(map(str, result))