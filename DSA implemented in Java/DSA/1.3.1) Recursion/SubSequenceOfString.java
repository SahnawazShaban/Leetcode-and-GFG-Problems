public class SubSequenceOfString {
    public static void subSequence(String str,int idx,String newString){
        //base condition
        if (idx == str.length()){
            System.out.println(newString);
            return;
        }
        char ch = str.charAt(idx);
        //to be or (include) = anna chahata hai
        subSequence(str,idx+1,newString+ch);
        //not to be or (exclude) = nahi aana chahata
        subSequence(str,idx+1,newString);
    }
    public static void main(String[] args) {
        String str = "aaa";

        subSequence(str,0,"");
    }
}
