//Single level inheritance
//Multi-Level Inheritance
//Hierarchial Inheritance
//Hybrid Inheritance
import bank.Account;
class Shape{
    public void area(){
        System.out.println("Display area");
    }
}
class Triangle extends Shape{
    public void area(int l,int h){
        System.out.println((1/2)*l*h);
    }

}
//class EquivalentTriangle extends Triangle{
//    public void area(int l,int h){
//        System.out.println((1/2)*l*h);
//    }
//
//}

class Circle extends Shape{
    public void area(int r){
        System.out.println(3.14*r*r);
    }
}
public class Inheritance {
    public static void main(String[] args) {
//        Triangle t1=new Triangle();
//        t1.area(2);

//        bank.Account b1=new bank.Account();
//        b1.name = "Customer - 1";

        Circle sh = new Circle();
        sh.area(2);
    }
}
