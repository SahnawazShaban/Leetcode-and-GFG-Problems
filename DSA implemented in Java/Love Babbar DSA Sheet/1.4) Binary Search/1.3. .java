/*
Print all the duplicate characters in a string
Given a string S, the task is to print all the duplicate characters with their occurrences in the given string.

Example:
Input: S = “geeksforgeeks”
Output:
e, count = 4
g, count = 2
k, count = 2
s, count = 2

*/

// SOLUTION

class GFG {

    // Java program to count all duplicates
    // from string using maps
    static void printDups(String str) {
        Map<Character, Integer> count = new HashMap<>();
        for (int i = 0; i < str.length(); i++) {
            if (count.containsKey(str.charAt(i)))
                count.put(str.charAt(i), count.get(str.charAt(i)) + 1);
            else
                count.put(str.charAt(i), 1);
            // increase the count of characters by 1
        }

        for (Map.Entry<Character, Integer> mapElement : count.entrySet()) { // iterating through the unordered map
            if (mapElement.getValue() > 1) // if the count of characters is greater than 1 then duplicate found
                System.out.println(mapElement.getKey() + ", count = " + mapElement.getValue());
        }
    }

    /* Driver program to test above function */
    public static void main(String args[]) {
        String str = "test string";
        printDups(str);
    }
}

// Output:
// t, count = 3
// s, count = 2

// Time Complexity: O(N), where N = length of the string passed and it takes
// O(1) time to insert and access any element in an unordered map

// Auxiliary Space: O(K), where K = size of the map (0<=K<=input_string_length),
// in worst case space will be O(N).

// ...................................................

import java.util.*;

public class Main {

    public static void printDuplicates(String str) {
        int len = str.length();

        // Sorting the string
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        String sortedStr = new String(chars);

        // Loop through the sorted string to find duplicates
        for (int i = 0; i < len; i++) {
            int count = 1;

            // Counting the occurrences of each character
            while (i < len - 1
                    && sortedStr.charAt(i) == sortedStr.charAt(i + 1)) {
                count++;
                i++;
            }

            // Printing the duplicate character and its
            // count
            if (count > 1) {
                System.out.println(sortedStr.charAt(i) + ", count = " + count);
            }
        }
    }

    public static void main(String[] args) {
        String str = "test string";
        printDuplicates(str);
    }
}

// Time Complexity: O(N*logN), where n is the length of the string
// Auxiliary Space: O(1), if you observe we did not use any extra space.
