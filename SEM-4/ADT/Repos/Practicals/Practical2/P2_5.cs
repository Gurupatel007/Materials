using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicals
{
    internal class P2_5
    {
        static void Main(string[] args)
        {
            int sum = 0, n,i;

            Console.WriteLine("Enter any Number: ");
            n=int.Parse(Console.ReadLine());

            for (i = 1; i < n; i++)
            {
                if(n%i==0)
                {
                    sum += i;
                }
            }

            if (sum == n)
            {
                Console.WriteLine("{0} is Perfect.", n);
            }
            else { Console.WriteLine("{0} is not perfect.", n); }
            Console.ReadKey();
        }
    }
}
