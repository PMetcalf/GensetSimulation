using Microsoft.Extensions.Hosting;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

namespace BmrsDataAcquisition.Business_Logic
{
    public class bmrsWebCallHostedService : IHostedService
    {
        private Timer _timer;

        public Task StartAsync(CancellationToken cancellationToken)
        {
            // Start webservices

            _timer = new Timer(BmrsWebCall, null, 0, 100000);   // Interval specified in milliseconds
            return Task.CompletedTask;
        }

        // This is the routine called by the timer
        void BmrsWebCall(object state)
        {
            Debug.WriteLine("Hello World!");
        }

        public Task StopAsync(CancellationToken cancellationToken)
        {
            //New Timer does not have a stop. 
            _timer?.Change(Timeout.Infinite, 0);
            return Task.CompletedTask;
        }
    }
}
