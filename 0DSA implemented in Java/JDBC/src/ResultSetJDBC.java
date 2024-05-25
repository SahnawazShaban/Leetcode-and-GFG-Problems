import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;

public class ResultSetJDBC {
    public static void main(String[] args) {
        try {
            Connection con = ConnectionProvider.getConnection();

            String q="select * from table1";

            Statement stmt = con.createStatement();

            ResultSet set = stmt.executeQuery(q);

            while (set.next()){
                int id = set.getInt(1);
                String name = set.getString(2);
                String city = set.getString(3);

                System.out.print(id + " ");
                System.out.print(name + " ");
                System.out.println(city);
            }
            con.close();
        }
        catch (Exception e){
            e.printStackTrace();
        }

    }
}
