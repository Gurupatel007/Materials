using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practical4
{
    internal class P4_3
    {
        static void Main(string[] args)
        {
            string a = "Hello Guru";
            StringBuilder sb = new StringBuilder(a);
            sb.Append(" Tulsibhai");
            Console.WriteLine(sb);
            string b = " Patel";
            sb.AppendFormat("{0}",b);
            Console.WriteLine(sb);
            sb.Insert(6,"Mr.");
            Console.WriteLine(sb);
            sb.Remove(0, 6);
            Console.WriteLine(sb);
            sb.Replace("Tulsibhai", "Krishnaben");
            Console.WriteLine(sb);
            Console.ReadKey();
        }
    }
}
