import java.util.Scanner;

public class TransposeOfMatrix {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //n x m matrix to m x n
        // Transpose is applied only for square matrix
        System.out.println("Enter value of n : ");
        int n = sc.nextInt();

        System.out.println("Enter value of m : ");
        int m = sc.nextInt();

        int[][] transpose = new int[n][m];

        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                transpose[i][j] = sc.nextInt();
            }
        }

        // just change i->m and j->n that's it.....
        for (int i=0;i<m;i++){
            for (int j=0;j<n;j++){
                System.out.print(transpose[i][j]+ " ");
            }
            System.out.println();
        }
    }
}
