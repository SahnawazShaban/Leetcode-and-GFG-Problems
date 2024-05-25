public class PartOfRotatedArray {
    static boolean isRotated(String str1, String str2){
        return (str1.length()==str2.length() && (str1 + str1).contains(str2));
    }
    public static void main(String[] args) {
        String str1 = "ABCD";
        String str2 = "CDA";

        if (isRotated(str1,str2)){
            System.out.println("Rotation of string is present.");
        }
        else {
            System.out.println("Rotation of string is not present.");
        }
    }
}



//String 1 : ABCD
//String 2 : CDAB
//
//AB CDAB CD