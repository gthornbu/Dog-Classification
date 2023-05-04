using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Dog_Classification
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public void runPython()
        {
            string fileName = @"script.py";
            string pythonPath = txtPath.Text;
            if (pythonPath == "Graham's path")
            {
                pythonPath = @"C:\ProgramData\Anaconda3\envs\tensorflow_gpuenv\python.exe";
            }
            Process p = new Process();
            p.StartInfo = new ProcessStartInfo(pythonPath, fileName)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            p.Start();

            string output = p.StandardOutput.ReadToEnd();
            p.WaitForExit();
            MessageBox.Show(output);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            runPython();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog1 = new OpenFileDialog();

            openFileDialog1.Filter = "Image Files (*.jpg, *.jpeg, *.png, *.bmp)|*.jpg;*.jpeg;*.png;*.bmp";

            openFileDialog1.InitialDirectory = Environment.GetFolderPath(Environment.SpecialFolder.MyPictures);

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                string imagePath = openFileDialog1.FileName;

                string savePath = @"image.jpg";

                using (FileStream fileStream = new FileStream(savePath, FileMode.Create))
                {
                    using (BinaryWriter binaryWriter = new BinaryWriter(fileStream))
                    {
                        byte[] imageBytes = File.ReadAllBytes(imagePath);
                        binaryWriter.Write(imageBytes);
                    }
                }
                pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                pictureBox1.Image = Image.FromFile(imagePath);

            }
        }
    }
}
