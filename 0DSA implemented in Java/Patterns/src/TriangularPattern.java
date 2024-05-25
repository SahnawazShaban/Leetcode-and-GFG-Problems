public class TriangularPattern {
    public static void main(String[] args) {
//        for (int i=1;i<=5;i++){
//            for (int j=1;j<=i;j++){
//                System.out.print(j);
//            }
//            System.out.println();
//        }
//
//        1
//        12
//        123
//        1234
//        12345

        for (int i=1;i<=5;i++){
//            print row-i spaces
            for (int j=1;j<=(5-i);j++){
                System.out.print(" ");
            }

//            print 1 to i
            for (int k=1;k<=i;k++){
                System.out.print(k);
            }

//            print i-1 to 1
            for (int l=i-1;l>=1;l--){
                System.out.print(l);
            }
            System.out.println();
        }
    }
}
