import java.rmi.RemoteException;
import java.rmi.*;
import java.rmi.server.*;
com SampleClient;

public class SampleClient {
    public static void main(String[] args) {
        try{
            System.out.println("Security Manager loaded");
            String url="//localhost/SAMPLE-SERVER";

            SampleServer remoteObject = (SampleServer)Naming.lookup(url);
            System.out.println("Got remote object");

            System.out.println("10 + 20 = "+remoteObject.sum(10, 20));
        }
        catch(RemoteException exc){
            System.out.println(("Error int lookup: "+exc.toString()));
        }
        catch(java.net.MalformedURLException exc){
            System.out.println("Malformed URL: "+exc.toString());
        }
        catch(java.rmi.NotBoundException exc){
            System.out.println("NotBound: "+exc.toString());
        }
    }    
}
