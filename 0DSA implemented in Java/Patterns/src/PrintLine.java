public class PrintLine {
    static void printPat(int n)
    {
        for(int i=n;i>0;i--){
            for(int j=n;j>0;j--){
                for (int count=0;count<i;count++){
                    System.out.print(j+" ");
                }
            }
            System.out.println("$");
        }
    }
    public static void main(String[] args) {
        printPat(3);
    }
}
