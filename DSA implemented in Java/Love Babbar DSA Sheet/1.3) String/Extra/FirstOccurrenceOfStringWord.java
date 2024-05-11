public class FirstOccurrenceOfStringWord {
    public static boolean repeatedSubstringPattern(String s) {

        int size = s.length();

        String sFold = s.substring(1, size) + s.substring(0, size-1);

        return sFold.contains(s);

    }
    public static int strStr(String haystack, String needle) {
        // empty needle appears everywhere, first appears at 0 index
        if (needle.length() == 0)
            return 0;
        if (haystack.length() == 0)
            return -1;

        for (int i = 0; i < haystack.length(); i++) {
            // no enough places for needle after i
            if (i + needle.length() > haystack.length())
                break;

            for (int j = 0; j < needle.length(); j++) {
                if (haystack.charAt(i+j) != needle.charAt(j))
                    break;
                if (j == needle.length()-1)
                    return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        String str = "mississippi";
        String s = "abcabc"; //bc|abcabc|ab

//        int ans = strStr(str,"issip");
//        System.out.println(ans);

        boolean res = repeatedSubstringPattern(s);

        System.out.println(res);
    }
}
