/*
Insertion Sort
Easy
The task is to complete the insert() function which is used to implement Insertion Sort.


Example 1:
Input:
N = 5
arr[] = { 4, 1, 3, 9, 7}
Output:
1 3 4 7 9

Example 2:
Input:
N = 10
arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output:
1 2 3 4 5 6 7 8 9 10

Your Task: 
You don't have to read input or print anything. Your task is to complete the function insert() and insertionSort() where insert() takes the array, it's size and an index i and insertionSort() uses insert function to sort the array in ascending order using insertion sort algorithm. 

Expected Time Complexity: O(N*N).
Expected Auxiliary Space: O(1).


Constraints:
1 <= N <= 1000
1 <= arr[i] <= 1000

*/

// SOLUTION

class Solution {
    // Function to recursively insert an element into the sorted subarray
    // arr[0..i-1]
    static void insert(int arr[], int i) {
        // Base case: if i is less than or equal to 0, return
        if (i <= 0) {
            return;
        }

        // Recursively insert the element at index i-1 into the sorted subarray
        insert(arr, i - 1);

        // Store the current element to be inserted into the sorted subarray
        int temp = arr[i];
        // Initialize the index j to traverse the sorted subarray
        int j = i - 1;

        // Move elements of arr[0..i-1], that are greater than temp,
        // to one position ahead of their current position
        while (j >= 0 && arr[j] > temp) {
            arr[j + 1] = arr[j];
            j--;
        }

        // Insert the stored element (temp) at the correct position in the sorted
        // subarray
        arr[j + 1] = temp;
    }

    // Function to perform insertion sort recursively on the array
    public void insertionSort(int arr[], int n) {
        // Base case: if n is less than or equal to 1, return
        if (n <= 1) {
            return;
        }

        // Recursively sort the first n-1 elements of the array
        insertionSort(arr, n - 1);
        // Insert the last element (at index n-1) into the sorted subarray
        insert(arr, n - 1);
    }
}
