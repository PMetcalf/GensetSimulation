using System;
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
            await GetBMRSData();

            // Process data?

            // Send data to database.
        }

        /// <summary>
        /// Retrieves data from BMRS service using http Get.
        /// </summary>
        static async Task GetBMRSData()
        {
            try
            {
                // Get request string
                string request_string = "https://api.bmreports.com/BMRS/B1630/V1?APIKey=ittvxvqico9tta1&SettlementDate=2020-06-25&Period=1&ServiceType=csv";

                HttpResponseMessage response = await client.GetAsync(request_string);

                response.EnsureSuccessStatusCode();

                // Create response body
                string responseBody = await response.Content.ReadAsStringAsync();

                Console.WriteLine(responseBody);
            }
            catch (Exception ex)
            {
                Console.WriteLine("\nException Caught!");
                Console.WriteLine("Message :{0} ", ex.Message);
            }
        }
    }
}
