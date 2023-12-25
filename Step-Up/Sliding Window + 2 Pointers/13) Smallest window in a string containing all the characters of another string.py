"""
Smallest window in a string containing all the characters of another string

Hard

Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index.
Note : All characters are in Lowercase alphabets. 

Example 1:
Input:
S = "timetopractice"
P = "toc"
Output: 
toprac
Explanation: "toprac" is the smallest substring in which "toc" can be found.

Example 2:
Input:
S = "zoomlazapzo"
P = "oza"
Output: 
apzo
Explanation: "apzo" is the smallest substring in which "oza" can be found.
Your Task:
You don't need to read input or print anything. Your task is to complete the function smallestWindow() which takes two string S and P as input paramters and returns the smallest window in string S having all the characters of the string P. In case there are multiple such windows of same length, return the one with the least starting index. 

Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(n) n = len(p)

Constraints: 
1 ≤ |S|, |P| ≤ 10^5

"""

# SOLUTION

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        # Solution - 1
        
        # Check if p is None
        if p is None:
            return ""

        # Length of string s
        n = len(s)
        
        # Left pointer of the window
        l = 0

        # Initialize variables to track the smallest window
        window_len = float('inf')
        res = [-1, -1]

        # Dictionaries to store character frequencies in p and the current window
        map = {}
        window = {}

        # Populate map dictionary with character frequencies in p
        for ele in p:
            map[ele] = map.get(ele, 0) + 1
            
        # Counters for characters in the current window
        have, need = 0, len(map)


        # Iterate through the characters in s using the right pointer r
        for r in range(n):
            # Update window dictionary with the current character
            window[s[r]] = window.get(s[r], 0) + 1

            # Check if the character at position r is in map and if the frequency
            # in window matches the required frequency in map
            if s[r] in map and window[s[r]] == map[s[r]]:
                have += 1

            # Enter a while loop to contract the window from the left until have equals need
            while have == need:
                # Update result and window length if the current window is smaller
                # than the previously recorded smallest window
                if (r - l + 1) < window_len:
                    res = [l, r]
                    window_len = (r - l + 1)

                # Decrement the frequency of the character at position l in window
                window[s[l]] -= 1

                # If the character at position l is in map and the frequency in window
                # is less than the required frequency in map, decrement the have counter
                if s[l] in map and window[s[l]] < map[s[l]]:
                    have -= 1

                # Move the left pointer l to the right
                l += 1

        # Retrieve the indices l and r from the result and return the substring of s
        # from l to r+1 if a valid window is found; otherwise, return an empty string
        l, r = res
        return s[l:r + 1] if window_len != float('inf') else -1
        
        '''
        Time Complexity:

        The algorithm uses two pointers (l and r) that traverse the input string s from left to right.
        Each character in s is processed once by the pointers.
        The while loop inside the outer for loop runs at most N times in total across all iterations of the outer loop, where N is the length of the input string s.
        Therefore, the overall time complexity is O(N).
        
        Space Complexity:
        
        The space complexity is primarily determined by the dictionaries map and window.
        The size of the map dictionary is proportional to the number of unique characters in the string p, denoted as len(map). In the worst case, this could be O(min(M, N)), where M is the length of string p and N is the length of string s.
        The window dictionary also grows with the size of the input string s, so its space complexity is O(N).
        The additional variables (have, need, l, r, res, window_len, etc.) have constant space complexity.
        Therefore, the overall space complexity is O(min(M, N) + N) or simply O(N).
        In conclusion, your code has a time complexity of O(N) and a space complexity of O(N) or O(min(M, N)) depending on the lengths of strings s and p.
        '''        
        
        # ------------------------------------
        
        # Solution - 2
        
        '''
        # Initialize an array to store the frequency of characters (a-z)
        mp = [0] * 26
        # Variable to track the distinct characters in p
        pos = 0
    
        # Populate the frequency array and count distinct characters in p
        for char in p:
            mp[ord(char) - ord('a')] += 1
            if mp[ord(char) - ord('a')] == 1:
                pos += 1
    
        # Pointers for the sliding window
        l = 0
        r = 0
        # Initialize result string and minimum length
        result_str = "-1"
        ans = float('inf')
    
        # Sliding window approach
        while r < len(s):
            # Update frequency array for the current character
            mp[ord(s[r]) - ord('a')] -= 1
    
            # If the frequency becomes 0, decrement the count of distinct characters
            if mp[ord(s[r]) - ord('a')] == 0:
                pos -= 1
    
            # Contract the window from the left until the window is valid
            while mp[ord(s[l]) - ord('a')] < 0:
                mp[ord(s[l]) - ord('a')] += 1
                l += 1
    
            # If all distinct characters are covered, update the result
            if pos == 0:
                if ans > r - l + 1:
                    ans = r - l + 1
                    result_str = s[l:r + 1]
    
            # Expand the window to the right
            r += 1
    
        return result_str
    '''
    
    # Time complexity: O(N), where N is the length of the input string s
    # Space complexity: O(1) since the frequency array has a fixed size (26 characters)
        
