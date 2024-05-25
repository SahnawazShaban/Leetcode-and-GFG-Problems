public class RemoveDuplicateElement {
    public static boolean[] map = new boolean[26];
    // this array we can use any of the method without declare in parameter

    public static void removeDuplicate(String str,int idx,String newString){

        if (idx == str.length()){
            System.out.println(newString);
            return;
        }
        char currChar = str.charAt(idx);
        if (map[currChar - 'a']){       //map[currChar - 'a'] == true
            removeDuplicate(str,idx+1,newString);
        }
        else {
            newString += currChar;
            map[currChar - 'a'] = true;
            removeDuplicate(str,idx+1,newString);
        }
    }
    public static void main(String[] args) {
        String str = "SahnawaShabanZ";

        removeDuplicate(str.toLowerCase(),0,"");
    }
}
