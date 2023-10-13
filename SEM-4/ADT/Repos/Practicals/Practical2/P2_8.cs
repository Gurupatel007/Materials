using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicals
{
    internal class P2_8
    {
        static void Main(string[] args)
        {
            Console.Write("Enter the string: ");
            String s= Console.ReadLine();
            Console.WriteLine("Enter the stirng you want to change: ");
            String s1=Console.ReadLine();
            Console.WriteLine("Enter the new string: ");
            String s2=Console.ReadLine();
            String rep = s.Replace(s1, s2);
            Console.Write("New String is: " + rep + " \n\n");
            Console.ReadKey();
        }
    }
}
