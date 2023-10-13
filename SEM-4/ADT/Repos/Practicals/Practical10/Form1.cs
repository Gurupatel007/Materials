using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Runtime.Remoting.Contexts;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;
using System.Linq.Expressions;

namespace Practical10
{
    public partial class Form1 : Form
    {
        SqlConnection con=new SqlConnection(@"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\gurup\OneDrive\Documents\guru.mdf;Integrated Security=True;Connect Timeout=30");
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            con.Open();
            SqlCommand cmd=con.CreateCommand();
            cmd.CommandType=CommandType.Text;
            cmd.CommandText = ("insert into guru values('" + textBox1.Text + "','" + textBox2.Text + "','" + textBox3.Text + "')");
            cmd.ExecuteNonQuery();
            MessageBox.Show("Data Inserted");
            con.Close();
            show();

        }
        private void show()
        {
            con.Open();
            SqlCommand cmd= con.CreateCommand();
            cmd.CommandType= CommandType.Text;
            cmd.CommandText = ("Select * from guru");
            cmd.ExecuteNonQuery();
            DataTable dt = new DataTable();
            SqlDataAdapter ad = new SqlDataAdapter(cmd);
            ad.Fill(dt);
            dataGridView1.DataSource = dt;
            con.Close();

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            con.Open();
            SqlCommand cd=con.CreateCommand();
            cd.CommandType= CommandType.Text;
            cd.CommandText = ("update guru set Name='"+textBox1.Text+"' ,Marks='"+textBox2.Text+"' ,Enroll='"+textBox3.Text+"' where Enroll='"+textBox4.Text+"' ");
            cd.ExecuteNonQuery();
            MessageBox.Show("Table Updated");
            con.Close();
            show();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            con.Open();
            SqlCommand cd=con.CreateCommand();
            cd.CommandType= CommandType.Text;
            cd.CommandText = ("delete from guru where Enroll='" + textBox4.Text + "'");
            cd.ExecuteNonQuery();
            MessageBox.Show("Row Deleted");
            con.Close();
            show();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            con.Open();
            SqlCommand cmd = con.CreateCommand();
            cmd.CommandType = CommandType.Text;
            cmd.CommandText = ("Select * from guru where Enroll='" + textBox4.Text + "'");
            SqlDataReader dr = cmd.ExecuteReader();
            while (dr.Read())
            {
                textBox1.Text=dr.GetValue(0).ToString();
                textBox2.Text=dr.GetValue(1).ToString();
                textBox3.Text=dr.GetValue(2).ToString();
            }
            con.Close();
        }
    }
}
