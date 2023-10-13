using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practical4
{
    internal class P4_2
    {
        static void Main(string[] args)
        {
            int n = args.Length;
            int[] arr = new int[n];
            //Initialize array   
            for (int i = 0; i < args.Length; i++)
            {
                arr[i] = int.Parse(args[i]);
            }
                //Array fr will store frequencies of element  
                int[] fr = new int[arr.Length];
                int visited = -1;

                for (int i = 0; i < arr.Length; i++)
                {
                    int count = 1;
                    for (int j = i + 1; j < arr.Length; j++)
                    {
                        if (arr[i] == arr[j])
                        {
                            count++;
                            //To avoid counting same element again  
                            fr[j] = visited;
                        }
                    }
                    if (fr[i] != visited)
                        fr[i] = count;
                }

                //Displays the frequency of each element present in array  
                Console.WriteLine("---------------------");
                Console.WriteLine(" Element | Frequency");
                Console.WriteLine("---------------------");
                for (int i = 0; i < fr.Length; i++)
                {
                    if (fr[i] != visited)
                        Console.WriteLine("    " + arr[i] + "    |    " + fr[i]);
                }
                Console.WriteLine("---------------------");
            


        }
    }
}