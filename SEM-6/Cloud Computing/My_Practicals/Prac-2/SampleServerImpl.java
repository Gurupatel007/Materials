import java.rmi.*;
import java.rmi.server.*;
import java.rmi.registry.*;
import java.rmi.Remote;
import java.rmi.RemoteException;

public class SampleServerImpl extends UnicastRemoteObject implements SampleServer{
    SampleServerImpl() throws RemoteException{
        super();
    }
    public static void main(String[] args) {
        try{
            // System.setSecurityManger(new RMISecurityManager());
            SampleServerImpl Server = new SampleServerImpl();

            Naming.rebind("SAMPLE-SERVER", Server);

            System.out.println("Server waiting....");
        }
        catch(java.net.MalformedURLException me){
            System.out.println("Malformed URL: +"+me.toString());
        }
        catch(RemoteException re){
            System.out.println("RmeoteException: "+re.toString());
        }
        
    }
    public int sum(int a,int b) throws RemoteException{
        return a+b;
    }
}

// import java.rmi.Remote;
// import java.rmi.RemoteException;

// // This is your remote interface. It should only include instance methods that throw RemoteException.
// public interface SampleInterface extends Remote {
//     void sampleMethod() throws RemoteException;
// }

// // This is your implementation of the remote interface.
// public class SampleServer implements SampleInterface {
//     public void sampleMethod() throws RemoteException {
//         // Implementation here.
//     }
// }

// // This is your class with the main method. It does not implement the remote interface.
// public class MainClass {
//     public static void main(String[] args) {
//         // Start your RMI server here.
//     }
// }
