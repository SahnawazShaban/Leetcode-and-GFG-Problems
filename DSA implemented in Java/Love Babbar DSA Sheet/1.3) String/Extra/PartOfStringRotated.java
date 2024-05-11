public class PartOfStringRotated {
    public static void main(String[] args) {
        String str = "Geeks";
        String goal = "eeKsG";
        String str1 = str+str;
//        System.out.println(str1);

        str1.contains(goal);

        System.out.println(str1);
        //type-1
//        StringBuilder rev = new StringBuilder(str);
//        System.out.println(rev.reverse());

        //type-2
//        for (int i=str.length()-1;i>=0;i--){
//            rev.append(str.charAt(i));
//        }
//
//        System.out.println(rev);

        //type-3
//        String str = "Geeks";
//        String rev = "";
//
//        for (int i=str.length()-1;i>=0;i--){
//            rev += str.charAt(i);
//        }
//
//        System.out.println(rev);
    }
}
