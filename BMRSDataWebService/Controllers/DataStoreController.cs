using BMRSDataWebService.Services;
using E_GridDataShunter.Models;
using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;

namespace BMRSDataWebService.Controllers
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
        /// Http Post method, adding data to database
        /// </summary>
        /// <param name="data"></param>
        /// <returns></returns>
        public async Task<ActionResult<B1620_data_model>> PostDataEntryAsync(B1620_data_model data)
        {

        }
    }
}
