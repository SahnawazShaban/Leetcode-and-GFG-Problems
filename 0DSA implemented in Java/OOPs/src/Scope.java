public class Scope {
    int a=10;

    int demo(){
        int a = 10;

        System.out.println(a);

        {
            int b=20;
            System.out.println(b);
            System.out.println(a);
        }

        {
            int b=100;
            System.out.println(b);
            System.out.println(a);
        }

        for (int i=0;i<=5;i++){
            System.out.println(i);
        }
//        System.out.println(b); -> it is not accessible
        return 0;
    }
    int add(){ //method-level scope of variable
        int a = 10;
        int b = 5;
        return a+b;
    }
    int sub(){
        int a = 10;
        int b = 5;
        return a-b;
    }
    public static void main(String[] args) {
        Scope sc = new Scope();
        System.out.println(sc.add());
        System.out.println(sc.sub());
        System.out.println(sc.demo());
    }
}
