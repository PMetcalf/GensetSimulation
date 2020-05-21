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
            Console.Title = typeof(Program).Name;

            // Initialise webservice.

            Run();
        }


        static void Run()
        {
            // Initialise genset.
            Genset genset = new Genset();

            while (true)
            {
                var consoleInput = ReadFromConsole();
                if (string.IsNullOrWhiteSpace(consoleInput)) continue;

                try
                {
                    genset.StartGenset(5);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
            }
        }

        const string _readPrompt = "Type to Start:";

        public static string ReadFromConsole()
        {
            // Show a prompt, and get input:
            Console.Write(_readPrompt);
            return Console.ReadLine();
        }
    }
}