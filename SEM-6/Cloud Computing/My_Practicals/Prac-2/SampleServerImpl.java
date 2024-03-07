import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.rmi.registry.LocateRegistry;

public class SampleServerImpl extends UnicastRemoteObject implements SampleServer{
    SampleServerImpl() throws RemoteException{
        super();
    }
    public int sum(int a,int b) throws RemoteException{
        return a+b;
    }
    public static void main(String[] args) {
        try{
            LocateRegistry.createRegistry(1099);
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
    
}
