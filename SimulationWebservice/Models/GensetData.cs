using Newtonsoft.Json;

namespace SimulationWebservice.Models
{
    /// <summary>
    /// Contains data model for genset system.
    /// </summary>

    public class GensetData
    {
        // Id is used to identify data element in storage.
        [JsonProperty(PropertyName = "id")]
        public string Id { get; set; }

        //
    }
}
