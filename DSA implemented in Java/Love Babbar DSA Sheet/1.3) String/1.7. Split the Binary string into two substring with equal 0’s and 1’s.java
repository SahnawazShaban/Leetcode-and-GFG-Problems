/*
Split the binary string into substrings with equal number of 0s and 1s

Given a binary string str of length N, the task is to find the maximum count of consecutive substrings 
str can be divided into such that all the substrings are balanced i.e. they have equal number of 0s and 1s. 
If it is not possible to split str satisfying the conditions then print -1.

Input: str = “0100110101” 
Output: 4 
The required substrings are “01”, “0011”, “01” and “01”.
Input: str = “0111100010” 
Output: 3 

Input: str = “0000000000” 
Output: -1

*/

// SOLUTION

// Java implementation of the above approach
class Solution {
    static int maxSubStr(String str, int n) {
        // Solution - 1
        int count0 = 0, count1 = 0;

        // To store the count of maximum
        // substrings str can be divided into
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (str.charAt(i) == '0') {
                count0++;
            } else {
                count1++;
            }
            if (count0 == count1) {
                cnt++;
            }
        }

        // It is not possible to
        // split the string
        if (count0 != count1) {
            return -1;
        }
        return cnt;
    }
    // ''''''''''''''''''''''''''''''''''''''''

    // Solution - 2
    int ans = 0;
    int i = 0;
    Stack<Character> s = new Stack<>();s.push(str.charAt(i));i++;while(i<str.length())
    {
        while (i < str.length() && !s.empty() && s.peek() != str.charAt(i)) {
            s.pop();
            i++;
        }
        if (s.empty()) {
            ans++;
        }
        while (i < str.length() && (s.empty() || s.peek() == str.charAt(i))) {
            s.push(str.charAt(i));
            i++;
        }
    }if(s.empty())return ans;return-1;
    }

    // Driver code
    public static void main(String []args) 
    {
        String str = "0100110101";
        int n = str.length();

        System.out.println(maxSubStr(str, n));
    }
}
