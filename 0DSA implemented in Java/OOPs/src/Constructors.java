public class Constructors {
    int a,b;
    Constructors(int x, int y){
        System.out.println("COnstructor is called.");
        a = x;
        b = y;
    }

    int sub(){
        return a-b;
    }
    int add(){
        return a+b;
    }
    int mul(){
        return a*b;
    }

    public static void main(String[] args) {
        Constructors co=new Constructors(10,2);
        System.out.println("Subtraction : "+co.sub());
        System.out.println("Addition : "+co.add());
        System.out.println("Multiplication : "+co.mul());

        Constructors co1 = new Constructors(19,5);
        System.out.println("Subtraction : "+co1.sub());
        System.out.println("Addition : "+co1.add());
        System.out.println("Multiplication : "+co1.mul());

    }
}
