import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

public class DynamicInput {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");

            String url = "jdbc:mysql://localhost:3306/youtube";
            String username = "root";
            String password = "8140402685";

            Connection con = DriverManager.getConnection(url,username,password);

            String q = "insert into table1(tName,tCity) values (?,?)";

            //get the PreparedStatement object

            PreparedStatement pstmt  =con.prepareStatement(q);

            //Set Dynamically

            BufferedReader br =new BufferedReader(new InputStreamReader(System.in));

            System.out.println("Enter Name : ");
            String name = br.readLine();

            System.out.println("Enter City : ");
            String city = br.readLine();

            //set the value to query

            pstmt.setString(1,name);
            pstmt.setString(2,city);

            pstmt.executeUpdate();

            System.out.println("Inserted .....");

            con.close();
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}
