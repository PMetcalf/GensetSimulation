using E_GridDataShunter.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;
using System.Xml;

namespace E_GridDataShunter
{
    class Program
    {
        // Http clients used for collecting and sending data.
        static HttpClient bmrsClient = new HttpClient();
        static HttpClient databaseClient = new HttpClient();

        static async Task Main(string[] args)
        {
            Console.WriteLine("Data Collection Started ...");

            // Point http client to database webservice
            InitialiseDatabaseClient();

            try
            {
                // Collect data from this date
                DateTime startDate = new DateTime(2020, 7, 1);

                // Iterate over one month from start date
                for (int day = 0; day < 32; day++)
                {
                    // Iterate date based on day
                    DateTime date = startDate.AddDays(day);

                    // Iterate over periods in day (50 periods)
                    for (int period = 1; period < 51; period++)
                    {
                        // Request data
                        string returnedData = await GetBMRSDataAsync(date, period);

                        Console.WriteLine("BMRS Response (Raw) ...");
                        Console.WriteLine(returnedData);

                        // If response contains data, serialise and send to cloud
                        if (returnedData.Contains("Success But No data available") == false)
                        {
                            Console.WriteLine("Serialising data ...");

                            // Process data into JSON objects
                            List<B1620_data_model> serialisedDataList = ReturnDataAsJSON(returnedData);

                            Console.WriteLine("Posting data elements to database ...");

                            // Send each JSON data object to database
                            foreach (var dataElement in serialisedDataList)
                            {
                                // Send to database
                                var statusCode = await SendDataToDatabaseAsync(dataElement);

                                // Report outcome
                                Console.WriteLine($"uploading {dataElement.Id} : StatusCode: {statusCode}");
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex);
            }
        }

        /// <summary>
        /// Retrieves data from BMRS service using http Get.
        /// </summary>
        static async Task<string> GetBMRSDataAsync(DateTime date, int period)
        {
            try
            {
                // Create uri
                Uri bmrsUri = BuildBMRSDataUri(date, period);
                
                HttpResponseMessage response = await bmrsClient.GetAsync(bmrsUri);

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
        /// Returns BMRS GET Uri with specified date and period.
        /// </summary>
        /// <param name="date"></param>
        /// <param name="period"></param>
        /// <returns></returns>
        static Uri BuildBMRSDataUri(DateTime date, int period)
        {
            UriBuilder uriBuilder = new UriBuilder();

            // Create the base
            uriBuilder.Scheme = "https";

            // Set default parameters
            uriBuilder.Host = "api.bmreports.com/BMRS/B1620";
            uriBuilder.Path = "V1";

            // Add date and time
            string uriDate = date.Date.ToString("yyyy-MM-dd");
            string uriPeriod = period.ToString();
            uriBuilder.Query = $"APIKey=ittvxvqico9tta1&SettlementDate={uriDate}&Period={uriPeriod}&ServiceType=csv";

            // return Uri
            Uri uri = uriBuilder.Uri;
            return uri;
        }

        /// <summary>
        /// Converts bmrs csv data into list of JSON data elements.
        /// </summary>
        /// <param name="bmrsData"></param>
        /// <returns></returns>
        static List<B1620_data_model> ReturnDataAsJSON(string bmrsData)
        {
            // Create empty list of data models
            List<B1620_data_model> b1620List = new List<B1620_data_model>();

            // Create intermediate list of input strings?
            string[] lineSeparators = new string[] { "\n" };
            string[] linesArray;

            linesArray = bmrsData.Split(lineSeparators, StringSplitOptions.None);
            List<string> linesList = linesArray.ToList<string>();

            // Remove unwanted info
            for (int i = 0; i < linesList.Count; i++)
            {
                string line = linesList[i];

                if (line.Contains("*"))
                {
                    linesList.RemoveAt(i);
                }

                if (line.Contains("<EOF>"))
                {
                    linesList.RemoveAt(i);
                }
            }

            List<string> resultsList = new List<string>();

            foreach (var line in linesList)
            {
                resultsList.Add(line.Trim());
            }

            // Iterate over each line in input string
            foreach (var line in resultsList)
            {
                try
                {
                    if (!line.Contains("*"))
                    {
                        // Create a string array based on the line
                        string[] lineSeparator = new string[] { "," };
                        string[] lineArray;

                        lineArray = line.Split(lineSeparator, StringSplitOptions.None);

                        // Create JSON object
                        B1620_data_model dataElement = new B1620_data_model
                        {
                            DocType = lineArray[0],
                            BusType = lineArray[1],
                            ProType = lineArray[2],
                            TimeId = lineArray[3],
                            Quantity = lineArray[4],
                            CurveType = lineArray[5],
                            Resolution = lineArray[6],
                            SetDate = lineArray[7],
                            SetPeriod = lineArray[8],
                            PowType = lineArray[9],
                            ActFlag = lineArray[10],
                            DocId = lineArray[11],
                            DocRevNum = lineArray[12]
                        };

                        // Clean raw data
                        string powerType = lineArray[9];
                        powerType = powerType.Replace("\"", "");

                        string period = lineArray[8].ToString();
                        if (period.Length == 1)
                        {
                            period = "0" + period;
                        }

                        // Set Id parameter
                        dataElement.Id = lineArray[7] + "-P" + period + "-" + powerType;

                        // Add to list of data models
                        b1620List.Add(dataElement);
                    }
                }
                catch (Exception ex)
                {
                    Console.WriteLine("\nException Caught trying to create JSON!");
                    Console.WriteLine("Message :{0} ", ex.Message);
                }
            }

            return b1620List;
        }

        /// <summary>
        /// Points http client to database webservice (for data POST / GET)
        /// </summary>
        static void InitialiseDatabaseClient()
        {
            // Set base address
            databaseClient.BaseAddress = new Uri("https://localhost:5001/");

            // Clear default headers
            databaseClient.DefaultRequestHeaders.Accept.Clear();

            // Add default headers for database interaction
            databaseClient.DefaultRequestHeaders.Accept.Add(
                new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));
        }

        /// <summary>
        /// Sends data in json format to database via http post 
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        static async Task<HttpStatusCode> SendDataToDatabaseAsync(B1620_data_model data)
        {
            HttpResponseMessage response = await databaseClient.PostAsJsonAsync("datastore/", data);

            // Return response status code
            return response.StatusCode;
        }
    }
}
