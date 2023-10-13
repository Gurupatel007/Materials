using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicals
{
    internal class P2_2
    {
        static void Main(string[] args)
        {
            double d;
            try
            {
                Console.Write("Enter any Value: ");
                d=int.Parse(Console.ReadLine());
            }
            catch
            {
                Console.WriteLine("Entered value is not numeric");
            }
            Console.ReadKey();
        }
    }
}
