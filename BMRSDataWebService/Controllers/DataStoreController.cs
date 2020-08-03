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
        /// Http GET returning one dataset by ID.
        /// </summary>
        /// <param name="id"></param>
        /// <returns></returns>
        [HttpGet]
        public async Task<ActionResult<B1620_data_model>> GetDataAsync(string id)
        {
            // Retrieve data asynchronously via database service

            // Handle missing data

            // Return result
        }
    }
}
