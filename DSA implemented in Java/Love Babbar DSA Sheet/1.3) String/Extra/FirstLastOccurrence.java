import java.util.Scanner;

public class FirstLastOccurrence {
    public static void main(String[] args) {
        String str = "bdsasjfjaaadvsa";

        int len = str.length()-1;

        int first = -1,last = -1;
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Character : ");
        char element = sc.next().charAt(0);

        for (int i=0;i<=len;i++){
            if (str.charAt(i) == element){
                if (first == -1){
                    first = i;
                }
                else {
                    last = i;
                }
            }
        }

        System.out.println("First Occurrence of "+element+" is "+ first);
        System.out.println("Last Occurrence of "+element+" is "+ last);
    }
}
