import javax.sound.midi.Soundbank;
import java.util.Scanner;

class stack{
    int top = -1;
    int n=10;
    int[] st = new int[n];

    void push(Scanner sc){
        if (top == (n-1)){
            System.out.println("Stack is Overflow.");
        }
        else {
            System.out.println("Enter Your value : ");
            int i = sc.nextInt();
            top++;
            st[top] = i;
            System.out.println("Push successfully.");
        }
    }

    void pop(){
        if (top == -1){
            System.out.println("Stack is underflow.");
        }
        else {
            top--;
            System.out.println("pop successfully.");
        }
    }
    void display(){
        System.out.println("Element of Stack : ");
        for (int i=top;i>=0;i--){
            System.out.println(st[i]);
        }
        System.out.println();
    }
}
public class StackUsingArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        stack stk = new stack();
        int l;
        do {
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Display");
            System.out.println("Choose your Option : ");
            int n = sc.nextInt();

            switch (n){
                case 1:
                    stk.push(sc);
                    break;
                case 2:
                    stk.pop();
                    break;
                case 3:
                    stk.display();
                    break;
            }
            System.out.println("Enter 0 to go back to the Main Menu.");
            System.out.println("Enter any key to EXIT.");
            l = sc.nextInt();
        }while (l == 0);
    }
}
