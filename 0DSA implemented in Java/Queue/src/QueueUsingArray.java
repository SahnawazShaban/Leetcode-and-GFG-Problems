import javax.swing.plaf.IconUIResource;
import java.util.Scanner;

class queue{
    int f=-1,r=-1;
    int n=10;
    int[] qu = new int[n];

    void enqueue(Scanner sc){
        System.out.println("Enter your element : ");
        int i = sc.nextInt();

        if (r == (n-1)){
            System.out.println("Queue is Overflow.");
        }
        else if (f == -1 && r == -1){
            r++;
            f++;
            qu[r] = i;
            System.out.println("Enqueue Sccessfully.");
        }
        else {
            r++;
            qu[r] = i;
            System.out.println("Enqueue Sccessfully.");
        }
    }

    void dequeue(){
        if (f == -1 && r == -1){
            System.out.println("Queue is Underflow.");
        }
        else {
            f++;
            System.out.println("Dequeue Successfully.");
        }
    }
    void display(){
        System.out.println("Element of Queue : ");
        for (int i=f;i<=r;i++){
            System.out.println(qu[i]);
        }
    }
}
public class QueueUsingArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        queue que = new queue();
        int l = 0;
        do {
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Dispaly");
            System.out.println("Choose your option : ");
            int d = sc.nextInt();
            if (d == 1 || d == 2 || d==3){
                switch (d){
                    case 1:
                        que.enqueue(sc);
                        break;
                    case 2:
                        que.dequeue();
                        break;
                    case 3:
                        que.display();
                        break;
                }
            }
            else {
                System.out.println("Enter Valid number.");
                continue;
            }

            System.out.println("0 for Main Menu");
            System.out.println("Any number for Exit");

            l = sc.nextInt();
        }while (l == 0);
    }
}
