public class StringGoal {
    //Rotate String
    public static boolean rotateString(String s,String goal){
        if (s.length() != goal.length()){
            return false;
        }
        String s1 = s+s;

        return s1.contains(goal);
    }
    public static void main(String[] args) {
        String s = "sahnawaz";
        String goal = "awazsahn";

        boolean ans = rotateString(s,goal);

        System.out.println(ans);
    }
}
