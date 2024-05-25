import java.util.HashSet;
import java.util.StringJoiner;
public class IntersectionArray {
    public static void main(String[] args) {
        StringJoiner sj1=new StringJoiner(",","[","]");
        sj1.add("A").add("B").add("C");
        System.out.println(sj1);
        int[] arr1 = {2,4,2,1,6,5,1};
        int[] arr2 = {3,1,5,6,7,6};

        for (int i=0;i<arr1.length;i++){
            for (int j=0;j<arr2.length;j++){
                if (arr1[i]==arr2[j]){
                    System.out.println(arr1[i]);
                }
            }
        }
    }
}
