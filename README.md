# Azure Databricks + Azure Digital Twins
Demo Example for Databricks + Azure Digital Twin

## Example Demo Presentation
- [Here](https://drive.google.com/drive/folders/1C7QlG2i81O8DSvek4BNGSpOzPBhoAcZ1?usp=sharing)

## Contact
- Pawarit Laosunthara
- Tom Bonfert

## Scenario - Digital Twins for EV Battery Manufacturing Plants  

In this demo, we’ll aim to:
- Model a part of the manufacturing process using Azure Digital Twins
- Demonstrate Databricks’ Structured Streaming, ML capabilities, and connectivity to Azure Digital Twins
- Showcase 2 common uses for digital twins in manufacturing:
  - Predictive Maintenance
  - Root Cause Analysis & Troubleshooting

**Example: Battery Manufacturing Process**  
<img src="https://pawaritstorageaccount.blob.core.windows.net/public/digital-twin-gtm/digital-twins-battery-manufacturing-process.png" width=69%>

## Prerequisites
- Access to https://eastus2.azuredatabricks.net/
- Member of the *sales* Azure AD group ([search your name here](https://portal.azure.com/#blade/Microsoft_AAD_IAM/GroupDetailsMenuBlade/Members/groupId/09018260-2d7d-4b24-8633-8243c4b92340))

## Pre-Demo Instructions
1. Check your access to our [“Battery Manufacturing” instance on Azure Digital Twin Explorer](https://explorer.digitaltwins.azure.net/?tid=9f37a392-f0ae-4280-9796-f1864a10effc&eid=battery-plant-digital-twin.api.eus2.digitaltwins.azure.net)
2. Ensure that you have a cluster running with at least ML Runtime 10.4 LTS. **Shared Autoscaling Americas** or **Shared Autoscaling EMEA** should work
3. Navigate to the *notebooks* folder
4. *Run All* on each of them.

## Pre-Demo Saved Queries
- Feel free to use these saved queries for your demo :)
    - ```SELECT * FROM digitaltwins``` to show everything
    - ```SELECT * FROM digitaltwins WHERE HealthPrediction != 'OK'``` to show twins with health warnings
    - ```SELECT target FROM DIGITALTWINS source JOIN target RELATED source.rel_runs_steps   WHERE source.$dtId = 'ProductionLine2-Dallas'``` graph query to find all stations operated by `ProductionLine2-Dallas`

## Demo
1. After a brief introduction, click the [Twin Explorer](https://explorer.digitaltwins.azure.net/?tid=9f37a392-f0ae-4280-9796-f1864a10effc&eid=battery-plant-digital-twin.api.eus2.digitaltwins.azure.net) link in the first cell, explain how:
    - We have multiple plants/geographies consolidated
    - Click any MixingStep then quickly talk about the components and properties
    - You can run `SELECT * FROM digitaltwins WHERE HealthPrediction != 'OK'` to look for any assets meeting this certain condition (it should already be saved and available from the top-left of the screen)
      - there should be no results returned
2. Walk through the [`Databricks - Generating Intelligence for Digital Twins`](https://eastus2.azuredatabricks.net/?o=5206439413157315#notebook/3684663034102300/command/3684663034102302) notebook thoroughly, showing how we can do streaming inference directly pulling models from MLflow
    - Head back to the Twin Explorer
    - Run ```SELECT * FROM digitaltwins WHERE HealthPrediction != 'OK'``` again, you should now see `MixingStep-Line1-Munich`
      - click the + sign (Expand tree) to show `HealthPrediction` and `BallBearings.faultPredicted`
      - we've now made predictive maintenance a lot less ambiguous through the knowledge graph!
    - Stop *right before* the **Improving Root Cause Analysis and Troubleshooting** section
3. Return back to the **Improving Root Cause Analysis and Troubleshooting** section in the main notebook, where you'll see a link to the [Databricks SQL dashboard](https://eastus2.azuredatabricks.net/sql/dashboards/a5f9d0bd-60cb-4130-b21e-4330010a14d3?o=5206439413157315) created specifically for this use case.
    - To find all the stations being operated by `ProductionLine2-Dallas`:  
      ```
      SELECT target FROM DIGITALTWINS source JOIN target RELATED source.rel_runs_steps  
      WHERE source.$dtId = 'ProductionLine2-Dallas'
      ```
    - Pitch Databricks SQL's flexibility for all sorts of analytics (not just time series) + easy scheduling and alerting
4. Wrap it up by heading towards the end of [`Databricks - Generating Intelligence for Digital Twins`](https://eastus2.azuredatabricks.net/?o=5206439413157315#notebook/3684663034102254/command/3684663034102258)
5. Don't forget to click **Stop Execution** on all notebooks
    - To be safe, please also hit **Cancel** on any running (streaming) cells
