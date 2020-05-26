using Newtonsoft.Json;

namespace SimulationWebservice.Models
{
    /// <summary>
    /// Contains data model for genset system.
    /// </summary>

    public class GensetData
    {
        /// <summary>
        /// Id is used to identify data storage element.
        /// </summary>
        [JsonProperty(PropertyName = "id")]
        public string Id { get; set; }

        /// <summary>
        /// IsOn identifies if genset is running.
        /// </summary>
        [JsonProperty(PropertyName = "isOn")]
        public bool IsOn { get; set; }

        /// <summary>
        /// GensetPower describes output power in kWe.
        /// </summary>
        [JsonProperty(PropertyName = "gensetPower")]
        public int GensetPower { get; set; }
    }
}
