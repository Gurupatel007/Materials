import java.util.*;
public class Main {
    public static void main(String[] args) {
//        System.out.println("Hello world!");
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the Message to be Sent : ");
        String data = sc.nextLine();
        System.out.println("Enter the Flag : ");
        char flag = sc.next().charAt(0);
        System.out.println("Enter the Escape Character : ");
        char esc = sc.next().charAt(0);
        String res = new String();

        // Data in each frame is stuffed by 'F' at beginning and end
        data = flag + data + flag;
        for (int i = 0; i < data.length(); i++) {

            // Stuff with 'E' if 'F' is found in the data to be sent
            if (data.charAt(i) == flag && i != 0 && i != (data.length() - 1))
                res = res + esc + data.charAt(i);

                // Stuff with 'E' if 'E' is found in the data to be sent
            else if (data.charAt(i) == esc)
                res = res + esc + data.charAt(i);
            else
                res = res + data.charAt(i);
        }

        System.out.println("The data being sent (with byte stuffed) is : " + res);
        String out = new String();
        for (int i = 1; i < res.length() - 1; i++) {
            String ch = String.valueOf(res.charAt(i));
            // If data contains a 'D' or 'F' do not unstuff it
            if (data.contains(ch) && res.charAt(i)!='E' )//|| res.charAt(i) == 'F')
                out = out + res.charAt(i);

                // If data contains 'E' followed by 'E', de-stuff the former 'E'
            else if (res.charAt(i) == esc && res.charAt(i + 1) == esc) {
                out = out + esc;
                i++;
            }
        }
        System.out.println("The Destuffed Message is : " + out);

    }
}