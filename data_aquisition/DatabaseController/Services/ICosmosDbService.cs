﻿using DatabaseController.Models;
using System.Threading.Tasks;

namespace DatabaseController.Services
{
    /// <summary>
    /// Provides an interface for Cosmos DB services.
    /// </summary>

    public interface ICosmosDbService
    {
        Task AddDataAsync(B1620_data_model data);

        Task<B1620_data_model> GetDataAsync(string id);
    }
}
