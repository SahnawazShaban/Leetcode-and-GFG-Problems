public class RepeatedSubStringPattern {
    public static void main(String[] args) {
        String str = "abababab";

        int l = str.length();

        boolean flag = false;

        for(int i=l/2;i>=1;i--) {
            if(l%i==0) {
                int m = l/i;
                String subS = str.substring(0,i);
                StringBuilder sb = new StringBuilder();
                for(int j=0;j<m;j++) {
                    sb.append(subS);
                }
                if(sb.toString().equals(str)){
                    flag = true;
                }
            }
        }

        if (!flag){
            System.out.println(flag);
        }
        else {
            System.out.println(flag);
        }

    }
}
