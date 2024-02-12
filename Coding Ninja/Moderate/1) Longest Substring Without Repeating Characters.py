"""
 Longest Substring Without Repeating Characters

Moderate

Given a string input of length n, find the length of the longest substring without repeating characters i.e return a substring that does not have any repeating characters.

Substring is the continuous sub-part of the string formed by removing zero or more characters from both ends.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1<= n <=10^5
Time Limit: 1 sec

Sample Input 1:
abcabcbb 
Sample Output1:
3
Explanation For Sample Input 1:
Substring "abc" has no repeating character with the length of 3.

Sample Input 2:
aaaa
Sample Output 2:
1

"""


# Solution 

def uniqueSubstrings(input ) :
    # abcabcbb
    #  l      
    #    r

    l, r = 0, 0
    max_len = float('-inf')
    temp_dict = {}

    while r < len(input):
        if input[r] in temp_dict:
            l = max(l, temp_dict[input[r]]+1)

        max_len = max(max_len, r-l+1)
        temp_dict[input[r]] = r
        r += 1

    return max_len