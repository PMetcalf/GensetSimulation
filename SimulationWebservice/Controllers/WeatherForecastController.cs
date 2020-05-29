using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using SimulationWebservice.Models;
using SimulationWebservice.Services;

namespace SimulationWebservice.Controllers
{
    [ApiController]
    [Route("[controller]")]
    //[Route("api/[controller]")]
    public class WeatherForecastController : ControllerBase
    {
        private static readonly string[] Summaries = new[]
        {
            "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
        };

        private readonly ICosmosDbService _cosmosDbService;

        private readonly ILogger<WeatherForecastController> _logger;

        public WeatherForecastController(ILogger<WeatherForecastController> logger, ICosmosDbService cosmosDbService)
        {
            _logger = logger;

            _cosmosDbService = cosmosDbService;
        }

        [HttpGet]
        public IEnumerable<WeatherForecast> Get()
        {
            var rng = new Random();
            return Enumerable.Range(1, 5).Select(index => new WeatherForecast
            {
                Date = DateTime.Now.AddDays(index),
                TemperatureC = rng.Next(-20, 55),
                Summary = Summaries[rng.Next(Summaries.Length)]
            })
            .ToArray();
        }

        [HttpPost]
        public async Task<ActionResult> CreateDataEntryAsync(GensetData gensetData)
        {
            try
            {
                await _cosmosDbService.AddDataAsync(gensetData);
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex);
            }

            // return result.
            return CreatedAtAction("Genset Data POST", new { id = gensetData.Id }, gensetData);
        }
    }
}
