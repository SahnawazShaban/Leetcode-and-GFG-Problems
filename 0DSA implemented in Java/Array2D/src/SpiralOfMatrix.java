public class SpiralOfMatrix {
    public static void main(String[] args) {
        int[][] spiral = {{1,2,3},{4,5,6},{7,8,9}};

        System.out.println("Input : ");
        for (int i=0;i<3;i++){
            for (int j=0;j<3;j++){
                System.out.print(spiral[i][j] + " ");
            }
            System.out.println();
        }

        int row = spiral.length;
        int col = spiral[0].length;

        int t=0,b=row-1,l=0,r=col-1;
        int dir=0;

        System.out.println("Output : ");
        while (t<=b && l<=r){
            if (dir == 0){
                for (int i=l;i<=r;i++){
                    System.out.print(spiral[t][i]+" ");
                }
                dir = 1;
                t++;
            }
            else if (dir == 1) {
                for (int i=t;i<=b;i++){
                    System.out.print(spiral[i][r]+" ");
                }
                dir = 2;
                r--;
            } else if (dir == 2) {
                for (int i=r;i>=l;i--){
                    System.out.print(spiral[b][i]+" ");
                }
                dir = 3;
                b--;
            } else if (dir == 3) {
                for (int i=b;i>=t;i--){
                    System.out.print(spiral[i][l]+" ");
                }
                dir = 0;
                l++;
            }
        }
    }
}
