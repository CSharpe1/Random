using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

// This is the code for your desktop app.
// Press Ctrl+F5 (or go to Debug > Start Without Debugging) to run your app.

namespace BinTable
{
    public partial class Form1 : Form
    {
        int Var_Binary_value;

        public Form1() {
          

            InitializeComponent();
        }

        private void linkLabel1_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e) {
            // Click on the link below to continue learning how to build a desktop app using WinForms!
            System.Diagnostics.Process.Start("http://aka.ms/dotnet-get-started-desktop");

        }

        private void button1_Click(object sender, EventArgs e) {
           
        }

        private void Form1_Load(object sender, EventArgs e) {

        }

        private void textBox1_TextChanged(object sender, EventArgs e) {
      
        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e) {
            int Var_Binary_Value = Convert.ToInt32(Math.Round(numericUpDown1.Value));




            textBox1.Text = $"{Var_Binary_value}";

            
        }

        private void textBox2_TextChanged(object sender, EventArgs e) {
            string answer;
            string result;
            
            int num = Convert.ToInt32(answer);
            result = "";
            while (num > 1) {
                int remainder = num % 2;
                result = Convert.ToString(remainder) + result;
                num /= 2;
            }
            result = Convert.ToString(num) + result;
            textBox1.Text = $"{result}";
        }
    }
}
