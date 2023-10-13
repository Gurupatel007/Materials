using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Practical6
{
    public partial class P6_2 : Form
    {
        public P6_2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            StringBuilder str = new StringBuilder();
            for (int i = int.Parse(textBox1.Text); i <= int.Parse(textBox2.Text); i++)
            {
                int j = i;
                int sum = 0;
                while (j > 0)
                {
                    int rem = j % 10;
                    sum += rem * rem * rem;
                    j = j / 10;
                }
                if (i == sum)
                {
                    str.Append(" ");
                    str.Append(i.ToString());
                }
            }
            label1.Visible = true;
            label1.Text = str.ToString();
        }
    }
}
