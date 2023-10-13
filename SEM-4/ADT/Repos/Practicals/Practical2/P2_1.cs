using System;
using System.Diagnostics;

namespace Practicals
{
    class P2_1
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the Integer Value: ");
            int a = int.Parse(Console.ReadLine());

            Console.WriteLine("Enter the Double Value: ");
            double b = double.Parse(Console.ReadLine());

            Console.WriteLine("Enter the Char Value: ");
            char c = char.Parse(Console.ReadLine());

            Console.WriteLine("Enter the String Value: ");
            string d = Console.ReadLine();

            Console.WriteLine(a);
            Console.WriteLine(b);
            Console.WriteLine(c);
            Console.WriteLine(d);
        }
    }
}

