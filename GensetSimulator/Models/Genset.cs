using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Text;
using System.Threading.Tasks;

namespace GensetSimulator.Models
{
    /// <summary>
    /// Genset class holds properties and methods for a genset.
    /// </summary>

    class Genset
    {
        /// <summary>
        /// Identifies genset serial number.
        /// </summary>
        private string s_N;
        public string S_N { get => s_N; set => s_N = value; }

        /// <summary>
        /// Bool determines if genset is running.
        /// </summary>
        private bool isOn;
        public bool IsOn { get => isOn; set => isOn = value; }

        /// <summary>
        /// Property stores genset generated power.
        /// </summary>
        private int gensetPower;
        public int GensetPower { get => gensetPower; set => gensetPower = value; }

        /// <summary>
        /// Describes fuel mass flow rate in kg/s.
        /// </summary>
        private int fuelFlow_kgs;
        public int FuelFlow_kgs { get => fuelFlow_kgs; set => fuelFlow_kgs = value; }

        /// <summary>
        /// Describes shaft speed in rpm.
        /// </summary>
        private int shaftSpeed_rpm;
        public int ShaftSpeed_rpm { get => shaftSpeed_rpm; set => shaftSpeed_rpm = value; }

        /// <summary>
        /// Describes compressor outlet pressure in Bar.
        /// </summary>
        private int compPres_Bar;
        public int CompPres_Bar { get => compPres_Bar; set => compPres_Bar = value; }

        /// <summary>
        /// Describes turbine temp in deg C.
        /// </summary>
        private int turbineTemp_C;
        public int TurbineTemp_C { get => turbineTemp_C; set => turbineTemp_C = value; }

        /// <summary>
        /// Constructor alerts user and sets properties.
        /// </summary>
        public Genset()
        {
            Console.WriteLine("Genset Created.");

            // Initialise genset properties.
            IsOn = false;
            GensetPower = 0;
        }


        /// <summary>
        /// Prepares genset to run.
        /// </summary>
        public void StartGenset()
        {
            IsOn = true;
            Console.WriteLine("Starting Genset.");
        }

        /// <summary>
        /// Generates random values for properties for a pescribed count.
        /// </summary>
        public Genset RunGenset(Genset genset)
        {
            // Set running state.
            genset.IsOn = true;

            // Set S/N.
            genset.S_N = "Gen_001";

            // Generate values for properties.
            genset.GensetPower = GenerateRandomNumber(990, 1010);
            genset.FuelFlow_kgs = GenerateRandomNumber(20, 30);
            genset.ShaftSpeed_rpm = GenerateRandomNumber(30000, 32000);
            genset.CompPres_Bar = GenerateRandomNumber(30, 38);
            genset.TurbineTemp_C = GenerateRandomNumber(950, 1050);

            // Print values (Replace with data export).
            Console.WriteLine("Power Output: " + genset.gensetPower.ToString() + "kW");

            // Wait (simulated) time.
            Task.Delay(2000).Wait();

            // Return genset.
            return genset;
        }

        /// <summary>
        /// Stops generator.
        /// </summary>
        public void StopGenset()
        {
            IsOn = false;
            Console.WriteLine("Stopping Genset.");
        }

        /// <summary>
        /// Generates random number of value greater than min / less than max.
        /// </summary>
        /// <param name="min"></param>
        /// <param name="max"></param>
        private int GenerateRandomNumber(int min, int max)
        {
            if (min < 0)
            {
                min = 0;
            }

            if (max < 0)
            {
                max = 0;
            }

            // Generate number.
            Random random = new Random();
            int number = random.Next(min, max);

            // Return number.
            return number;
        }
    }
}
