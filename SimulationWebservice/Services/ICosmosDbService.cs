using SimulationWebservice.Models;
using System.Threading.Tasks;

namespace SimulationWebservice.Services
{
    /// <summary>
    /// Provides an interface for Cosmos DB services.
    /// </summary>

    public interface ICosmosDbService
    {
        Task AddDataAsync(GensetData data);

        Task<GensetData> GetDataAsync(string id);
    }
}
