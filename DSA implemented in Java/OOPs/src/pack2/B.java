package pack2;

import pack1.A;

class B extends A {
    public static void main(String[] args) {
//        we should take child reference only
//        parent class must be public otherwise compilation error occur
        B a=new B();
        a.m1();
    }
}
