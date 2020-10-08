using Microsoft.Azure.Cosmos;
using DataStoreController.Models;
using System.Threading.Tasks;

namespace DataStoreController.Services
{
    /// <summary>
    /// Connect and use Azure Cosmos DB, including CRUD operations.
    /// </summary>

    public class CosmosDBService : ICosmosDbService
    {
        private Container container;

        /// <summary>
        /// Use client to connect database connection in container.
        /// </summary>
        /// <param name="dbClient"></param>
        /// <param name="dbName"></param>
        /// <param name="containerName"></param>
        public CosmosDBService(CosmosClient dbClient, string dbName, string containerName)
        {
            this.container = dbClient.GetContainer(dbName, containerName);
        }

        /// <summary>
        /// Add data item to container.
        /// </summary>
        /// <returns></returns>
        public async Task AddDataAsync(B1620_data_model data)
        {
            await this.container.CreateItemAsync<B1620_data_model>(data, new PartitionKey(data.Id));
        }

        /// <summary>
        /// Retreives data item from container.
        /// </summary>
        /// <returns></returns>
        public async Task<B1620_data_model> GetDataAsync(string id)
        {
            try
            {
                ItemResponse<B1620_data_model> response = await this.container.ReadItemAsync<B1620_data_model>(id, new PartitionKey(id));

                return response.Resource;
            }
            catch
            {
                return null;
            }
        }
    }
}
