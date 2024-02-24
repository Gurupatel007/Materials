/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package webclient;

/**
 *
 * @author gurup
 */
public class Webclient {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        try{
            server.NewWebService_Service service = new server.NewWebService_Service();
            server.NewWebService port = service.getNewWebServicePort();
            System.out.println(port.sayHello());
            
            int add = port.add(10, 20);
            System.out.println("Addition of 10 and 20: "+add);
            
            int sub = port.sub(30, 20);
            System.out.println("Subtraction of 30 and 20: "+sub);
            
            int mul = port.mul(10, 20);
            System.out.println("Multiplication of 10 and 20: "+mul);
            
            int div = port.div(50, 2);
            System.out.println("Division of 50 and 2: "+div);   
        }catch(Exception ex){
            System.out.println(ex);
        }
    }

    private static String sayHello() {
        server.NewWebService_Service service = new server.NewWebService_Service();
        server.NewWebService port = service.getNewWebServicePort();
        return port.sayHello();
    }

    private static Integer add(int a, int b) {
        server.NewWebService_Service service = new server.NewWebService_Service();
        server.NewWebService port = service.getNewWebServicePort();
        return port.add(a, b);
    }

    private static Integer sub(int a, int b) {
        server.NewWebService_Service service = new server.NewWebService_Service();
        server.NewWebService port = service.getNewWebServicePort();
        return port.sub(a, b);
    }

    private static Integer mul(int a, int b) {
        server.NewWebService_Service service = new server.NewWebService_Service();
        server.NewWebService port = service.getNewWebServicePort();
        return port.mul(a, b);
    }

    private static Integer div(int a, int b) {
        server.NewWebService_Service service = new server.NewWebService_Service();
        server.NewWebService port = service.getNewWebServicePort();
        return port.div(a, b);
    }
    
}
