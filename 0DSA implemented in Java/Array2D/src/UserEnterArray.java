import java.util.Scanner;

public class UserEnterArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter row value : ");
        int row = sc.nextInt();

        System.out.println("Enter column value : ");
        int col = sc.nextInt();

        int[][] arr = new int[row][col];

        //input
        for (int i=0;i< row;i++){
            for (int j=0;j<col;j++){
                arr[i][j] = sc.nextInt();
            }
            System.out.println();
        }

        //output
        for (int i=0;i< row;i++){
            for (int j=0;j<col;j++){
                System.out.print(arr[i][j]+" ");
            }
            System.out.println();
        }

    }
}
