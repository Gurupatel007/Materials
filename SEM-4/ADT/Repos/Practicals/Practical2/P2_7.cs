using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicals
{
    internal class P2_7
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the number: ");
            int n = int.Parse(Console.ReadLine());
            int i, j;
            int temp = 1;
            for (i = 1; i < n; i++)
            {
                for (j = 0; j < i; j++)
                {
                    Console.Write(temp + " ");
                    temp++;
                }
                Console.Write("\n");
            }
        }
    }
}
