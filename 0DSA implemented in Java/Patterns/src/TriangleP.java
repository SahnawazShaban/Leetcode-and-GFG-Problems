public class TriangleP {
    public static void main(String[] args) {
//        for (int i=1;i<=5;i++){
//            for (int j=1;j<=5-i;j++){
//                System.out.print("&");
//            }
//
//            for (int k=1;k<=2*i-1;k++){
//                System.out.print("*");
//            }
//
//            for (int l=1;l<=5-i;l++){
//                System.out.print("$");
//            }
//            System.out.println();
//        }

//        OUTPUT:
//        &&&&*$$$$
//        &&&***$$$
//        &&*****$$
//        &*******$
//        *********

        for (int i=1;i<=5;i++){
            for (int j=1;j<=5-i;j++){
                System.out.print(" ");
            }
            for (int j=1;j<=i;j++){
                System.out.print(j);
            }

            for (int k=1;k<=i-1;k++){
                System.out.print(k);
            }
            System.out.println();
        }
    }
}
