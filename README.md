# UK Electricity Grid Analytics

This data acquisition and analysis project involves collecting, analysing and visualising electricity generation data from UK power networks via Elexon's BMRS web API.

Output data from a variety of different generation assets is collected and analysed to identify contributions from renewable and non-renewable sources, statistics for each generation type and characterisation of generation profiles. The UK energy grid mix contains a wide-ranging mix of generation types, from nuclear and fossil fuels through to fully renewable solutions such as solar, wind and hydro. 

Each of the different generation types produces different quantities of electricity for the UK market, and does so using different profiles. 

![Windfarm Electricity Generation](https://github.com/PMetcalf/uk-power-generation-project/blob/PF_201001/miscellaneous/windfarm1.jpg)

This project seeks to understand and characterise the generation of power from different assets using historic time-series generation data provided by Elexon, a company that compares how much electricity generators and suppliers say they will produce or consume with actual volumes in UK markets. 

Project Objectives
---

- Develop a capability to automatically acquire and store generation data from an API.
- Quantify overall contribution and statistical information for each generation class over adjustable time periods.
- Characterise the individual output profiles for each generation class.

Repository Structure
---

This is an end-to-end acquisition, storage, analysis and visualisation project with elements of the technology stack built for each function, and the project contains a dashboard displaying electricity generation data.

The project is divided into a series folders, each focused on a different element of the data pipeline:

- **Data Acquisition:** Acquisition script for requesting data for BMRS API, and database controller for data storage and retrieval with Azure Cosmos DB.
  
- **Data Analytics:** Jupyter notebooks and supporting source code for data exploration and analysis.

- **Web App:** Dashboard for displaying data trends and summary statistics.

Installation & Setup
---

The following packages are required to support various elements of the technology stack:

- **C#:** Microsoft.AspNet.WebApi.Client, Newtonsoft.Json, Microsoft.Azure.Cosmos
- **Python:** numpy, pandas, matplotlib, dash, plotly

Clone 
---
Clone this repository from: https://github.com/PMetcalf/uk-power-generation-project.git

Acknowledgements
---

This project collects and uses data from Elexon's BMRS site (https://www.bmreports.com/bmrs/?q=help/about-us).
