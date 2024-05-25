public class RemoveSpecialCharacter {
    static String removeSpecialChar(String str){
        StringBuilder special_character = new StringBuilder();
        int count = 0;
        for (int i=0;i<str.length();i++){
            if (!Character.isDigit(str.charAt(i)) && !Character.isLetter(str.charAt(i))){
                count++;
            }
            else {
                special_character.append(str.charAt(i));
            }
        }
        System.out.println("Special Character Count : "+count);
        return special_character.toString();
    }
    public static void main(String[] args) {
        String str = "Sha an@23^";
        String ans = removeSpecialChar(str);
        System.out.println("After Remove Special Character : "+ans);
    }
}
