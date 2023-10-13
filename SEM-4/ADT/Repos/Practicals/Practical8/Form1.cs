using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
namespace Practical8
{
    public partial class Form1 : Form
    {
        FileInfo f = new FileInfo(@"C:\Users\gurup\OneDrive\Desktop\ADT\File.txt");
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            f.Create();
            MessageBox.Show("File Created");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            f.Delete();
            MessageBox.Show("File Deleted");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            f.CopyTo(@"C:\Users\gurup\OneDrive\Desktop\ADT\File1.txt");
            MessageBox.Show("File Copied");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            StreamWriter sc = new StreamWriter(f.OpenWrite());
            sc.Write(textBox1.Text);
            textBox1.Clear();
            sc.Close();
        }

        private void button5_Click(object sender, EventArgs e)
        { 
                StreamReader sr = new StreamReader(f.OpenRead());
                string s = " ";
                while ((s = sr.ReadLine()) != null)
                {
                    textBox1.Text = s;
                }
                sr.Close();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            f.MoveTo(@"C:\Users\gurup\OneDrive\Desktop");
            MessageBox.Show("File Moved");
        }
    }
}
