/*
1358. Number of Substrings Containing All Three Characters
Medium
Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1

Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.
*/

// SOLUTION

int numberOfSubstrings(string s) {
    int res = 0, n = s.length();

    for (int i = 0; i < n; i++) {
        int[] count = { 0, 0, 0 };
        for (int j = i; j < n; j++) {
            count[s.charAt(j) - 'a']++;
            if (count[0] > 0 && count[1] > 0 && count[2] > 0) {
                res += (n - j);
                break;
            }
        }
    }
    return res;
}

class Solution {
    public int numberOfSubstrings(String s) {
        // Extra
        /*
        Strings with:
        1. only a
        2. only b
        3. only c
        4. a & b
        5. b & c
        6. c & a
        7. a, b & c

        These variables represent the count of substrings 
        having only the characters mentioned in the names of the variables
        till the immediate last position
        
        int a = 0;
        int b = 0;
        int c = 0;
        int ab = 0;
        int bc = 0;
        int ca = 0;
        int abc = 0;

        int total = 0;

        for(char character: s.toCharArray()) {
            switch(character) {
                case 'a':
                    a++;
                    
                    abc += bc;
                    bc = 0;
                    
                    ab += b;
                    b = 0;
                    
                    ca += c;
                    c = 0;

                    break;
                case 'b':
                    b++;
                    
                    abc += ca;
                    ca = 0;

                    bc += c;
                    c = 0;

                    ab += a;
                    a = 0;

                    break;
                default:
                    c++;

                    abc += ab;
                    ab = 0;

                    bc += b;
                    b = 0;

                    ca += a;
                    a = 0;

                    break;
            }

            total += abc;
        }

        return total;
        */

        int[] lastSeen = { -1, -1, -1 };
        int res = 0, n = s.length();

        for (int i = 0; i < n; i++) {
            lastSeen[s.charAt(i) - 'a'] = i;
            // System.out.println(lastSeen[0] +"--"+ lastSeen[1] + "--" + lastSeen[2]);
            if (lastSeen[0] != -1 && lastSeen[1] != -1 && lastSeen[2] != -1) {

                System.out.println("all 3 ele ..");
                System.out.println(lastSeen[0] + "--" + lastSeen[1] + "--" + lastSeen[2]);
                res += (1 + Math.min(lastSeen[0], Math.min(lastSeen[1], lastSeen[2])));
                System.out.println(res);
            }
        }
        return res;
    }
}

// all 3 ele ..
// 0--1--2
// 1
// all 3 ele ..
// 3--1--2
// 3
// all 3 ele ..
// 3--4--2
// 6
// all 3 ele ..
// 3--4--5
// 10