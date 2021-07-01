using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

namespace BmrsDataAcquisition.Services
{
    public class AzureWebService
    {
        // Http is used for database interactions
        static HttpClient azureHttpClient = new HttpClient();

        // Webservice initialisation routine (if needed)

        /// <summary>
        /// Points http client to database webservice (for data POST / GET)
        /// </summary>
        public void InitialiseAzureHttpClient()
        {
            // Set base address
            azureHttpClient.BaseAddress = new Uri("https://localhost:5001/");

            // Clear default headers
            azureHttpClient.DefaultRequestHeaders.Accept.Clear();

            // Add default headers for database interaction
            azureHttpClient.DefaultRequestHeaders.Accept.Add(
                new System.Net.Http.Headers.MediaTypeWithQualityHeaderValue("application/json"));
        }

        /// <summary>
        /// Retrieves earliest data entry in database via http GET
        /// </summary>
        /// <param ></param>
        /// <returns>EarliestDate (Tuple(Int, DateTime))</returns>
        public async Task<Tuple<int, DateTime>> ReturnEarliestDate()
        {
            // Retrieve earliest data entry
            HttpResponseMessage earliestData = await RetrieveEarliestDataEntryAsync();

            // Parse response into dictionary
            string dataAsJSON = earliestData.Content.ReadAsStringAsync().Result;
            
            // Return data as tuple
        }

        /// <summary>
        /// Retrieves earliest data entry in database via http GET
        /// </summary>
        /// <param ></param>
        /// <returns>response (HttpResponseMessage)</returns>
        private async Task<HttpResponseMessage> RetrieveEarliestDataEntryAsync()
        {
            HttpResponseMessage response = await azureHttpClient.GetAsync("datastore/");

            return response;
        }

        /// <summary>
        /// Converts response token into dictionary
        /// </summary>
        /// <param >response (HttpResponseMessage)</param>
        /// <returns>responseDictionary (Dictionary<string, string></string>))</returns>
        private Dictionary<string, string> ReturnResponseAsDictionary(HttpResponseMessage response)
        {
            // Retrieve content from response
            string dataAsJSON = response.Content.ReadAsStringAsync().Result;

            // Parse content into dictionary
            Dictionary<string, string> responseDictionary = JsonConvert.DeserializeObject<Dictionary<string, string>>(dataAsJSON);

            // Return dictionary
            return responseDictionary;
        }
    }
}       
