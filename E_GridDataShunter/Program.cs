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
            Console.WriteLine("Hello World!");

            // Initialise http client.

            // Request data.

            // Process data?

            // Send data to database.
        }

        ///
    }
}
