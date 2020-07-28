using E_GridDataShunter.Models;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

namespace E_GridDataShunter
{
    class Program
    {
        // Http client used for collecting and sending data.
        static HttpClient client = new HttpClient();

        static async Task Main(string[] args)
        {
            Console.WriteLine("Data Collection Started ...");

            // Request data.
            string returnedData = await GetBMRSDataAsync();

            Console.WriteLine(returnedData);

            // Process data into JSON.

            // Send data to database.
        }

        /// <summary>
        /// Retrieves data from BMRS service using http Get.
        /// </summary>
        static async Task<string> GetBMRSDataAsync()
        {
            try
            {
                // Get request string
                string request_string = "https://api.bmreports.com/BMRS/B1620/V1?APIKey=ittvxvqico9tta1&SettlementDate=2020-06-25&Period=10&ServiceType=csv";

                HttpResponseMessage response = await client.GetAsync(request_string);

                response.EnsureSuccessStatusCode();

                // Create response body
                string responseBody = await response.Content.ReadAsStringAsync();

                return responseBody;
            }
            catch (Exception ex)
            {
                Console.WriteLine("\nException Caught!");
                Console.WriteLine("Message :{0} ", ex.Message);

                return ex.Message.ToString();
            }
        }

        /// <summary>
        /// Converts bmrs csv data into list of JSON data elements.
        /// </summary>
        /// <param name="bmrsData"></param>
        /// <returns></returns>
        static List<B1620_data_model> ReturnDataAsJSON(string bmrsData)
        {
            // Create empty list of data models

            // Remove first line from input string

            // Iterate over each line in input string

                // Create JSON object

                // Set Id parameter

                // Add to list of data models

            // Return data model
        }
    }
}
