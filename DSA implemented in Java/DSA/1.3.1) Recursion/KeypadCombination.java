public class KeypadCombination {
    public static String[] keypad = {".","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    public static void keypadCombination(String str,int idx,String combination){
        //base condition
        if (idx == str.length()){
            System.out.println(combination);
            return;
        }
        char currChar = str.charAt(idx);
        String mapping = keypad[currChar - '0'];

        for (int i=0;i<mapping.length();i++){
            keypadCombination(str, idx+1, combination+mapping.charAt(i));
        }
    }
    public static void main(String[] args) {
        String str = "34";

        keypadCombination(str,0,"");
    }
}
