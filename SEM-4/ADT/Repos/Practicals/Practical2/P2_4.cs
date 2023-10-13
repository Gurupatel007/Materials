using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicals
{
    internal class P2_4
    {
        static void Main(string[] args)
        {
            Console.Write("Enter any numeric value:");
            int a=int.Parse(Console.ReadLine());
            if(a%4==0 || a%400==0 && a % 100 != 0)
            {
                Console.WriteLine("{0} is leap year.",a);
            }
            else
            {
                Console.WriteLine("{0} is not leap year.",a);
            }
        }
    }
}
