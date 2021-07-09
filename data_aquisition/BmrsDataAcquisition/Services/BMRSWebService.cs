using System;
using System.Diagnostics;
using System.Net.Http;
using System.Threading.Tasks;

namespace BmrsDataAcquisition.Services
{
    public class BMRSWebService
    {
        // Http client is used for BMRS API interactions
        static HttpClient bmrsClient = new HttpClient();

        /// <summary>
        /// Tries to return data from the BMRS API for the prescribed date.
        /// </summary>
        /// <param name="date">The date associated with the data request.</param>
        /// <param name="period">The period associated with the data request.</param>
        /// <returns>The body of the response, or an error message.</returns>
        public async Task<string> GetBMRSDataAsync(DateTime date, int period)
        {
            // Create Uri for request
            Uri bmrsUri = BuildBMRSDataUri(date, period);

            try
            {
                // Try to call API
                HttpResponseMessage response = await bmrsClient.GetAsync(bmrsUri);

                response.EnsureSuccessStatusCode();

                // Create and return response body
                string responseBody = await response.Content.ReadAsStringAsync();

                return responseBody;
            }
            catch (Exception ex)
            {
                Debug.WriteLine("\nException Caught!");
                Debug.WriteLine("Message :{0} ", ex.Message);

                return ex.Message.ToString();
            }
        }

        /// <summary>
        /// Builds BMRS GET Uri with specified date and period.
        /// </summary>
        /// <param name="date">The date associated with the data request.</param>
        /// <param name="period">The period associated with the data request.</param>
        /// <returns>A customised Uri for the prescribed date and time period.</returns>
        private Uri BuildBMRSDataUri(DateTime date, int period)
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
    }
}
