/*
Find duplicates in an array
Easy
Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Note: The extra space is only for the array to be returned. Try and perform all operations within the provided array. 

Example 1:
Input:
N = 4
a[] = {0,3,1,2}
Output: 
-1
Explanation: 
There is no repeating element in the array. Therefore output is -1.

Example 2:
Input:
N = 5
a[] = {2,3,1,2,3}
Output: 
2 3 
Explanation: 
2 and 3 occur more than once in the given array.
Your Task:
Complete the function duplicates() which takes array a[] and n as input as parameters and returns a list of elements that occur more than once in the given array in a sorted manner. 

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

Constraints:
1 <= N <= 10^5
0 <= A[i] <= N-1, for each valid i
*/

// SOLUTION

class Solution {
    public static ArrayList<Integer> duplicates(int arr[], int n) {
        // HashMap<Integer, Integer> mp = new HashMap<>();
        // Solution - 1
        HashSet<Integer> s = new HashSet<>();
        HashSet<Integer> set = new HashSet<>();

        for (int i = 0; i < arr.length; i++) {
            if (set.contains(arr[i])) {
                s.add(arr[i]);
            } else {
                set.add(arr[i]);
            }

        }

        ArrayList<Integer> ans = new ArrayList<>(s);
        if (ans.size() == 0) {
            ans.add(-1);
        }
        Collections.sort(ans);
        return ans;

        // Solution - 2

        ArrayList<Integer> res = new ArrayList<Integer>();

        for (int i = 0; i < n; i++) {
            int index = arr[i] % n;
            arr[index] += n;
        }

        for (int i = 0; i < n; i++) {

            if (arr[i] / n > 1) {
                res.add(i);
            }

            arr[i] = arr[i] / n;
        }

        if (res.size() == 0) {
            res.add(-1);
        }

        return res;
    }
}

/*
 * Time Complexity:
 * 
 * The loop iterates over each element in the input array once, so it's O(n),
 * where n is the number of elements in the array.
 * Inside the loop, the contains method of the HashSet is called. The average
 * time complexity of contains in a HashSet is O(1). So, for each iteration of
 * the loop, the time complexity for the contains operation is O(1).
 * Sorting the resulting ArrayList takes O(m log m) time, where m is the number
 * of duplicate elements found (the size of the HashSet s). If there are no
 * duplicates, sorting takes O(1).
 * Therefore, the overall time complexity is dominated by the loop, which is
 * O(n).
 * 
 * 
 * Space Complexity:
 * 
 * Two HashSet objects (set and s) are used to store elements. The space
 * required by these HashSet objects depends on the number of distinct elements
 * and duplicate elements respectively.
 * The worst-case space complexity for HashSet is O(n) when all elements are
 * distinct.
 * The resulting ArrayList ans will contain at most n/2 elements (if every
 * element in the input array is a duplicate), so the space complexity for it is
 * O(n).
 * Therefore, the overall space complexity is O(n).
 */

// EXTRA:

// 1. Brute Force Approach:

// In the brute force approach, you compare each element of the array with every
// other element to check for duplicates.

public class DuplicateFinder {

    public static void findDuplicatesBruteForce(int[] arr) {
        System.out.println("Duplicates using brute force method:");
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    System.out.println(arr[i]);
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 2, 6, 7, 8, 5 };
        findDuplicatesBruteForce(arr);
    }
}

// 2. Better Approach (Using Sorting):

// Sort the array first, then traverse it to find adjacent elements that are
// equal.

import java.util.Arrays;

public class DuplicateFinder {

    public static void findDuplicatesBetter(int[] arr) {
        System.out.println("Duplicates using better method (sorting):");
        Arrays.sort(arr);
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] == arr[i + 1]) {
                System.out.println(arr[i]);
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 2, 6, 7, 8, 5};
        findDuplicatesBetter(arr);
    }
}

// 3. Optimal Approach (Using HashSet):

// Use a HashSet to store elements as you traverse the array. If you encounter
// an element that is already in the HashSet, then its a duplicate.

import java.util.HashSet;

public class DuplicateFinder {

    public static void findDuplicatesOptimal(int[] arr) {
        System.out.println("Duplicates using optimal method (HashSet):");
        HashSet<Integer> set = new HashSet<>();
        HashSet<Integer> duplicates = new HashSet<>();

        for (int num : arr) {
            if (!set.add(num)) {
                duplicates.add(num);
            }
        }

        for (int duplicate : duplicates) {
            System.out.println(duplicate);
        }
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 2, 6, 7, 8, 5 };
        findDuplicatesOptimal(arr);
    }
}

// Brute Force: O(n^2)
// Better Approach (Sorting): O(n log n) due to sorting, then O(n) for
// traversing
// Optimal Approach (HashSet): O(n)
