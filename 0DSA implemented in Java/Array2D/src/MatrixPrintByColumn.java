public class MatrixPrintByColumn {
    public static void main(String[] args) {
        int[][] matrix = {{1,2,3},{4,5,6},{7,8,9}};

        int row = matrix.length;
        int col = matrix[0].length;

        System.out.println("Input : ");
        for (int i=0;i<row;i++){
            for (int j=0;j<col;j++){
                System.out.print(matrix[i][j]+ " ");
            }
            System.out.println();
        }

        int t=0,b=row-1,l=0,r=col-1;
        int dir = 0;

        while (t<=b && l<=r){
            if (dir % 2 == 0){
                for (int i=t;i<=b;i++){
                    System.out.print(matrix[i][l] + " ");
                }
                l++;
                dir++;
            }
            else {
                for (int i=col;i>=0;i--){
                    System.out.print(matrix[i][l] + " ");
                }
                l++;
                dir++;
            }
        }

    }
}

//input
//1 2 3
//4 5 6
//7 8 9

//output
//1 4 7 8 5 2 3 6 9