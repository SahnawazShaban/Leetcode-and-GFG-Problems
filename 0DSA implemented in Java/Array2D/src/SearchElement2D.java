import java.util.Scanner;

public class SearchElement2D {
    public static void main(String[] args) {
        int[][] matrix = {
                {1,3,5,7},
                {10,11,16,20},
                {23,30,34,60},
                {71,75,86,91}
        };

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter target element : ");

        int target = sc.nextInt();

        boolean flag = false;

        for (int i=0;i < matrix.length;i++){
            for (int j=0;j < matrix[0].length;j++){
                if (matrix[i][j] == target){
                    flag = true;
                }
            }
        }

        if (flag){ // flag == true
            System.out.println("Element Found.");
        }
        else { // flag == false
            System.out.println("Element not Found.");
        }
    }
}
