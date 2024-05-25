import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;


public class PreparedStatement1 {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            String url = "jdbc:mysql://localhost:3306/youtube";
            String username = "root";
            String password = "8140402685";

            Connection con = DriverManager.getConnection(url,username,password);

                                       //parameterIndex
            //create a query               1      2
            String q= "insert into table1(tName,tCity) values (?,?)";

            //get the PreparedStatement object
            PreparedStatement pstmt = con.prepareStatement(q);

            pstmt.setString(1,"Shaan Shaban");
            pstmt.setString(2,"Gujarat");

            pstmt.executeUpdate();

            System.out.println("Inserted...");
            con.close();
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}
