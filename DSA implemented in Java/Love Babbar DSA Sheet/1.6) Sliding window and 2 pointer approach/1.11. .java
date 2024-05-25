/*
Convert a sentence into its equivalent mobile numeric keypad sequence
Easy
Given a sentence in the form of a string in uppercase, convert it into its equivalent mobile numeric keypad sequence. Please note there might be spaces in between the words in a sentence and we can print spaces by pressing 0.

Example 1:
Input:
S = "GFG"
Output: 43334
Explanation: For 'G' press '4' one time.
For 'F' press '3' three times.

Example 2:
Input:
S = "HEY U"
Output: 4433999088
Explanation: For 'H' press '4' two times.
For 'E' press '3' two times. For 'Y' press '9' 
three times. For white space press '0' one time.
For 'U' press '8' two times.
 

Your Task:  
You dont need to read input or print anything. Complete the function printSequence() which takes a string as input parameter and returns its equivalent mobile numeric keypad sequence as a string.
 

Expected Time Complexity: O(Length of String)
Expected Auxiliary Space: O(Length of String)
 

Constraints:
1 <= Length of String <= 10^5
Characters of string can be empty space or capital alphabets.
*/

// SOLUTION

class Solution {
    String printSequence(String S) {
        HashMap<Character, String> map = new HashMap<>();

        map.put('A', "2");
        map.put('B', "22");
        map.put('C', "222");
        map.put('D', "3");
        map.put('E', "33");
        map.put('F', "333");
        map.put('G', "4");
        map.put('H', "44");
        map.put('I', "444");
        map.put('J', "5");
        map.put('K', "55");
        map.put('L', "555");
        map.put('M', "6");
        map.put('N', "66");
        map.put('O', "666");
        map.put('P', "7");
        map.put('Q', "77");
        map.put('R', "777");
        map.put('S', "7777");
        map.put('T', "8");
        map.put('U', "88");
        map.put('V', "888");
        map.put('W', "9");
        map.put('X', "99");
        map.put('Y', "999");
        map.put('Z', "9999");
        map.put(' ', "0");
        StringBuilder st = new StringBuilder();

        for (int i = 0; i < S.length(); i++) {
            st.append(map.get(S.charAt(i)));
        }
        return st.toString();
    }
}
