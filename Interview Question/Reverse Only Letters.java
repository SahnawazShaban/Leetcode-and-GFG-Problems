/*
Example 1:
input: "ab-cd"
Output: "dc-ba"

Example 2:
input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
*/


//Solution

public class ReverseOnlyLetters {
    public static String reverseOnlyLetters(String s) {
        // Convert the string to a character array
        char[] arr = s.toCharArray();
        
        // Initialize two pointers
        int left = 0;
        int right = arr.length - 1;
        
        // Traverse the array with two pointers
        while (left < right) {
            // Move left pointer to the right until it finds an alphabetic character
            if (!Character.isLetter(arr[left])) {
                left++;
                continue;
            }
            // Move right pointer to the left until it finds an alphabetic character
            if (!Character.isLetter(arr[right])) {
                right--;
                continue;
            }
            // Swap the characters at left and right pointers
            char temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            
            // Move both pointers towards the center
            left++;
            right--;
        }
        
        // Convert the character array back to a string
        return new String(arr);
    }

    public static void main(String[] args) {
        // Example 1
        String input1 = "ab-cd";
        String output1 = reverseOnlyLetters(input1);
        System.out.println("Input: " + input1);
        System.out.println("Output: " + output1);  // Output: "dc-ba"

        // Example 2
        String input2 = "a-bC-dEf-ghIj";
        String output2 = reverseOnlyLetters(input2);
        System.out.println("Input: " + input2);
        System.out.println("Output: " + output2);  // Output: "j-Ih-gfE-dCba"
    }
}
