import javax.swing.*;
import java.io.File;
import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.PreparedStatement;

public class ImageStore {
    public static void main(String[] args) {
        try {
            // called 'class name : ConnectionProvider' and its method getConnection().
            Connection c = ConnectionProvider.getConnection();

            String q = "insert into images(pic) values(?)";

            PreparedStatement pstmt = c.prepareStatement(q);

            //This is component of Swing
            //jo hame dialog box provide karega, file choose karne ke liye
            JFileChooser jfc = new JFileChooser();

            //parent : null -> center pe dialog box dekhega
            jfc.showOpenDialog(null);

            //jfc.getSelectedFile() - > this return file instance, so store in file object
            File file = jfc.getSelectedFile();

            //file ka reference aagaya fis pe
            FileInputStream fis = new FileInputStream(file);

            //setBinaryStream for image
            pstmt.setBinaryStream(1,fis,fis.available());

            pstmt.executeUpdate();

//            System.out.println("DONE.....");

            //GUI form
            JOptionPane.showMessageDialog(null,"success");
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}
