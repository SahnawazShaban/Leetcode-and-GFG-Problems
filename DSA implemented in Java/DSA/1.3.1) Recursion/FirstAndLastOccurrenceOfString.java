public class FirstAndLastOccurrenceOfString {
    public static int first = -1;
    public static int last = -1;
    static void firstAndLastOccurrence(String str, int idx, char ch){
        if (idx == str.length()-1){
            System.out.println("First Occurrence of a is "+first);
            System.out.println("Last Occurrence of a is "+last);
            return;
        }
        if (str.charAt(idx) == ch){
            if (first == -1){
                first = idx;
            }
            else {
                last = idx;
            }
        }

        firstAndLastOccurrence(str,idx+1,ch);
    }
    public static void main(String[] args) {
        String str = "sahnawaz";

        firstAndLastOccurrence(str,0,'a');
    }
}
