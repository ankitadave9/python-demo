import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;

import static java.lang.Thread.sleep;

public class BodgeIgnite {
    public static void main(String[] args) throws IOException, InterruptedException {
        for (int i = 0; i < 9999; i++) {
            Socket socket = new Socket("localhost", 47500);
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);

            out.println("Hello from JAVA TCP Client");
            System.out.println("calling ...");
            out.close();
            socket.close();
            sleep(2000);
        }

    }
}
