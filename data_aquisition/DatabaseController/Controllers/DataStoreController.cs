using DatabaseController.Services;
using DatabaseController.Models;
using Microsoft.AspNetCore.Mvc;
using System;
using System.Diagnostics;
using System.Threading.Tasks;

namespace DatabaseController.Controllers
{
    //[Route("api/[controller]")]
    [ApiController]
    [Route("[controller]")]
    public class DataStoreController : ControllerBase
    {
        private readonly ICosmosDbService cosmosDbService;

        public DataStoreController(ICosmosDbService dbService)
        {
            cosmosDbService = dbService;
        }

        /// <summary>
        /// Default Http Get - Provides simple feedback message
        /// </summary>
        /// <returns></returns>
        public string Get()
        {
            string feedbackMessage = "Webservice Active.";

            return feedbackMessage;
        }

        /// <summary>
        /// Http GET method, returning one dataset by ID.
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpGet("{id}", Name = "Get")]
        [ActionName("GetAsync")]    // Attribute naming overcomes bug in aspnet core 3.1
        public async Task<ActionResult<B1620_data_model>> GetDataAsync(string id)
        {
            // Retrieve data asynchronously via database service
            B1620_data_model data = await cosmosDbService.GetDataAsync(id);

            // Handle missing data
            if (data == null)
            {
                return NotFound();
            }

            // Return result
            else
            {
                return data;
            }
        }

        /// <summary>
        /// Http GET method, returning earliest dataset by passing SQL query.
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpGet("Earliest", Name = "Get")]
        [ActionName("GetAsync")]    // Attribute naming overcomes bug in aspnet core 3.1
        public async Task<ActionResult<B1620_data_model>> GetEarliestDataEntryAsync()
        {
            // Construct SQL query

            // Retrieve data asynchronously via database service
            B1620_data_model data = await cosmosDbService.GetEarliestDataEntryAsync();

            // Handle missing data
            if (data == null)
            {
                return NotFound();
            }

            // Return result
            else
            {
                return data;
            }
        }

        /// <summary>
        /// Http Post method, adding data to database
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        [HttpPost]
        public async Task<ActionResult<B1620_data_model>> PostDataEntryAsync(B1620_data_model data)
        {
            // Post data to database
            try
            {
                await cosmosDbService.AddDataAsync(data);
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex);

                if (ex.Message.Contains("409"))
                {
                    // Is OK if data is already in database
                    return Conflict(new { id = data.Id });
                }
            }

            // Return result
            return CreatedAtAction("Get", new { id = data.Id }, data);
        }
    }
}
