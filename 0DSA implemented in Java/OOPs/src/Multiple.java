//Interface Example
interface Animal{
    public void smell();
}

class Lion implements Animal{
    public void smell(){
        System.out.println("HI, I am Lion.");
    }
}
public class Multiple {
    public static void main(String[] args) {
        Lion l1 = new Lion();
        l1.smell();
    }
}
