public class ReverseString {
    public static void main(String[] args) {
        String str = "Shaban",str1="";
        char ch;

        for (int i=0;i<str.length();i++){
            ch = str.charAt(i);
            str1 = ch + str1; // before str1 i have to add 'ch'
        }
        System.out.println(str1);
    }
}
