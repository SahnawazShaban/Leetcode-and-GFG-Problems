public class SingleArray {
    public static void main(String[] args) {
//        int[] onedimension = new int[5];
//        String[] onedimension = new String[5];
        int[] singlearray = {1,5,3,23,45,78,90};
        String[] stringsarray = {"virat","ABde","babar","jos"};
        singlearray[0]=81; //initialize value
        System.out.println("Integer Array : ");
         for (int i=0;i< singlearray.length;i++){
             System.out.println("Index of "+i+" is "+singlearray[i]);
         }

        System.out.println();
        System.out.println("String Array : ");
         for (int i=0 ;i<stringsarray.length;i++){
             System.out.println("Index of "+i+" is "+stringsarray[i]);
         }

        System.out.println("For each loop :");
         for (int single:singlearray){
             System.out.println(single);
         }
    }
}
