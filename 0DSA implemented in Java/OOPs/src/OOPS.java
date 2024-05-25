class Pen{
    String color;
    String type;

    public void write(){
        System.out.println("Sahnawaz Shaban");
    }

    public void printColor(){
        System.out.println(this.color);
        //kisi bhi method ke andar, kissi bhi
        // scope me batata hai ki uss method ko
        // us jagah ko konsi object access karne
        // ki kosis kar rahi hai

        //Inside any method, in any scope, it tells
        //which object the method is trying to access at that place.
    }
}

class Student1{
    String name;
    int age;

    public void info(){
        System.out.println(this.name);
        System.out.println(this.age);
    }

    Student1(){
        System.out.println("Constructor called....");
    }
    Student1(String name,int age){
        this.name = name;
        this.age = age;
    }
}
public class OOPS {
    public static void main(String[] args) {
        Student1 s1 = new Student1();
        s1.name = "Shaan";
        s1.age = 22;
        Student1 s2 = new Student1();
        s2.info();
        //new is a keyword -> jesse hi humne new keyword
        // laga diya memory heap ke andar, ek jagah allocate
        // ho jayegi, aur uss jagah ke andar hamari puri ki
        // puri object ja kar store hojayegi.waha jagah humne
        // object ke hisab se allocate kar diye hai.

        //we will allocate a space in the memory heap,
        // and we will store our entire object in that
        // space. Where we allocate space according to
        // our object.

//        stu1.name = "Sahnawaz";
//        stu1.age = 12;
//        stu1.info();

//        Pen pen1 = new Pen();
//        pen1.color = "blue"; //blue color assign to color
//        pen1.type = "gel"; //gel type assign to type
//
//        Pen pen2 = new Pen();
//        pen2.color = "black";
//        pen2.type = "ink";
//
//        pen1.printColor();
//        pen2.printColor();
    }
}
