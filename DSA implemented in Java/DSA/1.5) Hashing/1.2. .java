/*
Second Largest
Easy
Given an array Arr of size N, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

Example 1:
Input: 
N = 6
Arr[] = {12, 35, 1, 10, 34, 1}
Output: 34
Explanation: The largest element of the 
array is 35 and the second largest element
is 34.

Example 2:
Input: 
N = 3
Arr[] = {10, 5, 10}
Output: 5
Explanation: The largest element of 
the array is 10 and the second 
largest element is 5.
Your Task:
You don't need to read input or print anything. Your task is to complete the function print2largest() which takes the array of integers arr and n as parameters and returns an integer denoting the answer. If 2nd largest element doesn't exist then return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
2 ≤ N ≤ 10^5
1 ≤ Arri ≤ 10^5
*/

// SOLUTION

class Solution {
    int print2largest(int arr[], int n) {
        int first = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        
        for (int i=0; i<n; i++){
            if (arr[i] > first){
                second = first;
                first = arr[i];
            }
            else if (arr[i] > second && arr[i] != first){
                second = arr[i];
            }
        }
        
        if (second == Integer.MIN_VALUE){
            return -1;
        }
        
        return second;
    }
}