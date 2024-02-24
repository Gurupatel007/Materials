import java.rmi.*;
import java.rmi.RemoteException; // Add the missing import statement

public interface SampleServer extends Remote{
    public int sum(int a, int b) throws RemoteException;

    // public static void main(String[] args) {
    //     // Add your main method code here
    // }
}