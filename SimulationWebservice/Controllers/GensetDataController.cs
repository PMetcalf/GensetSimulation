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

        /// <summary>
        /// Default GET method - Will (upon implmentation) return database details.
        /// </summary>
        /// <returns></returns>
        [HttpGet]
        public string Get()
        {
            string feedbackMessage = "All-item GET method not yet implemented.";

            return feedbackMessage;
        }

        /// <summary>
        /// GET method for returning one dataset entry by id.
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpGet("{id}", Name = "Get")]
        [ActionName("GetAsync")]    // Attribute naming overcomes issue with aspnet core 3.1.  
        public async Task<ActionResult<GensetData>> GetAsync(string id)
        {
            // Retrieve data from database.
            GensetData data = await _cosmosDbService.GetDataAsync(id);

            if (data == null)
            {
                return NotFound();
            }
            
            // Return data.
            return data;
        }

        /// <summary>
        /// POST method implementation creating a database Dataset entry.
        /// </summary>
        /// <param name="gensetData"></param>
        /// <returns></returns>
        [HttpPost]
        public async Task<ActionResult<GensetData>> CreateDataEntryAsync(GensetData gensetData)
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
            return CreatedAtAction(nameof(GetAsync), new { id = gensetData.Id }, gensetData); 
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
