using GensetSimulator.Models;
using System;

namespace GensetSimulator
{
    class Program
    {
        /// <summary>
        /// This is the main executable class for the program.
        /// </summary>
        /// <param name="args"></param>

        static void Main(string[] args)
        {
            Console.WriteLine("Starting Genset Simulator.");

            // Initialise new genset.
            Genset genset = new Genset();

            // [Initialise webservice connection].

            // Start genset / data logging.

            // Run genset / data logging.

            // End genset run / data logging (on interuption, or after time period?).

            // Clean up resources.
        }
    }
}
