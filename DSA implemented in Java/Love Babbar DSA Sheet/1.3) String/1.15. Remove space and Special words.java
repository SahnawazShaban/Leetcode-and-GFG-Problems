/*
Remove all characters other than alphabets

Given a string S, remove all the characters other than the alphabets.

Example 1:
Input: S = "$Gee*k;s..fo, r'Ge^eks?"
Output: GeeksforGeeks
Explanation: Removed charcters other than alphabets. 
 
Example 2:
Input:  S = "{{{}}> *& ^%*)"
Output: -1
Explanation: There are no alphabets.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function removeSpecialCharacter() which takes string S as input parameter and returns the resultant string. Return "-1" if no alphabets remain.

Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)

Constraints:
1 <= |S| <= 10^5

------------------------------------------------

Remove Spaces

Given a string, remove spaces from it. 

Example 1:
Input:
S = "geeks  for geeks"
Output: geeksforgeeks
Explanation: All the spaces have been removed.

Example 2:
Input: 
S = "    g f g"
Output: gfg
Explanation: All the spaces including the leading ones have been removed.

Your Task:
You don't need to read input or print anything. Your task is to complete the function modify() which takes the string S as input and returns the resultant string by removing all the white spaces from S.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1<=|S|<=105
*/

// SOLUTION

// Remove all characters other than alphabets
class Solution{
    String removeSpecialCharacter(String s) {
        String str = s.replaceAll("[^a-zA-Z]", "");
        
        if(str.length() == 0){
            return "-1";
        }
        
        return str;
    }
}

// ----------------------------------------

// Remove Spaces
class Solution
{
    String modify(String S)
    {
        // StringBuilder str = new StringBuilder();
        
        // for(int i = 0; i < S.length(); i++){
        //     char ch = S.charAt(i);
        //     if(ch != ' '){
        //         str.append(ch);
        //     }
        // }
        
        // return str.toString();

        // OR
        
        return S.replace(" ","");
    }
}