import java.util.Scanner;

public class Testing {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int a = Integer.parseInt(String.valueOf(in.nextLine()));
        for(int i=1;i<=100;i++){
            int answer = a*i;
            System.out.println(String.format("%s X %s = %s",a,i,answer));
        }
    }
}
