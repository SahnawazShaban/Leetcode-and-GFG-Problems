import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.PreparedStatement;

public class ImageStoreBasic {
    public static void main(String[] args) {
        try {
            Connection c = ConnectionProvider.getConnection();

            String q = "insert into images(pic) values(?)";

            PreparedStatement pstmt = c.prepareStatement(q);

            FileInputStream fis = new FileInputStream("Sahnawaz.jpg");

            pstmt.setBinaryStream(1,fis,fis.available());

            pstmt.executeUpdate();

            System.out.println("DONE .....");
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}
