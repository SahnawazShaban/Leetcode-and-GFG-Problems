class Password{
    private String pw;

    //Getters and Setters
    public String getPassword(){
        return this.pw;
    }
    public void setPassword(String pass){
        this.pw=pass;
    }

}
public class GetSet {
    public static void main(String[] args) {
        Password p = new Password();
        p.setPassword("shaaanshaban");
        System.out.println(p.getPassword());
//        p.pw="12344";
//        System.out.println(p.pw);
    }
}
