import java.util.Scanner;

public class SearchElement2DBetter {
    public static void main(String[] args) {
        int[][] matrix = {
                {4,6,7,11},
                {1,3,5,16},
                {8,12,20,21},
                {2,9,10,13}
        };

        int col = matrix[0].length-1;
        int row = 0;

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your target : ");
        int target = sc.nextInt();

        boolean flag = false;

        while (col >= 0 && row <= matrix.length-1){

            if (matrix[row][col] == target){
                flag = true;
                break;
            }
            else if (matrix[row][col] < target){
                row++;
                System.out.println("["+row+","+col+"]"+"--->"+matrix[row][col]);
            }
            else {
                col--;
                System.out.println("["+row+","+col+"]"+"--->"+matrix[row][col]);
            }
        }

        if (flag){
            System.out.println("["+row+","+col+"]"+"--->"+"Target Found.");
        }
        else {
            System.out.println("Not Found");
        }
    }
}
