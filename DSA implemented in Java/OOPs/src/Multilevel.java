class Multilevel {
    public void multi(){
        System.out.println("This is Grand parent Class.");
    }
}

class Y extends Multilevel{
    public void multi1(){
        System.out.println("This is Parent Class.");
    }
}

class Z extends Y{
    public void multi2(){
        System.out.println("This is Child Class.");
    }

    public static void main(String[] args) {
        Z z1 = new Z();
        z1.multi();
        z1.multi2();
        z1.multi1();
    }
}
