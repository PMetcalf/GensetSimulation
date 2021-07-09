using BmrsDataAcquisition.Services;
using Microsoft.Extensions.Hosting;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

namespace BmrsDataAcquisition.Business_Logic
{
    public class bmrsWebCallHostedService : IHostedService
    {
        private Timer _timer;

        private AzureWebService azureWebService = new AzureWebService();

        private BMRSWebService bmrsWebService = new BMRSWebService();

        public Task StartAsync(CancellationToken cancellationToken)
        {
            // Start webservices
            azureWebService.InitialiseAzureHttpClient();

            _timer = new Timer(BmrsWebCallAsync, null, 0, 86400000
                );   // 86400000 Interval specified in milliseconds (24 hrs)
            return Task.CompletedTask;
        }

        // This is the routine called by the timer
        async void BmrsWebCallAsync(object state)
        {
            Debug.WriteLine("Making webcall ...");

            // Determine earliest entry in storage
            Tuple<string, string> result = await azureWebService.ReturnEarliestDate();
            
            Debug.WriteLine(("Earliest Date:", result));

            // Calculate date to request data for
            DateTime earliestDate = DateTime.Parse(result.Item2);
            DateTime requestDate = earliestDate.AddDays(-1);

            // Iterate over periods for date
            for (int period = 1; period < 51; period ++)
            {
                Debug.WriteLine("Making BMRS Call ...");

                // Request data from BMRS API
                string response = await bmrsWebService.GetBMRSDataAsync(requestDate, period);

                Debug.WriteLine(response);

                // Convert data to storage format

                // Send converted data to storage
            }
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            //New Timer does not have a stop. 
            _timer?.Change(Timeout.Infinite, 0);
            return Task.CompletedTask;
        }
    }
}
