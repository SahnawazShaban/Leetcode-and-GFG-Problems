public class ReverseStringUsingRecursion {
    static void reverseString(String str,int index){

        if (index == 0){
            System.out.println(str.charAt(index));
            return;
        }
        System.out.print(str.charAt(index));
        reverseString(str,index-1);
    }
    public static void main(String[] args) {
        String str = "Shaban";

        reverseString(str,str.length()-1);
    }
}
