abstract class Animal1{
    abstract void walk();
}

class Tiger extends Animal1{
    public void walk(){
        System.out.println("Hi, I am Tiger");
    }
}

class Gorilla extends Animal1{
    public void walk(){
        System.out.println("Hi, i am gorilla.");
    }
}
public class AbstractClass {
    public static void main(String[] args) {
        Gorilla g1=new Gorilla();
        g1.walk();

        Tiger t1=new Tiger();
        t1.walk();
    }
}
