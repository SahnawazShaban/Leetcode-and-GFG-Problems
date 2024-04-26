/*
Union of two arrays
Basic
Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

Note : Elements are not necessarily distinct.

Example 1:
Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the elements which comes in the union set of both arrays. So count is 5.

Example 2:
Input:
6 2 
85 25 1 32 54 6
85 2 
Output: 
7
Explanation: 
85, 25, 1, 32, 54, 6, and
2 are the elements which comes in the
union set of both arrays. So count is 7.
Your Task:
Complete doUnion function that takes a, n, b, m as parameters and returns the count of union elements of the two arrays. The printing is done by the driver code.

Constraints:
1 ≤ n, m ≤ 10^5
0 ≤ a[i], b[i] < 10^5

Expected Time Complexity : O(n+m)
Expected Auxilliary Space : O(n+m)
*/

// SOLUTION

class Solution {
    public static int doUnion(int a[], int n, int b[], int m) {
        HashSet<Integer> st = new HashSet<>();

        for (int ele : a) {
            st.add(ele);
        }

        for (int ele1 : b) {
            st.add(ele1);
        }

        return st.size();
    }
}

// Time Complexity:

// The time complexity of adding an element to a HashSet is O(1) on average,
// assuming there are no collisions that require additional handling (which is
// typical for most practical scenarios).
// In the doUnion method, we iterate through each element in arrays a and b
// exactly once, adding them to the HashSet.
// Therefore, the time complexity of adding all elements to the HashSet is O(n +
// m), where n is the size of array a and m is the size of array b.
// Accessing the size of the HashSet using size() method also has a time
// complexity of O(1).

// Space Complexity:

// The space complexity depends on the number of unique elements present in
// arrays a and b.
// In the worst case scenario, if all elements in arrays a and b are unique, the
// HashSet will store all of them.
// Therefore, the space complexity is O(n + m), where n is the number of
// elements in array a and m is the number of elements in array b.
// In summary:

// Time complexity: O(n + m)
// Space complexity: O(n + m)
