using System;
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
        /// Retrieves earliest data entry in database via http 
        /// </summary>
        /// <param ></param>
        /// <returns></returns>
        public async Task<HttpResponseMessage> RetrieveEarliestDataEntryAsync()
        {
            HttpResponseMessage response = await azureHttpClient.GetAsync("datastore/");

            return response;
        }
    }
}
