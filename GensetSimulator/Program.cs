﻿using GensetSimulator.Models;
using SimulationWebservice.Models;
using System;
using System.Net.Http;
using System.Threading.Tasks;

namespace GensetSimulator
{
    class Program
    {
        static HttpClient client = new HttpClient();

        /// <summary>
        /// This is the main executable class for the program.
        /// </summary>
        /// <param name="args"></param>
        static void Main(string[] args)
        {
            Console.Title = typeof(Program).Name;

            // Initialise webservice.
            InitialiseHttpClientInstance();

            Run();
        }

        /// <summary>
        /// Initialises http client instance with URIs.
        /// </summary>
        static void InitialiseHttpClientInstance()
        {
            client.BaseAddress = new Uri("https://localhost:5001/");

            client.DefaultRequestHeaders.Accept.Clear();

            client.DefaultRequestHeaders.Accept.Add(
                new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));
        }

        static async Task<Uri> SendGensetData(GensetData gensetData)
        {
            HttpResponseMessage response = await client.PostAsJsonAsync("gensetdata/", gensetData);

            response.EnsureSuccessStatusCode();

            // Return uri of created resource.
            return response.Headers.Location;
        }

        /// <summary>
        /// Create genset, wait for user input then start.
        /// </summary>
        static void Run()
        {
            // Initialise genset.
            Genset genset = new Genset();

            while (true)
            {
                var consoleInput = ReadFromConsole();
                if (string.IsNullOrWhiteSpace(consoleInput)) continue;

                // Start genset.
                genset.StartGenset();
                Console.WriteLine("Press key to stop");

                // Connect to webservice.


                try
                {
                    while (!Console.KeyAvailable)
                    {
                        // Run genset.
                        genset = genset.RunGenset();

                        // Collect genset data.
                        GensetData data = new GensetData
                        {
                            IsOn = genset.IsOn,
                            GensetPower = genset.GensetPower
                        };

                        // Post genset data (generate Id).

                    }                
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.Message);
                }
                finally
                {
                    // Stop genset.
                    genset.StopGenset();
                }
            }
        }

        const string _readPrompt = "Type to Start:";

        /// <summary>
        /// Read and return console input.
        /// </summary>
        /// <returns>ConsoleMessage</returns>
        public static string ReadFromConsole()
        {
            // Show a prompt, and get input:
            Console.Write(_readPrompt);
            return Console.ReadLine();
        }
    }
}