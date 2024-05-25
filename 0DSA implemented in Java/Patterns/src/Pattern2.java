import java.util.Scanner;
public class Pattern2 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n = sc.nextInt();

        for (int i=1;i<=n;i++){
            for (int j=1;j<=i;j++){
                System.out.print(5+i-j);
            }
            System.out.println();
        }
    }
}


//System.out.print(5-i+j);
//        5
//        45
//        345
//        2345
//        12345

//System.out.print(5+i-j);
//        5
//        65
//        765
//        8765
//        98765
