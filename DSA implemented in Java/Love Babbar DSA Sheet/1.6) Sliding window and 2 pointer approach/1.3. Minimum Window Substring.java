/*
76. Minimum Window Substring
Hard
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 
Constraints:
m == s.length
n == t.length
1 <= m, n <= 10^5
s and t consist of uppercase and lowercase English letters.
 
Follow up: Could you find an algorithm that runs in O(m + n) time?
*/


// SOLUTION

class Solution {
    public String minWindow(String s, String t) {
        int n = s.length();

        if (t.length() > n)
            return "";
        HashMap<Character, Integer> mp = new HashMap<>();

        int r=0, l=0;
        int minWindowSize = Integer.MAX_VALUE;

        int starti = 0;

        int requiredLen = t.length();

        for (int i = 0; i < requiredLen; i++){
            char ch = t.charAt(i);
            mp.put(ch, mp.getOrDefault(ch, 0)+1);
        }
        
        // story starts
        while (r < n){
            char ch = s.charAt(r);
            if (mp.containsKey(ch) && mp.get(ch) > 0){
                requiredLen--;
            }

            mp.put(ch, mp.getOrDefault(ch, 0)-1);

            while (requiredLen == 0){
                // start shrinking the window
                int curWindowSize = r-l+1;

                if (minWindowSize > curWindowSize){
                    minWindowSize = curWindowSize;
                    starti = l;
                }

                char prevChar = s.charAt(l);

                mp.put(prevChar, mp.getOrDefault(prevChar, 0)+1);

                if (mp.containsKey(prevChar) && mp.get(prevChar) > 0){
                    requiredLen++;
                }
                l++;
            }
            r++;
        }
        return minWindowSize == Integer.MAX_VALUE ? "" : s.substring(starti, starti + minWindowSize);
    }
}
/*
Time Complexity:

Initializing the hashmap with characters from string t: This operation takes O(t), where t is the length of string t.
The while loop iterates over each character in string s once: This operation takes O(n), where n is the length of string s.
Within the while loop, there's another while loop that might iterate multiple times, but it's bounded by the length of string s: This nested while loop also contributes O(n) to the time complexity.
Therefore, the overall time complexity is O(n + t), where n is the length of string s and t is the length of string t.


Space Complexity:

The hashmap mp stores characters from string t along with their counts: This hashmap would take O(t) space.
Additionally, there are a few integer variables and constants used, which would require constant space.
Therefore, the overall space complexity is O(t) due to the hashmap.
In summary:

Time Complexity: O(n + t)
Space Complexity: O(t)
*/
