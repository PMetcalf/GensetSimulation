using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Hosting;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;

namespace BMRSDataWebService
{
    public class Program
    {
        public static void Main(string[] args)
        {
            CreateHostBuilder(args).Build().Run();

            //await getBMRSData();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureWebHostDefaults(webBuilder =>
                {
                    webBuilder.UseStartup<Startup>();
                });

        /// <summary>
        /// Routine makes async call to BMRS web service using HTTP Client.
        /// </summary>
        /// <returns></returns>
        public static async Task getBMRSData()
        {
            using var client = new HttpClient();

            // Setup http client
            client.BaseAddress = new Uri("https://api.bmreports.com/BMRS/B1630/V1?");

            // Call BMRS API
            var response = await client.GetAsync("APIKey=ittvxvqico9tta1&SettlementDate=2020-06-25&Period=1&ServiceType=csv");

            // Parse response
            if (response.IsSuccessStatusCode)
            {
                string message = await response.Content.ReadAsStringAsync();
            }
        }
    }
}
