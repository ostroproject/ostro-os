import java.awt.Button;
import java.awt.HeadlessException;

public class AppRtTestJavaX11Disabled {
    public static void main(String [] args) {
        try {
            Button button = new Button();
        } catch (HeadlessException ex) {
            System.out.println("OK!");
            return;
        }

        System.out.println("X11 not disabled");
    }
}