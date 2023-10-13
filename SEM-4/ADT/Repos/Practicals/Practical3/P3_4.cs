using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practical3
{
    internal class P3_4
    {
        static void Main(string[] args)
        {
            int[] arr = { 6, 3, 1, 9, 5 };
            int len=arr.Length;
            sorting(arr, len);
            for(int i=0; i<len; i++)
            {
                Console.Write(arr[i]+" ");
            }
            Console.ReadKey();
        }
        static void sorting(int[] arr,int len)
        {
            for(int i=0;i<len-1; i++) 
            { 
                for(int j = i + 1; j < len; j++)
                {
                    if (arr[i] > arr[j])
                    {
                        int temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                    }
                }
            }
        }
    }
}
