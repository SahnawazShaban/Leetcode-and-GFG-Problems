class Student{
    int age;
    String name;
}

public class Person {
    public static void main(String[] args) {
        Student Shaan = new Student();
//        age is the local variable but it is not exist in this class
//        age = 20; - > you don't do like this you fucking ass hole
        Shaan.name = "Shaban";
        System.out.println(Shaan.name);
    }
}
