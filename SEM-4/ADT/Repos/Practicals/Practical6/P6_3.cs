using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Text.RegularExpressions;

namespace Practical6
{
    public partial class P6_3 : Form
    {
        public P6_3()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Regex r = new Regex("^[6-9][0-9]{9}$");
            if (textBox1 == null)
            {
                label4.Visible = true;
                label4.Text = "Enter a valid Mobile Number";
            }
            else if (r.IsMatch(textBox1.Text))
            {
                label4.Visible = true;
                label4.Text = "valid Mobile Number";
            }
            else
            {
                label4.Visible = true;
                label4.Text = "Invalid Mobile Number";
            }
            if(textBox2.Text== "" || textBox3.Text== "")
            {
                label5.Visible= true;
                label5.Text = "Please Enter a password";
            }
            else if(textBox2.Text == textBox3.Text)
            {
                label5.Visible= true;
                label5.Text = "Password Matched";
            }
            else
            {
                label5.Visible= true;
                label5.Text = "Passwor didn't Matched";
            }
        }
    }
}
