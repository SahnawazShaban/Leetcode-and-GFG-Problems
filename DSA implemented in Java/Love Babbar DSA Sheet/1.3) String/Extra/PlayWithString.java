import java.util.Scanner;
import java.util.Stack;

public class PlayWithString {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //This is for only single word
        System.out.println("Enter a str1");
        String str1 = sc.next();
        System.out.println(str1); //eg.: shaan


        //This is for sentences
        System.out.println("Enter a str2");
        String str2 = sc.nextLine();
        System.out.println(str2);


        //Concatenation
//        String firstName = "Shaan";
//        String lastName = "Shaban";
//        String fullName = firstName + lastName;
//        System.out.println(fullName);


        //to find length of any string
//        System.out.println(fullName.length());


        //Print each element line by line
//        for (int i=0;i<fullName.length();i++){
//            System.out.println(fullName.charAt(i)+" ");
//        }


        //String Comparison
        String name1 = "Shaan";
        String name2 = "Shaan";

        //s1 > s2 : +ve value
        //s1 == s2 : 0
        //s1 < s2 : -ve value

        //How to decide which one is greater : its
        // depends on first character of string
        // for example hello and wello, so wello is greater.

//        if (name1.compareTo(name2) == 0){
//            System.out.println("String are equal");
//        }
//        else {
//            System.out.println("Not equal");
//        }


        // == is properly working. so why we use compareTo
        // function. read below after this problem
//        if (name1 == name2){
//            System.out.println("String are equal");
//        }
//        else {
//            System.out.println("Not equal");
//        }

        // output : String are not equal.
        //because new String("") created a new space in memory
//        if (new String("Shaan") == new String("Shaan")){
//            System.out.println("String are equal.");
//        }
//        else {
//            System.out.println("String are not equal.");
//        }


        //substring - if i get any part of my string
        //string_name.substring(begin index, end index)
        String name = "My name is Shaan";
        String ans = name.substring(11,13);
        System.out.println(ans);



        //String are Immutable
    }
}
