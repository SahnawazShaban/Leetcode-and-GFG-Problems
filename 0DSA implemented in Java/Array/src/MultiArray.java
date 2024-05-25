public class MultiArray {
//    void multiArray(){
//        int
//    }
    public static void main(String[] args) {
//        int[][] multidimension = new int[4][3];

        int[][] multidimension = {{2,3,4},{5,7,6},{8,1,2},{0,9,3}};

        for (int i=0;i< multidimension.length;i++){
            //arr[0] and arr[1]
            for (int j=0;j<multidimension[i].length;j++){
                System.out.print(multidimension[i][j]+" ");
            }
            System.out.println();
        }
    }
}
