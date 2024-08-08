/*
p-th Smallest Factor of a Number

Determine the factors of a number (i.e., all positive integer values that evenly divide into a number) 
and then return the pth element of the list, sorted in ascending order. If there is no pth element, 
return 0. Example: n = 20 p = 3 The factors of 20 in ascending order are {1, 2, 4, 5, 10, 20}. 
Using 1-based indexing, if p = 3, then 4 is returned. If p > 6, 0 would be returned.
*/


//Solution

import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        int n = 20;
        int p = 3;
        System.out.println(pthFactor(n, p));  // Output will be 4
    }

    public static int pthFactor(int n, int p) {
        ArrayList<Integer> factors = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                factors.add(i);
            }
        }

        Collections.sort(factors);
        
        if (p > factors.size()) {
            return 0;
        } else {
            return factors.get(p - 1);
        }
    }
}
