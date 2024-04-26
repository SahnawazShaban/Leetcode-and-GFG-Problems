/*
Kth smallest element
Medium
Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

Note :-  l and r denotes the starting and ending index of the array.

Example 1:
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
L=0 R=5
Output : 7
Explanation :
3rd smallest element in the given array is 7.

Example 2:
Input:
N = 5
arr[] = 7 10 4 20 15
K = 4 L=0 R=4
Output : 15
Explanation :
4th smallest element in the given array is 15.

Your Task:
You don't have to read input or print anything. Your task is to complete the function kthSmallest() which takes the array arr[], integers l and r denoting the starting and ending index of the array and an integer K as input and returns the Kth smallest element.
 
Expected Time Complexity: O(n*log(n) )
Expected Auxiliary Space: O(log(n))

Constraints:
1 <= N <= 10^5
 L==0
 R==N-1
1<= arr[i] <= 10^5
1 <= K <= N
*/

// SOLUTION

class Solution {
    public static int kthSmallest(int[] arr, int l, int r, int k) {
        int i = l;
        int j = r;
        int pivot = arr[l];

        while (i <= j) {
            // Move the left pointer i to the right until we find an element larger than the
            // pivot
            while (arr[i] < pivot) {
                i++;
            }
            // Move the right pointer j to the left until we find an element smaller than
            // the pivot
            while (arr[j] > pivot) {
                j--;
            }
            // Swap arr[i] and arr[j] if i <= j
            if (i <= j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }

        // If the index of the pivot after partitioning is greater than or equal to k,
        // then the kth smallest element must be on the left side of the pivot.
        if (l + k - 1 <= j) {
            return kthSmallest(arr, l, j, k);
        }
        // If the index of the pivot after partitioning is less than or equal to k,
        // then the kth smallest element must be on the right side of the pivot.
        else if (l + k - 1 >= i) {
            return kthSmallest(arr, i, r, k - (i - l));
        }
        // Otherwise, the pivot itself is the kth smallest element.
        else {
            return arr[j + 1];
        }
    }
}

// Optimal
class Solution {
    public static int kthSmallest(int[] arr, int l, int r, int k) {
        Queue<Integer> pq = new PriorityQueue<>();
        int n = r - l + 1;

        for (int i = 0; i < k; i++) {
            pq.add(-arr[i]);
        }

        for (int i = k; i < n; i++) {
            if (-pq.peek() > arr[i]) {
                pq.poll();
                pq.add(-arr[i]);
            }
        }
        return -pq.peek();
    }
}