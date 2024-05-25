import java.sql.Connection;
import java.sql.DriverManager;

public class ConnectionProvider {
    private static Connection con;

    public static Connection getConnection() {

        try {
            if (con == null){
                Class.forName("com.mysql.cj.jdbc.Driver");

                String url = "jdbc:mysql://localhost:3306/youtube";
                String username = "root";
                String password = "8140402685";

                con = DriverManager.getConnection(url,username,password);
            }
        }
        catch (Exception e){
            e.printStackTrace();
        }

        return con;
    }
}
