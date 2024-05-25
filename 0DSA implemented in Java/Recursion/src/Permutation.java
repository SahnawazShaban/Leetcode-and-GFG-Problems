public class Permutation {
    public static void permutation(String str,String prem,int idx){
        if (str.length() == 0){
            System.out.println(prem);
            return;
        }
        for (int i=0;i<str.length();i++){
            char currChar = str.charAt(i);
            String newStr1 = str.substring(0, i);
            String newStr = newStr1 + str.substring(i + 1);

            permutation(newStr,prem+currChar,idx+1);
        }
    }
    public static void main(String[] args) {
        String str = "ABC";

        permutation(str,"",0);
    }
}


// Permutation is a example of Backtracting.

//Frist place A__ and second time like this B__ but A already placed,
//so we remove A first
//
//currChar = str.charAt(i); -> saved first character
//
//so we remove A, str.substring(0,i)

// substring(int beginIndex)
// substring(int beginIndex,int endIndex)
