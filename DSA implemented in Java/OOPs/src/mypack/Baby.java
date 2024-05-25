package mypack;

public class Baby {
    public void naughtyBaby(){
        System.out.println("I am naughty");
    }
    public void cuteBaby(){
        System.out.println("I am cutie");
    }
    public void smartBaby(){
        System.out.println("I am Smarty");
    }
    public void sportyBaby(){
        System.out.println("I love sports");
    }

    public static void main(String[] args) {
        Baby bi=new Baby();
        bi.sportyBaby();
    }
}

class Mom extends Baby{
    Baby mom=new Baby();
    public void momComplain() {
        System.out.println("Chupppppp.....");
    }
}
