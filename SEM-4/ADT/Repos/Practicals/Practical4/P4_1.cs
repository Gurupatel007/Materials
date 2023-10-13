using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practical4
{
    internal class P4_1
    {
        const int Passd = 9909;
        static void Main(string[] args)
        {
            int yn, n;
            ATM ob1=new ATM();
            Console.WriteLine("Enter your Password :");
            int pass=int.Parse(Console.ReadLine());
            if(pass==Passd){
                do
                {
                    Console.WriteLine("Choose one option:\n1->Balance_check\n2->Debit\n3->Credit\n4->Get_info :");
                    n = int.Parse(Console.ReadLine());
                    switch (n)
                    {
                        case 1:
                            ob1.Balance_check();
                            break;
                        case 2:
                            ob1.Debit();
                            break;
                        case 3:
                            ob1.Credit();
                            break;
                        case 4:
                            ob1.Get_info();
                            break;
                        default:
                            Console.WriteLine("Enter valid option.");
                            break;
                    }
                    Console.WriteLine("Do you Want to continue?\n1->yes | 0->no");
                    yn = int.Parse(Console.ReadLine());
                } while (yn == 1);
            }
            else 
            {
                Console.WriteLine("Wrong Password!!!");
            }
            Console.ReadKey();
        }
    }
    public class ATM
    {
        const int Passwd = 99099;
        string name;
        long acc_no=560102393;
        int balance=50000;
        long mob;
        string add;
        public void Balance_check()
        {
            Console.WriteLine("Enter your Password");
            int psd=int.Parse(Console.ReadLine());
            if (psd == Passwd)
            {
                Console.WriteLine("Account No :" + acc_no);
                Console.WriteLine("Your Current Balance :" + balance);
            }
            else
            {
                Console.WriteLine("Wrong Password!!!");
            }
        }
        public void Debit()
        {
            Console.WriteLine("Enter the Password.");
            int y = int.Parse(Console.ReadLine());
            if(y==Passwd){

                Console.WriteLine("Enter the amount to withdraw :");
                int x = int.Parse(Console.ReadLine());
                if (x > balance)
                {
                    Console.WriteLine("Insufficient Balance.");
                }
                else
                {
                    balance = balance - x;
                    Console.WriteLine("Withdrawl Succesfull.");
                    Console.WriteLine("Your Current Balance :" + balance);
                }
            }
            else
            {
                Console.WriteLine("Wrong Passwoed!!!");
            }
        }
        public void Credit()
        {
            Console.WriteLine("Enter the amount to credit.");
            int credit=int.Parse(Console.ReadLine()) ;
            balance= balance + credit ;
            Console.WriteLine("Credit Succesfull") ;
            Console.WriteLine("your current balance :" + balance);
        }
        public void Get_info()
        {
            Console.WriteLine("Enter your name: ");
            name=Console.ReadLine();
            Console.WriteLine("Enter your address :");
            add =(Console.ReadLine());
            Console.WriteLine("Enter your mobile no :");
            mob=int.Parse(Console.ReadLine());

            Console.WriteLine("Name :"+name);
            Console.WriteLine("Address :"+add);
            Console.WriteLine("Mobile No :"+mob);

        }
    }
}
