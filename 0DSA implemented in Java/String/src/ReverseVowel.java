public class ReverseVowel {
    public static void main(String[] args) {
        String s = "leetcode";
        char[] chars = s.toCharArray();

        int j=0;
        int i = s.length()-1;

        while(j<=i){
            char fast = s.charAt(i);
            char slow = s.charAt(j);

            if(fast == 'a' && slow == 'a'){

                char temp = fast;
                fast = slow;
                slow = temp;

                i--;
            }
            j++;
        }
        System.out.println(s);
    }
}
