package shaan.shaban;

public class Main {
    public static void main(String[] args) {
        LL list = new LL();


        //Insert At First
//        list.insertFirst(1);
//        list.insertFirst(3);
//        list.insertFirst(2);
//        list.insertFirst(8);
//        list.insertFirst(4);
//        list.insertFirst(16);
//
//        //Insert At Last
//        list.insertLast(12);
//
//        //Insert At Anywhere
//        list.insert(11,2);
//
//        //Display elements
//        list.display();
//
//        System.out.println("Deleted First element : "+list.deleteFirst());
//        list.display();
//
//        System.out.println("Deleted Last element : "+list.deleteLast());
//        list.display();
//
//        System.out.println("Deleted particular element : "+list.delete(2));
//        list.display();
//
//        System.out.println("Find element : ");
//        list.find(1);
//        list.display();
//
//        list.insert(5,2);
//        list.display();


        //these elements only for remove duplicate
        list.insertFirst(1);
        list.insertFirst(1);
        list.insertFirst(1);
        list.insertFirst(2);
        list.insertFirst(2);
        list.insertFirst(3);

        list.display();
        list.duplicate();
        list.display();


//        DLL dll = new DLL();
//
//        dll.insertFirstDll(3);
//        dll.insertFirstDll(4);
//        dll.insertFirstDll(6);
//        dll.insertFirstDll(12);
//        dll.insertFirstDll(19);
//
//        dll.display();
//
////        dll.displayRev();
//        dll.insertLastDll(20);
//        dll.display();
//
//        dll.insertDll(6,100);
//        dll.display();

//        CLL cll = new CLL();
//
//        cll.insert(12);
//        cll.insert(42);
//        cll.insert(11);
//        cll.insert(9);
//        cll.insert(7);
//
//        cll.display();
//
//        cll.delete(9);
//
//        cll.display();
    }
}
