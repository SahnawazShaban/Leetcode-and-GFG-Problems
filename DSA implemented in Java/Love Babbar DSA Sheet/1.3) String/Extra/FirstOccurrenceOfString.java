import java.util.Scanner;

public class FirstOccurrenceOfString {
    public static void main(String[] args) {
        String str = "sdfsdaafg";
        int len = str.length()-1;
        System.out.println("Which element you found?");
        Scanner sc = new Scanner(System.in);
        char ch = sc.next().charAt(0);

        boolean flag = true;

        for (int i=0;i<=len;i++){
            if (str.charAt(i) == ch){
                System.out.print(i+" is first occurrence of '"+ ch+"' character.");
                flag = false;
                break;
            }
        }

        if (!flag){
            System.out.print("-> Found");
        }
        else {
            System.out.println("Not Found");
        }
    }
}
