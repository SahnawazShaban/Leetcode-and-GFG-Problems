package shaan.shaban;

public class App {
    public String str1 = "I am a pulbic user.";

    void printFromClass(){
        System.out.println("Within class : "+str1);
    }


    public static void main(String[] args) {
        App obj=new App();
        obj.printFromClass();
        System.out.println(obj.str1);

        App2 obj2=new App2();
        obj2.printOutsideClass();
    }

}

class App2{
    App app=new App();
    void printOutsideClass(){
        System.out.println("Within package but Outside Class : "+app.str1);
    }
}
