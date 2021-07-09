using BmrsDataAcquisition.Models;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace BmrsDataAcquisition.Business_Logic
{
    /// <summary>
    /// Class provides support for serialisation/deserialisation of BMRS data.
    /// </summary>

    public class DataSerialiser
    {
        /// <summary>
        /// Returns BMRS data as uploadable JSON, given the original string.
        /// </summary>
        /// <param name="bmrsData">String containing the original response from the BMRS API webcall.</param>
        /// <returns>A list of data objects in JSON format.</returns>
        public List<B1620DataModel> ReturnDataAsJSON(string bmrsData)
        {
            // Create empty list of data models
            List<B1620DataModel> b1620List = new List<B1620DataModel>();

            // Create intermediate list of input strings?
            string[] lineSeparators = new string[] { "\n" };
            string[] linesArray;

            linesArray = bmrsData.Split(lineSeparators, StringSplitOptions.None);
            List<string> linesList = linesArray.ToList<string>();

            // Remove unwanted info
            for (int i = 0; i < linesList.Count; i++)
            {
                string line = linesList[i];

                if (line.Contains("*"))
                {
                    linesList.RemoveAt(i);
                }

                if (line.Contains("<EOF>"))
                {
                    linesList.RemoveAt(i);
                }
            }

            List<string> resultsList = new List<string>();

            foreach (var line in linesList)
            {
                resultsList.Add(line.Trim());
            }

            // Iterate over each line in input string
            foreach (var line in resultsList)
            {
                try
                {
                    if (!line.Contains("*"))
                    {
                        // Create a string array based on the line
                        string[] lineSeparator = new string[] { "," };
                        string[] lineArray;

                        lineArray = line.Split(lineSeparator, StringSplitOptions.None);

                        // Create JSON object
                        B1620DataModel dataElement = new B1620DataModel
                        {
                            DocType = lineArray[0],
                            BusType = lineArray[1],
                            ProType = lineArray[2],
                            TimeId = lineArray[3],
                            Quantity = lineArray[4],
                            CurveType = lineArray[5],
                            Resolution = lineArray[6],
                            SetDate = lineArray[7],
                            SetPeriod = lineArray[8],
                            PowType = lineArray[9],
                            ActFlag = lineArray[10],
                            DocId = lineArray[11],
                            DocRevNum = lineArray[12]
                        };

                        // Clean raw data
                        string powerType = lineArray[9];
                        powerType = powerType.Replace("\"", "");

                        string period = lineArray[8].ToString();
                        if (period.Length == 1)
                        {
                            period = "0" + period;
                        }

                        // Set Id parameter
                        dataElement.Id = lineArray[7] + "-P" + period + "-" + powerType;

                        // Add to list of data models
                        b1620List.Add(dataElement);
                    }
                }
                catch (Exception ex)
                {
                    Debug.WriteLine("\nException Caught trying to create JSON!");
                    Debug.WriteLine("Message :{0} ", ex.Message);
                }
            }

            return b1620List;
        }
    }
}
