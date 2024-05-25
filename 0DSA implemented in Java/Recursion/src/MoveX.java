public class MoveX {
    public static void moveX(String str,String str1,int i,int count){
        if(str.length() == i){
            while (count!=0){
                str1 = str1 + 'x';
                count--;
            }
            System.out.println(str1);
            return;
        }
        if (str.charAt(i) == 'x'){
            count++;
        }
        else {
            str1 = str1 + str.charAt(i);
        }
        moveX(str,str1,i+1,count);
    }
    public static void main(String[] args) {
        String str = "axbcxxd";
        String str1 = "";
        moveX(str,str1,0,0);
    }
}

//NOTES:
//->First i have to check !=x values store in new String str1 and
// count how many x are there.
//
//-> add x into end of the str1.
//
//->suppose, if count == 3, then 3 times x add into end of the str1.

//Time Complexity : 0(n + count is n time (possible))
//
//=0(n + n) = 0(2n) = 0(n)
