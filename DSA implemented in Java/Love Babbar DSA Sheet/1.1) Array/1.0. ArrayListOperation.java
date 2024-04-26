import java.util.ArrayList;
import java.util.Collections;

public class ArrayListOperation {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();

        //Add elements - list.add(int index)
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        System.out.println("Add Element : "+list);

        //Get element - get an element with its index
        int ele = list.get(0); //get(int index)
        System.out.println("Get element "+ele);

        //Add element in between - list.add(int index,int element)
        list.add(1,10);
        System.out.println("Add Element in between : "+list);

        //Set element
        list.set(3,12);
        System.out.println("Set Elements : "+list);

        //Delete element
        list.remove(0);
        System.out.println("After Remove Element : "+list);

        //size of list
        int size = list.size(); // return integer value
        System.out.println("Size is "+size);

        //loops / Iterative
        System.out.println("List values using loops.");
        for (int i=0;i<list.size();i++){
            System.out.println(list.get(i));
        }

        //Sorting - Ascending or descending order
        Collections.sort(list);  //Collection is class and inside it, we have sort function
        System.out.println(list);

    }
}
