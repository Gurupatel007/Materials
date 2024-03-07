import java.rmi.*;
import java.rmi.RemoteException; // Add the missing import statement

public interface SampleServer extends Remote{
    public int sum(int a, int b) throws RemoteException;
}