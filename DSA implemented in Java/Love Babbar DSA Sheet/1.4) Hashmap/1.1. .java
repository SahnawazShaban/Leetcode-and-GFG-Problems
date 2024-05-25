/*
Majority Element

Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears strictly more than N/2 times in the array.
 

Example 1:
Input:
N = 3 
A[] = {1,2,3} 
Output:
-1
Explanation:
Since, each element in 
{1,2,3} appears only once so there 
is no majority element.

Example 2:
Input:
N = 5 
A[] = {3,1,3,3,2} 
Output:
3
Explanation:
Since, 3 is present more
than N/2 times, so it is 
the majority element.

Your Task:
The task is to complete the function majorityElement() which returns the majority element in the array. If no majority exists, return -1.
 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 

Constraints:
1 ≤ N ≤ 10^7
0 ≤ Ai ≤ 10^6

Company Tags
Flipkart, Accolite, Amazon, Microsoft, D-E-Shaw, Google, Nagarro, Atlassian
*/

// SOLUTION

class Solution {
    static int majorityElement(int a[], int size) {
        HashMap<Integer, Integer> mp = new HashMap<>();

        int k = size / 2;

        for (int val : a) {
            mp.put(val, mp.getOrDefault(val, 0) + 1);
        }

        for (int key : mp.keySet()) {
            if (mp.get(key) > k) {
                return key;
            }
        }
        return -1;
    }
}

// By using Moor's voting algorithm approach
// TC : O(N) & SC : O(1)

class Solution {
    static int majorityElement(int a[], int n) {
        int initialCnt = 0;
        int majorityNum = 0;

        for (int i = 0; i < n; i++) {
            if (initialCnt == 0) {
                initialCnt = 1;
                majorityNum = a[i];
            } else if (a[i] == majorityNum) {
                initialCnt++;
            } else {
                initialCnt--;
            }
        }

        int majorityCnt = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] == majorityNum) {
                majorityCnt++;
            }
        }

        if (majorityCnt > n / 2) {
            return majorityNum;
        }

        return -1;
    }
}