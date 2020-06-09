using Newtonsoft.Json;
using Newtonsoft.Json.Serialization;
using System;

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

        /// <summary>
        /// Describes fuel mass flow rate in kg/s.
        /// </summary>
        [JsonProperty(PropertyName = "fuelFlow_kgs")]
        public int FuelFlow_kgs { get; set; }

        /// <summary>
        /// Describes shaft speed in rpm.
        /// </summary>
        [JsonProperty(PropertyName = "shaftSpeed_rpm")]
        public int ShaftSpeed_rpm { get; set; }

        /// <summary>
        /// Describes compressor outlet pressure in Bar.
        /// </summary>
        [JsonProperty(PropertyName = "compPres_Bar")]
        public int CompPres_Bar { get; set; }

        /// <summary>
        /// Describes turbine temp in deg C.
        /// </summary>
        [JsonProperty(PropertyName = "turbineTemp_C")]
        public int TurbineTemp_C { get; set; }

        /// <summary>
        /// Generates data Id stamp based on genset S/N and datetime.
        /// </summary>
        /// <returns></returns>
        public string GenerateIdStamp()
        {
            string idStamp = null;

            string gensetSN = "Genset_SN_001";

            // Build date & time part of id stamp.
            string time = DateTime.Now.ToString("yyyy-MM-dd-HH:mm:ss");

            // Build dataset Id.
            idStamp = gensetSN + "_" + time;

            // Return Id.
            return idStamp;
        }
    }
}
