"""
Minimum Window Subsequence

Hard

Given strings str1 and str2, find the minimum (contiguous) substring W of str1, so that str2 is a subsequence of W.

If there is no such window in str1 that covers all characters in str2, return the empty string "". If there are multiple such minimum-length windows, return the one with the left-most starting index.

Example 1:
Input: 
str1: geeksforgeeks
str2: eksrg
Output: 
eksforg
Explanation: 
Eksforg satisfies all required conditions. str2 is its subsequence and it is longest and leftmost among all possible valid substrings of str1.

Example 2:
Input: 
str1: abcdebdde
str2: bde
Output: 
bcde
Explanation: 
"bcde" is the answer and "deb" is not a smaller window because the elements of T in the window must occur in order.

Your Task:
Complete the function string minWindow(string str1, string str2), which takes two strings as input and returns the required valid string as output.

Expected Time Complexity: O(N^2).
Expected Auxiliary Space: O(N^2).

Constraints:
0 <= str1 <= 1000
0 <= str2 <= 100

"""

# SOLUTION

class Solution:
    def minWindow(self, str1, str2):
        # Solution - 1 - Brute Force - TLE
        
        '''
        if len(str1) == 0 or len(str2) == 0:
            return ""
            
        # Variables to track window properties
        l = r = 0
        length = float('inf')
        ans = ""
    
        # Iterate through each character in str1
        while r < len(str1):
            tidx = 0
            
            # Go forward
            while r < len(str1):
                
                if str1[r] == str2[tidx]:
                    tidx += 1
                    
                if tidx == len(str2):
                    break
                
                r += 1
                
                
            # GO backward
                
            l = r
            tidx = len(str2)-1
            
            while l >= 0:
                
                if str1[l] == str2[tidx]:
                    tidx -= 1
                    
                if tidx < 0:
                    break
                    
                l -= 1
                
            if (r-l+1) < length:
                length = r-l+1
                ans = str1[l:r+1]
                
            # Repeat the process
            r = l+1
    
        return ans
        '''
        # Solution - 2 - Optimal - Run with all test cases
        
        s1 = 0
        s2 = 0
        s1len = len(str1)
        s2len = len(str2)
        start = 0
        end = 0
        minlen = float('inf')
        minstr = ""
    
        while s1 < s1len and s2 < s2len:
            # Match the characters
            if str1[s1] == str2[s2]:
                # If the last character of str2 is matched
                if s2 == s2len - 1:
                    end = s1
                    # Move s1 and s2 back to find the starting index of the matching substring
                    while s2 >= 0:
                        if str2[s2] == str1[s1]:
                            s2 -= 1
                        s1 -= 1
        
                    start = s1 + 1
                    # Update the minimum window if the current window is smaller
                    if minlen > end - start + 1:
                        minlen = end - start + 1
                        minstr = str1[start:end + 1]
        
                    # Move s1 to the next position and reset s2
                    s1 = s1 + 1
                    s2 = 0
                else:
                    # Move to the next character in str2
                    s2 += 1
            # Move to the next character in str1
            s1 += 1
    
        return "" if minlen == float('inf') else minstr
            
            
'''   
Time Complexity:
The time complexity is primarily determined by the while loop, which iterates through the characters of str1 once. In the worst case, each character in str1 is compared with each character in str2. Therefore, the time complexity is O(len(str1) * len(str2)).

Space Complexity:
The space complexity is determined by the variables used to keep track of indices, lengths, and the minimum window substring. These variables use constant space, and they do not depend on the input size. Therefore, the space complexity is O(1) or constant.
'''