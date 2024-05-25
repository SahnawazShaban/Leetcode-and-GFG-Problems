/*
Next Permutation

Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers. If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in an ascending order. You are given an list of numbers arr[ ] of size N.

Example 1:
Input: N = 6
arr = {1, 2, 3, 6, 5, 4}
Output: {1, 2, 4, 3, 5, 6}
Explaination: The next permutation of the given array is {1, 2, 4, 3, 5, 6}.

Example 2:
Input: N = 3
arr = {3, 2, 1}
Output: {1, 2, 3}
Explaination: As arr[] is the last permutation. So, the next permutation is the lowest one.

Your Task:
You do not need to read input or print anything. Your task is to complete the function nextPermutation() 
which takes N and arr[ ] as input parameters and returns a list of numbers containing the next permutation.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10000
*/

// SOLUTION

class Solution {
    // Function to reverse the elements in the array from index i to j
    static void reverse(int[] arr, int i, int j) {
        while (i < j) {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

            i++;
            j--;
        }
    }

    // Function to find the next permutation of the given array
    static List<Integer> nextPermutation(int N, int arr[]) {
        // Initialize k to N-2
        int k = N - 2;

        // Initialize a list to store the result
        List<Integer> res = new ArrayList<>();

        // Traverse the array from right to left to find the first element smaller than
        // its next element
        for (int i = N - 1; i > 0; i--) {
            if (arr[i] <= arr[i - 1]) {
                k--;
            } else {
                break;
            }
        }

        // If no such element is found (i.e., k == -1), reverse the entire array and
        // return
        if (k == -1) {
            reverse(arr, 0, N - 1);

            // Add the reversed array to the result list
            for (int i = 0; i < N; i++) {
                res.add(arr[i]);
            }
            return res;
        }

        // Find the rightmost element greater than the element at index k
        for (int i = N - 1; i > 0; i--) {
            if (arr[k] < arr[i]) {
                int temp = arr[k];
                arr[k] = arr[i];
                arr[i] = temp;
                break;
            }
        }

        // Reverse the elements from index k+1 to N-1
        reverse(arr, k + 1, N - 1);

        // Add the modified array to the result list
        for (int i = 0; i < N; i++) {
            res.add(arr[i]);
        }

        return res;
    }
}

// ............................

// String

// Java program to find next greater
// number with same set of digits.
import java.util.Arrays;

public class nextGreater {
    // Utility function to swap two digit
    static void swap(char ar[], int i, int j) {
        char temp = ar[i];
        ar[i] = ar[j];
        ar[j] = temp;
    }

    // Given a number as a char array number[],
    // this function finds the next greater number.
    // It modifies the same array to store the result
    static void findNext(char ar[], int n) {
        int i;

        // I) Start from the right most digit
        // and find the first digit that is smaller
        // than the digit next to it.
        for (i = n - 1; i > 0; i--) {
            if (ar[i] > ar[i - 1]) {
                break;
            }
        }

        // If no such digit is found, then all
        // digits are in descending order means
        // there cannot be a greater number with
        // same set of digits
        if (i == 0) {
            System.out.println("Not possible");
        } else {
            int x = ar[i - 1], min = i;

            // II) Find the smallest digit on right
            // side of (i-1)'th digit that is greater
            // than number[i-1]
            for (int j = i + 1; j < n; j++) {
                if (ar[j] > x && ar[j] < ar[min]) {
                    min = j;
                }
            }

            // III) Swap the above found smallest
            // digit with number[i-1]
            swap(ar, i - 1, min);

            // IV) Sort the digits after (i-1)
            // in ascending order
            Arrays.sort(ar, i, n);
            System.out.print("Next number with same" +
                    " set of digits is ");
            for (i = 0; i < n; i++)
                System.out.print(ar[i]);
        }
    }

    public static void main(String[] args) {
        char digits[] = { '5', '3', '4', '9', '7', '6' };
        int n = digits.length;
        findNext(digits, n);
    }
}
