using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicals
{
    internal class P2_3
    {
        static void Main(string[] args)
        {
            try
            {
                Console.Write("Enter the number: ");
                int a=int.Parse(Console.ReadLine());
                if(a%2==0 )
                {
                    Console.WriteLine("Entered number is even.");
                }
                else
                {
                    throw new ArithmeticException("Entered number is odd.");
                }
            }
            catch (ArithmeticException e){
                Console.WriteLine(e.Message);
            }
            Console.ReadKey();
        }
    }
}
