import shaan.shaban.App;

public class Vivo {
    public static void main(String[] args) {
        App vi=new App();
        System.out.println("Outside Package non-child class : "+vi.str1);

        App3 obj3=new App3();
        obj3.printFromChildClass();
    }
}

class App3 extends App{
    void printFromChildClass(){
        App3 obj3=new App3();
        System.out.println("Child Class : "+obj3.str1);
    }
}