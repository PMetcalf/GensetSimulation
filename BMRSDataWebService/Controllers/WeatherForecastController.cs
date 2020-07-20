using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace BMRSDataWebService.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class WeatherForecastController : ControllerBase
    {
        private static readonly string[] Summaries = new[]
        {
            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        };

        private readonly ILogger<WeatherForecastController> _logger;

        public WeatherForecastController(ILogger<WeatherForecastController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public async Task<IEnumerable<WeatherForecast>> GetAsync()
        {
            var rng = new Random();

            await getBMRSDataAsync();

            return Enumerable.Range(1, 5).Select(index => new WeatherForecast
            {
                Date = DateTime.Now.AddDays(index),
                TemperatureC = rng.Next(-20, 55),
                Summary = Summaries[rng.Next(Summaries.Length)]
            })
            .ToArray();
        }

        public static async Task getBMRSDataAsync()
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
