namespace Encoder_Calc
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing) {
            if (disposing && (components != null)) {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent() {
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.numericUpDownPulsePerDistance = new System.Windows.Forms.NumericUpDown();
            this.numericUpDownDistanceMeter = new System.Windows.Forms.NumericUpDown();
            this.textBoxPulsePerInch = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.numericUpDownPrintedResolution = new System.Windows.Forms.NumericUpDown();
            this.label5 = new System.Windows.Forms.Label();
            this.textBoxPulsePerPrintStroke = new System.Windows.Forms.TextBox();
            this.label6 = new System.Windows.Forms.Label();
            this.label7 = new System.Windows.Forms.Label();
            this.textBoxDivider = new System.Windows.Forms.TextBox();
            this.numericUpDownMultiplier = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownPulsePerDistance)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownDistanceMeter)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownPrintedResolution)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownMultiplier)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(44, 36);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(102, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Pulses Per Distance";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(44, 58);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(95, 13);
            this.label2.TabIndex = 1;
            this.label2.Text = "Distance in Meters";
            // 
            // numericUpDownPulsePerDistance
            // 
            this.numericUpDownPulsePerDistance.Increment = new decimal(new int[] {
            50,
            0,
            0,
            0});
            this.numericUpDownPulsePerDistance.Location = new System.Drawing.Point(165, 29);
            this.numericUpDownPulsePerDistance.Maximum = new decimal(new int[] {
            100000000,
            0,
            0,
            0});
            this.numericUpDownPulsePerDistance.Name = "numericUpDownPulsePerDistance";
            this.numericUpDownPulsePerDistance.Size = new System.Drawing.Size(103, 20);
            this.numericUpDownPulsePerDistance.TabIndex = 2;
            // 
            // numericUpDownDistanceMeter
            // 
            this.numericUpDownDistanceMeter.Location = new System.Drawing.Point(165, 51);
            this.numericUpDownDistanceMeter.Maximum = new decimal(new int[] {
            100000000,
            0,
            0,
            0});
            this.numericUpDownDistanceMeter.Name = "numericUpDownDistanceMeter";
            this.numericUpDownDistanceMeter.Size = new System.Drawing.Size(103, 20);
            this.numericUpDownDistanceMeter.TabIndex = 3;
            // 
            // textBoxPulsePerInch
            // 
            this.textBoxPulsePerInch.Location = new System.Drawing.Point(165, 91);
            this.textBoxPulsePerInch.Name = "textBoxPulsePerInch";
            this.textBoxPulsePerInch.Size = new System.Drawing.Size(103, 20);
            this.textBoxPulsePerInch.TabIndex = 4;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(44, 98);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(76, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Pulse Per Inch";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(44, 142);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(93, 13);
            this.label4.TabIndex = 6;
            this.label4.Text = "Printed Resolution";
            // 
            // numericUpDownPrintedResolution
            // 
            this.numericUpDownPrintedResolution.Location = new System.Drawing.Point(165, 135);
            this.numericUpDownPrintedResolution.Name = "numericUpDownPrintedResolution";
            this.numericUpDownPrintedResolution.Size = new System.Drawing.Size(103, 20);
            this.numericUpDownPrintedResolution.TabIndex = 7;
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(44, 187);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(106, 13);
            this.label5.TabIndex = 8;
            this.label5.Text = "Pulse per print stroke";
            // 
            // textBoxPulsePerPrintStroke
            // 
            this.textBoxPulsePerPrintStroke.Location = new System.Drawing.Point(165, 187);
            this.textBoxPulsePerPrintStroke.Name = "textBoxPulsePerPrintStroke";
            this.textBoxPulsePerPrintStroke.Size = new System.Drawing.Size(103, 20);
            this.textBoxPulsePerPrintStroke.TabIndex = 9;
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(44, 247);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(48, 13);
            this.label6.TabIndex = 10;
            this.label6.Text = "Multiplier";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(162, 247);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(40, 13);
            this.label7.TabIndex = 11;
            this.label7.Text = "Divider";
            // 
            // textBoxDivider
            // 
            this.textBoxDivider.Location = new System.Drawing.Point(165, 274);
            this.textBoxDivider.Name = "textBoxDivider";
            this.textBoxDivider.Size = new System.Drawing.Size(103, 20);
            this.textBoxDivider.TabIndex = 13;
            // 
            // numericUpDownMultiplier
            // 
            this.numericUpDownMultiplier.Location = new System.Drawing.Point(43, 275);
            this.numericUpDownMultiplier.Name = "numericUpDownMultiplier";
            this.numericUpDownMultiplier.Size = new System.Drawing.Size(103, 20);
            this.numericUpDownMultiplier.TabIndex = 14;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(316, 602);
            this.Controls.Add(this.numericUpDownMultiplier);
            this.Controls.Add(this.textBoxDivider);
            this.Controls.Add(this.label7);
            this.Controls.Add(this.label6);
            this.Controls.Add(this.textBoxPulsePerPrintStroke);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.numericUpDownPrintedResolution);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.textBoxPulsePerInch);
            this.Controls.Add(this.numericUpDownDistanceMeter);
            this.Controls.Add(this.numericUpDownPulsePerDistance);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownPulsePerDistance)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownDistanceMeter)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownPrintedResolution)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownMultiplier)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.NumericUpDown numericUpDownPulsePerDistance;
        private System.Windows.Forms.NumericUpDown numericUpDownDistanceMeter;
        private System.Windows.Forms.TextBox textBoxPulsePerInch;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.NumericUpDown numericUpDownPrintedResolution;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox textBoxPulsePerPrintStroke;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox textBoxDivider;
        private System.Windows.Forms.NumericUpDown numericUpDownMultiplier;
    }
}

