using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using SimulationWebservice.Models;
using SimulationWebservice.Services;

namespace SimulationWebservice.Controllers
{
    //[Route("api/[controller]")]
    [ApiController]
    [Route("[controller]")]
    public class GensetDataController : ControllerBase
    {
        private readonly ICosmosDbService _cosmosDbService;

        public GensetDataController(ICosmosDbService cosmosDbService)
        {
            _cosmosDbService = cosmosDbService;
        }

        // GET: api/GensetData
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET: api/GensetData/5
        [HttpGet("{id}", Name = "Get")]
        public string Get(int id)
        {
            return "value";
        }

        // POST: api/GensetData
        [HttpPost]
        public async Task<ActionResult> CreateDataEntryAsync(GensetData gensetData)
        {
            // Post data to database.
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

        // PUT: api/GensetData/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE: api/ApiWithActions/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
