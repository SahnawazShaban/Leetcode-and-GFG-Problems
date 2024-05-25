import java.util.ArrayList;

class Solution {
    
    // Function to sort the list
    public void sortFun(ArrayList<Integer> num) {
        if (num.isEmpty()) {
            return;
        }
        int temp = num.get(num.size() - 1);
        num.remove(num.size() - 1);
        sortFun(num);
        insertSort(num, temp);
    }
    
    // Function to insert an element into a sorted list
    private void insertSort(ArrayList<Integer> num, int temp) {
        if (num.isEmpty() || num.get(num.size() - 1) <= temp) {
            num.add(temp);
            return;
        }
        int val = num.get(num.size() - 1);
        num.remove(num.size() - 1);
        insertSort(num, temp);
        num.add(val);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        ArrayList<Integer> num = new ArrayList<>();
        num.add(4);
        num.add(2);
        num.add(5);
        num.add(8);
        num.add(1);
        num.add(5);
        solution.sortFun(num);
        for (int i : num) {
            System.out.print(i + " ");
        }
    }
}
