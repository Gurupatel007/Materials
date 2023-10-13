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
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int p1 = 0;
            int p2 = getnum.TextLength - 1;
            while(p1 <= p2) {
                if (getnum.Text[p1] == getnum.Text[p2]) {
                    p1++;
                    p2--;
                }
                else {
                    lbl.Text = "Not Palindrome";
                    return;
                }
            }
            lbl.Text = "Palindrome";
        }
    }
}
