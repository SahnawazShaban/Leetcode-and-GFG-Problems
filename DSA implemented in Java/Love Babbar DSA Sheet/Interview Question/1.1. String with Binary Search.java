/*
Iterate through each element in the string and compare it with the target value.
If the target value is found, return "Yes", otherwise return "No".


Input : str = "12 23 45 66 89 122 156 678", k = 122
this is sorted array find k elemment exist or not 
Output : Yes
*/

// SOLUTION

// Brute Force Approach:

public class Main {
    public static void main(String[] args) {
        String str = "12 23 45 66 89 122 156 678";
        int k = 122;
        String[] elements = str.split(" ");
        boolean found = false;
        for (String element : elements) {
            if (Integer.parseInt(element) == k) {
                found = true;
                break;
            }
        }
        if (found) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
// Time complexity: O(n) where n is the number of elements in the string.
// Space complexity: O(n) to store the split elements.

// Better Approach:
// Since the string is sorted, we can use binary search to find the target
// element efficiently.

public class Main {
    public static void main(String[] args) {
        String str = "12 23 45 66 89 122 156 678";
        int k = 122;
        String[] elements = str.split(" ");
        int left = 0;
        int right = elements.length - 1;
        boolean found = false;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int midValue = Integer.parseInt(elements[mid]);
            if (midValue == k) {
                found = true;
                break;
            } else if (midValue < k) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        if (found) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
// Time complexity: O(log n) where n is the number of elements in the string.
// Space complexity: O(n) to store the split elements.

// Optimal Approach:
// Instead of splitting the string and storing elements in an array, we can
// directly manipulate the string to perform binary search.

public class Main {
    public static void main(String[] args) {
        String str = "12 23 45 66 89 122 156 678";
        int k = 122;
        int left = 0;
        int right = str.length() - 1;
        boolean found = false;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int start = getStartIndex(str, mid);
            int end = getEndIndex(str, mid);
            int midValue = Integer.parseInt(str.substring(start, end + 1));
            if (midValue == k) {
                found = true;
                break;
            } else if (midValue < k) {
                left = end + 1;
            } else {
                right = start - 1;
            }
        }
        if (found) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

    private static int getStartIndex(String str, int mid) {
        int start = mid;
        while (start >= 0 && str.charAt(start) != ' ') {
            start--;
        }
        return start + 1;
    }

    private static int getEndIndex(String str, int mid) {
        int end = mid;
        while (end < str.length() && str.charAt(end) != ' ') {
            end++;
        }
        return end - 1;
    }
}

// Time complexity: O(log n) where n is the number of elements in the string.
// Space complexity: O(1).