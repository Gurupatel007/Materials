using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Practical7
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.listBox1.Items.Remove(listBox1.SelectedItem);
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.listBox1.Items.Add(this.textBox1.Text);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.listBox2.Items.Add(this.textBox2.Text);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.listBox2.Items.Remove(listBox2.SelectedItem);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (listBox1.Items.Count > 0)
            {
                for (int i = listBox1.SelectedItems.Count - 1; i >= 0; i--)
                {
                    this.listBox2.Items.Add(listBox1.SelectedItem);
                    this.listBox1.Items.Remove(listBox1.SelectedItem);
                }
            }
            else
            {
                MessageBox.Show("Please Selecte items");

            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (listBox2.Items.Count > 0)
            {
                for (int i = listBox2.SelectedItems.Count - 1; i >= 0; i--)
                {
                    this.listBox1.Items.Add(listBox2.SelectedItem);
                    this.listBox2.Items.Remove(listBox2.SelectedItem);
                }
            }
            else
            {
                MessageBox.Show("Please Selecte items");
            }

        }
    }
}
