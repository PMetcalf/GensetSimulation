﻿

using Microsoft.Azure.Cosmos;

namespace SimulationWebservice.Services
{
    /// <summary>
    /// Connect and use Azure Cosmos DB, including CRUD operations.
    /// </summary>

    public class CosmosDBService : ICosmosDbService
    {
        private Container container;

        /// <summary>
        /// Use client to connect place database connection in container.
        /// </summary>
        /// <param name="dbClient"></param>
        /// <param name="dbName"></param>
        /// <param name="containerName"></param>
        public CosmosDBService(CosmosClient dbClient, string dbName, string containerName)
        {
            this.container = dbClient.GetContainer(dbName, containerName);
        }
    }
}
