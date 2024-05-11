import java.util.Scanner;

public class ValidPalindrome {
    static boolean valid2(String s, int i, int j){
        while (i<=j){
            if (s.charAt(i) == s.charAt(j)){
                i++;
                j--;
            }
            else {
                break;
            }
            if (i>=j){
                return true;
            }
        }
        return false;
    }
    static boolean valid(String s, int i, int j){
        while (i<=j){
            if (s.charAt(i) == s.charAt(j)){
                i++;
                j--;
            }
            else {
                break;
            }
            if (i>=j){
                return true;
            }
        }
        return valid2(s,i+1,j) || valid2(s,i,j-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a String to check, it is palindrome or not : ");
        String s = sc.next();
        int i=0,j=s.length()-1;

        boolean ans = valid(s,i,j);

        System.out.println(ans);
    }
}
