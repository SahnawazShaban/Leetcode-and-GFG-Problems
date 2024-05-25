public class PassByValue {
    static void changeValue(int a){
        a += 10;
        System.out.println("Inside method : "+a);
    }
    public static void main(String[] args) {
        int a=10;
        System.out.println("Before calling method : "+a);
        changeValue(a);
        System.out.println("After calling method : "+a);
    }

//    NOTE : Java doesn't have pass by reference
}
