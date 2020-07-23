using System;
using System.Net.Http;

namespace E_GridDataShunter
{
    class Program
    {
        // Separate http clients used to (1) collect data and (2) send data to storage.
        static HttpClient clientBMRSData = new HttpClient();
        static HttpClient clientDataStore = new HttpClient();

        static void Main(string[] args)
        {
            Console.WriteLine("Data Collection Started ...");

            // Initialise http client.
            InitialiseClientBMRSData();

            // Request data.

            // Process data?

            // Send data to database.
        }

        /// <summary>
        /// Initialises http client instance for BMRS interaction.
        /// </summary>
        static void InitialiseClientBMRSData()
        {
            clientBMRSData.BaseAddress = new Uri("https://api.bmreports.com/BMRS/");

            // [TASK] Investigate if should include API key.
            clientBMRSData.DefaultRequestHeaders.Accept.Clear();
        }
    }
}
