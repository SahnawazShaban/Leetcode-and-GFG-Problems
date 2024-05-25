public class StringReverse {
    public static void reverseStr(String str, int idx){
        if (idx == -1){
            return;
        }
        System.out.print(str.charAt(idx));
        reverseStr(str,idx-1);
    }

    public static void main(String[] args) {
        String str = "shaan";
        reverseStr(str,str.length()-1);

        // without using any extra space
//        for (int i=str.length()-1;i>=0;i--){
//            char ch = str.charAt(i);
//            System.out.print(ch);
//        }
    }
}
