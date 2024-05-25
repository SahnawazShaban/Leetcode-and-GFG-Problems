import java.util.Scanner;

public class FindXIndices {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter row value :");
        int row = sc.nextInt();

        System.out.println("Enter column value : ");
        int col = sc.nextInt();

        int[][] arr = new int[row][col];

        for (int i=0;i<row;i++){
            for (int j=0;j<col;j++){
                arr[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter value of X to get indices of X : ");
        int x=sc.nextInt();

        //output
        for (int i=0;i<row;i++){
            for (int j=0;j<col;j++){
                if (arr[i][j] == x){
                    System.out.print("("+i+","+j+")"+" ");
                }
            }
            System.out.println();
        }

    }
}
