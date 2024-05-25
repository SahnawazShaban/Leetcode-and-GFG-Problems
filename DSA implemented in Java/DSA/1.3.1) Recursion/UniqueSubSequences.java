import java.util.HashSet;

public class UniqueSubSequences {
    public static void uniqueSubsets(String str,int idx,String newString,HashSet<String> set){
        if (idx >= str.length()){
            if (set.contains(newString)){
                return;
            }
            else {
                System.out.println(newString);
                set.add(newString);
                return;
            }

            //other way to compress line of code

//            if (!set.contains(newString)) {
//                System.out.println(newString);
//                set.add(newString);
//            }
//            return;
        }
        char currElement = str.charAt(idx);
        //include
        uniqueSubsets(str,idx+1,newString+currElement,set);
        //exclude
        uniqueSubsets(str,idx+1,newString,set);

    }
    public static void main(String[] args) {
        String str = "aaa";
        HashSet<String> set = new HashSet<>();
        uniqueSubsets(str,0,"",set);
    }
}
