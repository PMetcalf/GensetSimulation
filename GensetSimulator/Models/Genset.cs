using System;
using System.Collections.Generic;
using System.Text;

namespace GensetSimulator.Models
{
    /// <summary>
    /// Genset class holds properties and methods for a genset.
    /// </summary>

    class Genset
    {
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
        /// Constructor alerts user and sets properties.
        /// </summary>
        public Genset()
        {
            Console.WriteLine("Genset Created.");

            // Initialise genset properties.
            IsOn = false;
            GensetPower = 0;
        }
    }
}
