public class Exam {
    public static void main(String[] args) {
        String str = "ABC";
        String ans = "";

        for (int i=0;i<str.length();i++){
            ans = str.substring(0,i) + str.substring(i+1);
            System.out.println(ans);
        }
    }
}
