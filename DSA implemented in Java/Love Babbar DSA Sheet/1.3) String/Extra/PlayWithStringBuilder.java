public class PlayWithStringBuilder {
    public static void main(String[] args) {
//        StringBuilder sb = new StringBuilder("Shaan");
//
//
//        //replace char (index,char)
//        sb.setCharAt(0,'A');
//        System.out.println(sb);   //Ahaan
//
//        //add more char (offset,str), at any index
//        sb.insert(0,"S");
//        System.out.println(sb);  //SAhaan
//
//        sb.insert(3,"z");
//        System.out.println(sb);     //SAhzaan
//
//        //delete in String
//        sb.delete(3,4);
//        System.out.println(sb);    //SAhaan
//
//
//        //str = str + h in this String, creating a new space from stack memory.
//        //sb1.append("h") in this update on same string
//        StringBuilder sb1 = new StringBuilder("S");
//        sb1.append("h"); // str = str + h
//        sb1.append("a"); // str = str + a
//        sb1.append("a");
//        sb1.append("n");
//        System.out.println(sb1);  //Shaan
//        System.out.println(sb1.length());  //5


        //reverse a String - method 1
        StringBuilder rev = new StringBuilder("Shaan");

        for (int i=0;i<rev.length()/2;i++){
            int front = i;//0,1
            int back = rev.length()-1-i; //5-1-0=4, 5-1-1=3

//            s-0,h-1,a-2,a-3,n-4

            char frontChar = rev.charAt(front);
            char backChar = rev.charAt(back);

            rev.setCharAt(front,backChar);
            rev.setCharAt(back,frontChar);
        }
        System.out.println(rev); // naahS


        //reverse a String - method 2
        StringBuilder rev1 = new StringBuilder("Shaan");
        rev1.reverse();
        System.out.println(rev1);    //naahS

        //reverse a String - method 3, only string is reverse
        String rev2 = "Shaan123";
        String rev3 = "";
        int n = rev.length();

        for (int i=n-1;i>=0;i--){
            char ch = rev2.charAt(i);
            if (Character.isLetter(ch)) {
                rev3 += ch;
            }
        }
        System.out.println(rev3);
    }
}
