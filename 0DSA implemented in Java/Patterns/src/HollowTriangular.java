import java.util.Scanner;
public class HollowTriangular {
    public static void main(String[] args) {
        for (int i=1;i<=4;i++){
            for (int j=1;j<=7;j++){
                if ((i+j==5) || (j-i==3) || (i==4)) {
                    System.out.print(i);
                }
                else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
