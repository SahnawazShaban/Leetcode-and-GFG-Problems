/*
Largest Sum Contiguous Subarray (Kadane’s Algorithm)

Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum. 
*/

// SOLUTION

// Java program to print largest contiguous array sum
import java.io.*;
import java.util.*;

class Kadane {
	// Driver Code
	public static void main(String[] args)
	{
		int[] a = { -2, -3, 4, -1, -2, 1, 5, -3 };
		System.out.println("Maximum contiguous sum is "
						+ maxSubArraySum(a));
	}

	// Function Call
	static int maxSubArraySum(int a[])
	{
		int size = a.length;
		int max_so_far = Integer.MIN_VALUE, max_ending_here
											= 0;

		for (int i = 0; i < size; i++) {
			max_ending_here = max_ending_here + a[i];
			if (max_so_far < max_ending_here)
				max_so_far = max_ending_here;
			if (max_ending_here < 0)
				max_ending_here = 0;
		}
		return max_so_far;
	}
}

// start and end index

import java.io.*;
import java.util.*;

class GFG {

    static void maxSubArraySum(int a[], int size) {
        int max_so_far = Integer.MIN_VALUE,
                max_ending_here = 0, start = 0, end = 0, s = 0;

        for (int i = 0; i < size; i++) {
            max_ending_here += a[i];

            if (max_so_far < max_ending_here) {
                max_so_far = max_ending_here;
                start = s;
                end = i;
            }

            if (max_ending_here < 0) {
                max_ending_here = 0;
                s = i + 1;
            }
        }
        System.out.println("Maximum contiguous sum is " + max_so_far);
        System.out.println("Starting index " + start);
        System.out.println("Ending index " + end);
    }

    // Driver code
    public static void main(String[] args) {
        int a[] = { -2, -3, 4, -1, -2, 1, 5, -3 };
        int n = a.length;
        maxSubArraySum(a, n);
    }
}
