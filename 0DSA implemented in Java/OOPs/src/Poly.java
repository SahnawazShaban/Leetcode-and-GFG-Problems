class Student2{
    String name;
    int age;

    public void printInfo(String name){
        System.out.println(name);
    }
    public void printInfo(int age){
        System.out.println(age);
    }
    public void printInfo(String name,int age){
        System.out.println(name+" "+age);
    }
}
public class Poly {
    public static void main(String[] args) {
        Student2 s1=new Student2();
        s1.printInfo("Shaan");
    }
}
