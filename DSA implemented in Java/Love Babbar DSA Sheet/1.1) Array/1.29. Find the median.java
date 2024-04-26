/*
Find the median
School
Given an array arr[] of N integers, calculate the median.

NOTE: Return the floor value of the median.
 

Example 1:
Input: N = 5
arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array 
middle element is the median 

Example 2:
Input: N = 4
arr[] = 56 67 30 79
Output: 61
Explanation: In case of even number of 
elements, average of two middle elements 
is the median. 

Your Task:
You don't need to read or print anything. Your task is to complete the function find_median() which takes the array as input parameter and return the floor value of the median.
 

Expected Time Complexity: O(n * log(n))
Expected Space Complexity: O(1)
 

Constraints:
1 <= Length of Array <= 100
1 <= Elements of Array <= 100

Company Tags
Accolite, Amazon, Samsung, FactSet
*/

// SOLUTION

class Solution {
    public int find_median(int[] v) {
        Arrays.sort(v);
        int val = 0;
        int n = v.length - 1;

        if (v.length % 2 == 0) {
            val = (v[n / 2] + v[(n / 2) + 1]);
            return val / 2;
        }

        return v[n / 2];
    }
}

// Same logic different way to write code.

class Solution {
    public int find_median(int[] v) {
        int mid;
        Arrays.sort(v);
        int n = v.length;

        if (n % 2 == 0) {
            mid = n / 2;
            return ((v[mid] + v[mid - 1]) / 2);

        } else {
            mid = n / 2;
            return v[mid];
        }
    }
}
