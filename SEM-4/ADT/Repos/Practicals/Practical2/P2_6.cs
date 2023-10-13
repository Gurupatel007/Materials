using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practicals
{
    internal class P2_6
    {
        static void Main(string[] args)
        {
            int sum = 0;
            int flag = 0;
            Console.WriteLine("Enter the number: ");
            int n =int.Parse(Console.ReadLine());
            for (int i = 2; i <= n / 2; i++)
            {
                if (n % i == 0)
                {
                    flag++;
                    break;

                }
            }
            while (n != 0)
            {
                sum += n % 10;
                n = n / 10;
            }
            for (int i = 2; i <= sum / 2; i++)
            {
                if (sum % i == 0)
                {
                    flag++;
                    break;

                }
            }

            if (flag == 0)
                Console.Write("It is Lucky");
            else
                Console.Write("It is not Lucky");
        }
    }
}
