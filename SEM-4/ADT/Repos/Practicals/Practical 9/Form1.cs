using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Practical_9
{
    
    public partial class Form1 : Form
    {
        int total = 0, i = 0;

        public Form1()
        {
            InitializeComponent();
        }
        private void comboBox1_ValueChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listView1.Columns.Add("Item_name");
            listView1.Columns.Add("Price");
            listView1.View = View.Details;
            listView1.GridLines = true;
            string[] item = { "Pizza", "Cold coffee", "Tea", "Coffee", "Sandwich" };
            int[] price = { 200, 45, 20, 25, 50 };
            for (int i = 0; i < 5; i++)
            {
                add_items(item[i], price[i]);
            }

            listView2.Columns.Add("Item_names");
            listView2.Columns.Add("Price");
            listView2.Columns.Add("Quantity");
            listView2.View = View.Details;
            listView2.GridLines = true;
        }
            private void add_items(string item, int price)
            {
                ListViewItem l = new ListViewItem(item);
                l.SubItems.Add(price.ToString());
                listView1.Items.Add(l);
            }

        private void button2_Click(object sender, EventArgs e)
        {
            int cost =Convert.ToInt32(listView2.SelectedItems[0].SubItems[1].Text);
            int q =Convert.ToInt32(listView2.SelectedItems[0].SubItems[2].Text);

            int cancleItem_Total = cost * q;
            total = total - cancleItem_Total;
            listView2.Items.Remove(listView2.SelectedItems[0]);
            label3.Text = total.ToString();
            i--;

        }

        private void button1_Click(object sender, EventArgs e)
            {
                int p, q;
                string iname;
                p = int.Parse(listView1.SelectedItems[0].SubItems[1].Text);
                q = int.Parse(numericUpDown1.Text);
                iname = listView1.SelectedItems[0].Text;
                listView2.Items.Add(iname);
                listView2.Items[i].SubItems.Add(p.ToString());
                listView2.Items[i].SubItems.Add(q.ToString());
                i++;
                p = p * q;
                total = total + p;
                label3.Text = total.ToString();
                label3.Visible = true;
            }
    }
}
