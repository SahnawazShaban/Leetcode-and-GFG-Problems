public class ReverseTriangle {
    public static void main(String[] args) {
        int n=5;
        int space=n;

        for (int i=1;i<=n;i++){
            for (int j=1;j<=space;j++){
                System.out.print("*");
            }
            space--;
            System.out.println();
        }
    }
}
