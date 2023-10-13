using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practical3
{
    internal class P3_5
    {
        static void Main(string[] args)
        {
            fun(2,6,3,8,9,10);

            Console.ReadKey();

        }
        static void fun(params int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                Console.Write(arr[i]+" ");
            }
        }
    }
}
