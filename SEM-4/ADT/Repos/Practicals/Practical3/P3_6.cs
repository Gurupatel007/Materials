using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practical3
{
    internal class P3_6
    {
        static void Main(string[] args)
        {
            int i = 10,j;
            fun1(i);
            Console.WriteLine("Without Reference: "+i);
            fun(ref i);
            Console.WriteLine("With Reference: "+i);
            fun2(out j);
            Console.ReadKey();

        }
        static void fun(ref int i)
        {
            i = 12;
        }
        static void fun1(int i)
        {
            i= 12;
        }
        static void fun2(out int j)
        {
            j = 50;
            Console.WriteLine("With Out keyword: "+(j + 2));
        }
    }
}
