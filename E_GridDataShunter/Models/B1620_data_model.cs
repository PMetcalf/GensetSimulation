using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Diagnostics.Contracts;
using System.Text;

namespace E_GridDataShunter.Models
{
    /// <summary>
    /// Data model representation (JSON focus) for BMRS B1620 report data.
    /// </summary>

    public class B1620_data_model
    {
        [JsonProperty(PropertyName = "id")]
        public string Id { get; set; }

        [JsonProperty(PropertyName = "docType")]
        public string DocType { get; set; }

        [JsonProperty(PropertyName = "busType")]
        public string BusType { get; set; }

        [JsonProperty(PropertyName = "proType")]
        public string ProType { get; set; }

        [JsonProperty(PropertyName = "timeId")]
        public string TimeId { get; set; }

        [JsonProperty(PropertyName = "quantity")]
        public string Quantity { get; set; }

        [JsonProperty(PropertyName = "curveType")]
        public string CurveType { get; set; }

        [JsonProperty(PropertyName = "resolution")]
        public string Resolution { get; set; }

        [JsonProperty(PropertyName = "setDate")]
        public string SetDate { get; set; }

        [JsonProperty(PropertyName = "setPeriod")]
        public string setPeriod { get; set; }

        [JsonProperty(PropertyName = "powType")]
        public string PowType { get; set; }

        [JsonProperty(PropertyName = "actFlag")]
        public string ActFlag { get; set; }

        [JsonProperty(PropertyName = "docId")]
        public string DocId { get; set; }

        [JsonProperty(PropertyName = "docRevNum")]
        public string DocRevNum { get; set; }
    }
}
