/*
Reverse an Array
Basic
You are given a string s. You need to reverse the string.

Example 1:
Input:
s = Geeks
Output: skeeG

Example 2:
Input:
s = for
Output: rof

Your Task:
You only need to complete the function reverseWord() that takes s as parameter and returns the reversed string.

Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).

Constraints:
1 <= |s| <= 10000
*/

// SOLUTION

class Reverse {
    // Complete the function
    // str: input string
    public static String reverseWord(String str) {
        char arr[] = str.toCharArray();

        int s = 0, e = arr.length - 1;

        while (s < e) {
            char temp = arr[s];
            arr[s] = arr[e];
            arr[e] = temp;
            s++;
            e--;
        }

        String res = "";
        for (char ch : arr) {
            res += ch;
        }

        return res;

        // Reverse the string str
        // StringBuilder sb = new StringBuilder(str);
        // return sb.reverse().toString();
    }
}

// ------------------------------------------------------------
// GFG Revision : https://www.geeksforgeeks.org/program-to-reverse-an-array/

// 1. Array Reverse Using an Extra Array (Non In-place):
// Brute Force Approach
public class ReverseArrayExtraArray {
    public static void reverseArrayExtraArray(int[] arr) {
        int[] reversedArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            reversedArr[i] = arr[arr.length - i - 1];
        }

        // Print reversed array
        System.out.print("Reversed Array: ");
        for (int i : reversedArr) {
            System.out.print(i + " ");
        }
    }

    public static void main(String[] args) {
        int[] originalArr = { 1, 2, 3, 4, 5 };
        reverseArrayExtraArray(originalArr);
    }
}

// Time Complexity: O(n)
// Copying elements to a new array is a linear operation.
// Auxiliary Space Complexity: O(n)
// Additional space is used to store the new array.

// 2. Array Reverse Using a Loop (In-place):
// 2 pointer approach

public class GFG {
    /*
     * Function to reverse arr[] from
     * start to end
     */
    static void rvereseArray(int arr[],
            int start, int end) {
        int temp;

        while (start < end) {
            temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }

    /*
     * Utility that prints out an
     * array on a line
     */
    static void printArray(int arr[],
            int size) {
        for (int i = 0; i < size; i++)
            System.out.print(arr[i] + " ");

        System.out.println();
    }

    // Driver code
    public static void main(String args[]) {

        int arr[] = { 1, 2, 3, 4, 5, 6 };
        printArray(arr, 6);
        rvereseArray(arr, 0, 5);
        System.out.print("Reversed array is \n");
        printArray(arr, 6);

    }
}

// Time Complexity: O(n)
// The loop runs through half of the array, so it’s linear with respect to the
// array size.
// Auxiliary Space Complexity: O(1)
// In-place reversal, meaning it doesn’t use additional space.

// 3. Array Reverse Inbuilt Methods (Non In-place):

import java.util.Arrays;

public class ArrayReverse {
    public static void main(String[] args) {
        int[] originalArray = { 1, 2, 3, 4, 5 };

        // Using inbuilt method in Java
        int[] reversedArray = new int[originalArray.length];
        for (int i = 0; i < originalArray.length; i++) {
            reversedArray[i] = originalArray[originalArray.length - 1 - i];
        }

        // Print the reversed array
        System.out.println(Arrays.toString(reversedArray));
    }
}

// Time Complexity:O(n), The reverse method typically has linear time
// complexity.
// Auxiliary Space Complexity: O(n), Additional space is used to store the
// reversed array.

// 4. Array Reverse Recursion (In-place or Non In-place):

// Recursive Java Program to reverse an array
import java.io.*;

class ReverseArray {

    /* Function to reverse arr[] from start to end */
    static void rvereseArray(int arr[], int start, int end) {
        int temp;
        if (start >= end)
            return;
        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        rvereseArray(arr, start + 1, end - 1);
    }

    /* Utility that prints out an array on a line */
    static void printArray(int arr[], int size) {
        for (int i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
        System.out.println("");
    }

    /* Driver function to check for above functions */
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5, 6 };
        printArray(arr, 6);
        rvereseArray(arr, 0, 5);
        System.out.println("Reversed array is ");
        printArray(arr, 6);
    }
}

// Time Complexity: O(n). The recursion goes through each element once, so it’s
// linear.
// Auxiliary Space Complexity: O(n). for non in-place, O(log n) for in-place
// (due to recursion stack).

// 5. Array Reverse Stack (Non In-place):

import java.util.Stack;

public class ReverseArrayUsingStack {
    public static void reverseArrayUsingStack(int[] arr) {
        Stack<Integer> stack = new Stack<>();

        // Push elements onto the stack
        for (int element : arr) {
            stack.push(element);
        }

        // Pop elements from the stack to reverse the array
        for (int i = 0; i < arr.length; i++) {
            arr[i] = stack.pop();
        }
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5 };

        reverseArrayUsingStack(arr);

        System.out.print("Reversed Array: ");
        for (int element : arr) {
            System.out.print(element + " ");
        }
    }
}

// Time Complexity: O(n)
// Pushing and popping each element onto/from the stack requires linear time.
// Auxiliary Space Complexity: O(n)
// Additional space is used to store the stack.
