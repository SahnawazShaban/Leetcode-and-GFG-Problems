public class WholeFibonacciSum {
    public static void main(String[] args) {
        int first_num = 0;
        int second_num = 1;
        int n=5, sum=0, i=0;

        int[] fibo = new int[n];
        System.out.print(first_num + " "+ second_num);

        while (n-2 != 0){
            sum=first_num+second_num;
            System.out.print(" "+sum);
            fibo[i] = sum;
            first_num = second_num;
            second_num = sum;

            n--;
        }
    }
}
