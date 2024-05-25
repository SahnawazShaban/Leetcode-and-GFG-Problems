import com.mysql.jdbc.Driver;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class CreateTable {
    public static void main(String[] args) {
        try {
            //1)load the driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            //2)Create a connection
            String url = "jdbc:mysql://localhost:3306/youtube";
            String username = "root";
            String password = "8140402685";
            Connection con = DriverManager.getConnection(url,username,password);

            //3)Create a query
            //Table with its structure
            String q = "create table table1(tId int(20) primary key auto_increment, tName varchar(200) not null, tCity varchar(40))";

            //Create a Statement
            Statement stmt = con.createStatement();
            stmt.executeUpdate(q);

            System.out.println("Table Created in Database.");

            con.close();
//            if (con.isClosed()){
//                System.out.println("Connection is not created.");
//            }
//            else {
//                System.out.println("Connection Created.");
//            }
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}
