
class Student1{
    String movieNAme;
    int ticketPrice;

    public void show(){
        System.out.println("Movie name is "+ movieNAme);
        System.out.println("Ticket Price is "+ ticketPrice);
    }

    // 3 condition in Overloading - Constructor Overloading and Method Overloading
    /*
    1. Number of argument different
    2. Type of arguments different
    3. Order or arguments may differ
     */
    public void show(int t){
        //statements
    }
}

public class Method_overloading {
    public static void main(String[] args) {
        // Creating object of class

        Student1 st1 = new Student1();
        st1.movieNAme = "Oppenheimer";
        st1.ticketPrice = 300;

        st1.show();
    }
}

//OUTPUT
/*
Movie name is Oppenheimer
Ticket Price is 300
*/