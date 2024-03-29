# Databricks notebook source
# MAGIC %md 
# MAGIC 
# MAGIC ## What is a Digital Twin?
# MAGIC 
# MAGIC A Digital Twin is a virtual representation of a physical product (asset/equipment twin) or  process (process twin), used to understand and predict the physical counterpart’s performance characteristics
# MAGIC 
# MAGIC It is used throughout the product lifecycle to simulate, predict, and optimize the product and production system, before optimizing the physical assets or processes, continuously updated using real-world data.
# MAGIC 
# MAGIC Digital Twins drive advanced, value-adding use cases. Consider the following scenarios:
# MAGIC * A refinery’s crude distillation unit wants to shift fuel blends in one period and a different blend in the next period. Digital twins enable the company to simulate the changes and settings before they enact physical changes.  
# MAGIC * A company wants to reconfigure a line in a plant. It costs $200,000 per hour for a line to be down. Digital twins enable the company to test various new configurations of the line virtually before taking the line down.  
# MAGIC * An airplane engine manufacturer wants to determine when an engine needs to be serviced to ensure optimal performance and safety. They’re accountable to the airlines for on-time metrics, so any unplanned maintenance carries severe financial penalties. Digital twins are used to predict potential failure of components, and enable the maintenance crews to schedule maintenance.  
# MAGIC <br>  
# MAGIC 
# MAGIC ## Scenario - Digital Twins for EV Battery Manufacturing Plants  
# MAGIC 
# MAGIC In this demo, we’ll create an EV Battery Manufactoring plant using Azure Digital Twins, with data and insights generated by Databricks:
# MAGIC 
# MAGIC - Model a part of the manufacturing process using Azure Digital Twins
# MAGIC - Demonstrate Databricks’ ingestion capabilities to efficiently and continuously process IoT data
# MAGIC - Leverage Databricks to showcase 2 common uses for digital twins in manufacturing:
# MAGIC   - **Predictive Maintenance**
# MAGIC   - **Root Cause Analysis & Troubleshooting**

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Why Databricks?
# MAGIC 
# MAGIC <img src="https://pawaritstorageaccount.blob.core.windows.net/public/digital-twin-gtm/digital-twins-challenges.png" width=88%>

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ### Enabling advanced analytics for Digital Twins with Azure Databricks
# MAGIC 
# MAGIC Azure Digital Twins provides a great visual overview and representation of our system.  
# MAGIC However, more intelligent insights into the processes often require more advanced modelling capabilities. 
# MAGIC 
# MAGIC #### Desired Capabilities
# MAGIC 
# MAGIC Customers often want to apply their own **(programmatic) business logic** in order to achieve:
# MAGIC - custom transformations, aggregations
# MAGIC - simulations and predictions using arbitrary models (e.g. Machine Learning)
# MAGIC - virtual sensing (aka soft sensing)
# MAGIC 
# MAGIC Databricks provides high performance and scalability while flexibly allowing you to express meaningful, domain-specific insights.  
# MAGIC <img src="https://pawaritstorageaccount.blob.core.windows.net/public/digital-twin-gtm/digital-twins-key-capabilities.png" width=69%>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Step 1: Create your digital twin instance(s) on Azure Digital Twins
# MAGIC 
# MAGIC <br>
# MAGIC 
# MAGIC 1. From your Azure Portal, create a new instance of Azure Digital Twins 
# MAGIC    - Don't forget to grant yourself the **Azure Digital Twins Data Owner** role
# MAGIC    - Once your instance has been created, launch the Azure Digital Twins Explorer UI
# MAGIC 2. Clone the following GitHub repo: [https://github.com/PawaritL/databricks-azure-digital-twin](https://github.com/PawaritL/databricks-azure-digital-twin)
# MAGIC    - Note the `models/` folder and the `twins/TwinGraph.json` file
# MAGIC 3. Under **MODELS** (towards the left), click [*Upload a directory of Models*](https://docs.microsoft.com/en-us/azure/digital-twins/how-to-use-azure-digital-twins-explorer#upload-models)
# MAGIC    - Upload the entire `models/` folder from the cloned repo
# MAGIC 4. Under **TWIN GRAPH** then [*Import graph*](https://docs.microsoft.com/en-us/azure/digital-twins/how-to-use-azure-digital-twins-explorer#import-file-to-azure-digital-twins-explorer)
# MAGIC    - Upload the `twins/TwinGraph.json` file
# MAGIC 5. You should then a twin graph similar to the screenshot below. Finally, click the *Save* icon.
# MAGIC 
# MAGIC <img src="https://pawaritstorageaccount.blob.core.windows.net/public/digital-twin-gtm/azure-digital-twins-screenshot.png" width=69%>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Step 2: Enrich your twins with custom business logic and intelligence with Databricks
# MAGIC 
# MAGIC <br>
# MAGIC continue along this notebook :)

# COMMAND ----------

# MAGIC %pip install azure-identity azure-digitaltwins-core

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Use Case: Vibration Fault Detection
# MAGIC 
# MAGIC Some popular use-cases digital twins include health monitoring, fault detection, and predictive maintenance.  
# MAGIC In our scenario, vibrations in our mixing stations can quickly lead to plant outages, having very high impact on revenue.  
# MAGIC To solve this issue, the business asked us to detect early onset of vibration faults in the production line.  
# MAGIC 
# MAGIC Our domain experts have been collecting vibration reports from our mixers then cross-referencing them with subsequent machine faults.  
# MAGIC Using this dataset, we can then build **and productionize** a predictive maintenance model as follows:

# COMMAND ----------

import pandas as pd

storage_account = "pawaritstorageaccount" # for original training set

vibration_reports_path = f"https://{storage_account}.blob.core.windows.net/public/digital-twin-gtm/data/model_development/vibration_reports.csv"
vibration_reports = spark.createDataFrame(pd.read_csv(vibration_reports_path))
vibration_reports.write.mode("overwrite").saveAsTable("vibration_reports_labelled")

display(vibration_reports)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #### Reproducible, enterprise-grade Data Science & ML
# MAGIC 
# MAGIC While data scientists might have great ideas or prototypes, getting to production has been notoriously challenging. 
# MAGIC <br>  
# MAGIC **Especially:**  
# MAGIC 1. Ensuring robust, production-grade code that is consistent across environments
# MAGIC 2. Proper tracking and versioning of models and data for reproducibility and auditability
# MAGIC 3. Meeting DevOps standards (e.g. automated tests before transitioning from *DEV* to *STAGING* to *PROD*, rollbacks, etc.)
# MAGIC 
# MAGIC Databricks ML doesn't only focus on model development and training, but addresses the MLOps lifecycle holistically.
# MAGIC 
# MAGIC <img src="https://pawaritstorageaccount.blob.core.windows.net/public/digital-twin-gtm/databricks-ml.png" width=50%>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Accelerating Predictive Maintenance using Databricks AutoML  
# MAGIC <br>
# MAGIC <img style="float: right" width="500" src="https://github.com/QuentinAmbard/databricks-demo/raw/main/retail/resources/images/churn-auto-ml.png"/>
# MAGIC 
# MAGIC ### A glass-box solution that empowers data teams without taking away control
# MAGIC 
# MAGIC Bootstraping new ML projects can be long and inefficient.  
# MAGIC Instead of creating the same boilerplate code for each new project, Databricks AutoML can automatically generate robust models **with code** for classification, regression, and forecasting.
# MAGIC 
# MAGIC Models can either be deployed directly or you can tweak/modify the generated code with your own domain expertise, saving you weeks of effort.
# MAGIC 
# MAGIC ### Using the Databricks AutoML UI
# MAGIC 
# MAGIC A dataset containing labels on faulty mixers has been provided.  
# MAGIC All we have to do is start a new AutoML experiment and select the dataset `vibration_reports_labelled`  
# MAGIC Our prediction target is the `fault` column.
# MAGIC 
# MAGIC Click on *Start*, and Databricks will do the rest.
# MAGIC 
# MAGIC While this is done using the UI, you can also leverage the [Python API](https://docs.databricks.com/applications/machine-learning/automl.html#automl-python-api-1) (see example below)

# COMMAND ----------

import databricks.automl

run_automl = False # change to True if you're not a Databricks employee on the demo workspace!

if run_automl:
  
  # Successfully run on ML Runtime 10.4 LTS
  summary = databricks.automl.classify(
    dataset=vibration_reports,
    target_col="fault",
    timeout_minutes=5,
  )

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### MLOps - Productionize your models and manage their lifecycles
# MAGIC 
# MAGIC The team have now validated (and perhaps tweaked) the best model generated by Databricks AutoML and would like to productionize the model.  
# MAGIC MLflow's experiment tracking and model registry on Databricks ensures that results and deployments are properly versioned and reproducible.
# MAGIC 
# MAGIC Most importantly, guardrails and verification steps can be enforced via [MLflow Webhooks](https://databricks.com/blog/2022/02/01/streamline-mlops-with-mlflow-model-registry-webhooks.html) (e.g. when transitioning models from development/staging to production). This ensures that deployment procedures in your organization are adhered to.

# COMMAND ----------

import mlflow
from mlflow.tracking.client import MlflowClient

model_name = "vibration_fault_detection"

if run_automl:

  # Find path to our best model from AutoML, then add it to our model registry
  model_uri = summary.best_trial.model_path
  model_details = mlflow.register_model(model_uri=model_uri, name=model_name)

  # Transition the model to the Production environment
  client = MlflowClient()
  client.transition_model_version_stage(
    name=model_details.name,
    version=model_details.version,
    stage="production",
  )

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Integrating with your live environment
# MAGIC 
# MAGIC IoT data integration often happens in two typical patterns:  
# MAGIC 
# MAGIC - Stream-based or message-based  
# MAGIC   - Databricks can read streams directly from Kafka / Event Hub topics 
# MAGIC   - Great for continuous, always-on streams 
# MAGIC   
# MAGIC - File-based  
# MAGIC   - Your IoT systems upload files (CSV, JSON, or even binary)
# MAGIC   - Uploads can either be regular (e.g. every hour) or sporadical

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #### Scalable exactly-once data ingestion with Auto Loader
# MAGIC 
# MAGIC In this example, we'll see why Databricks Auto Loader is an extremely popular choice for processing files uploaded by IoT systems.
# MAGIC 
# MAGIC <br>
# MAGIC <img src="https://pawaritstorageaccount.blob.core.windows.net/public/digital-twin-gtm/databricks-auto-loader.png" width=69%>

# COMMAND ----------

# DBTITLE 1,Retrieve credentials to read from your landing zone 
import os 

azSubcriptionId = dbutils.secrets.get(scope = "common-sp", key = "az-sub-id") # TODO: please change to your own credentials
azTenantId = dbutils.secrets.get(scope = "common-sp", key = "az-tenant-id") # TODO: please change to your own credentials
spId = dbutils.secrets.get(scope = "common-sp", key = "common-sa-sp-client-id") # TODO: please change to your own credentials
spSecret = dbutils.secrets.get(scope = "common-sp", key = "common-sa-sp-client-secret") # TODO: please change to your own credentials

os.environ["AZURE_TENANT_ID"] = azTenantId
os.environ["AZURE_CLIENT_ID"] = spId
os.environ["AZURE_CLIENT_SECRET"] = spSecret

storage_account = "pawaritstorageaccount" # TODO: please change to your own storage account

spark.conf.set("spark.sql.shuffle.partitions", 1) # just for this demo
spark.conf.set(f"fs.azure.account.auth.type.{storage_account}.dfs.core.windows.net", "OAuth")
spark.conf.set(f"fs.azure.account.oauth.provider.type.{storage_account}.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set(f"fs.azure.account.oauth2.client.id.{storage_account}.dfs.core.windows.net", spId)
spark.conf.set(f"fs.azure.account.oauth2.client.secret.{storage_account}.dfs.core.windows.net", spSecret)
spark.conf.set(f"fs.azure.account.oauth2.client.endpoint.{storage_account}.dfs.core.windows.net", f"https://login.microsoftonline.com/{azTenantId}/oauth2/token")

# COMMAND ----------

import pyspark.sql.functions as F
from pyspark.sql.types import *

import requests

from azure.digitaltwins import *
from azure.digitaltwins.core import DigitalTwinsClient
from azure.identity import *

# COMMAND ----------

feature_columns = ['max', 'min', 'mean', 'sd', 'rms', 'skewness', 'kurtosis', 'crest', 'form']
schema = ", ".join([x + " float" for x in feature_columns])

dbutils.fs.rm("./tmp/digital_twin_upload_schema/", True)
dbutils.fs.mkdirs("./tmp/digital_twin_upload_schema/")

file_name_expr = F.reverse(F.split(F.input_file_name(), "/")).getItem(0)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #### Auto Loader Example
# MAGIC 
# MAGIC - Let's pick up the vibration monitoring dumps from our machines
# MAGIC - We can then process them on-the-fly to produce real-time insights and even machine learning inference

# COMMAND ----------

landing_zone_storage_account = "pawaritstorageaccount" # TODO: please change to your own storage account
landing_zone_storage_container = "demo" # TODO: please change to your own storage container
landing_zone_path = f"abfss://{landing_zone_storage_container}@{landing_zone_storage_account}.dfs.core.windows.net/digital-twin/data/landing_zone"

input_df = (
  spark
    .readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("header", "true")
    .option("cloudFiles.schemaLocation", "/tmp/digital_twin_upload_schema/")
    .option("cloudFiles.schemaHints", schema)
    .option("cloudFiles.useIncrementalListing", "true") # for demo purposes, no checkpointing
    .load(landing_zone_path)
)

input_df = input_df.select(file_name_expr.alias("fileName"), "*") # Get file name from ADLS path
input_df = input_df.withColumn("station_id", F.lit("MixingStep-Line1-Munich")) # for this demo, simulate just one station for clarity
display(input_df)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #### Apply business logic (e.g. custom transformations, aggregations, predictions)
# MAGIC 
# MAGIC In this example, we'll apply an ML model to the data to predict potential vibration faults.

# COMMAND ----------

import mlflow.pyfunc

# Load the current (latest) model from the PROD environment
model_name = "vibration_fault_detection"
environment = "production" 
model_production_uri = f"models:/{model_name}/{environment}"

print("Loading registered model version from URI: '{model_uri}'".format(model_uri=model_production_uri))

# Load the current (latest) model from the PROD environment into a User-Defined Function (UDF)
# Make sure the model exists on your workspace: set run_automl to True if you don't have the trained model in your workspace yet! 
loaded_model = mlflow.pyfunc.spark_udf(spark, model_uri=model_production_uri, result_type='string')

# Apply our LightGBM model immediately to our incoming data
prediction_df = input_df.withColumn("prediction", loaded_model(*feature_columns))
prediction_df = prediction_df.withColumn(
  "prediction", F.when(F.col("prediction").startswith("Normal"), "NORMAL").otherwise("BALL_FAULT_PREDICTED")
)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Live Prediction Example: Update your Azure Digital Twin instance
# MAGIC 
# MAGIC As Databricks allows custom, programmatic functions. You can flexibly update your Azure Digital Twin instance from Databricks.  
# MAGIC In this example, we'll use the Python SDK directly. However, you can also use Event Hubs + Azure Functions to update your twins in case you prefer to decouple your core Databricks streaming job from your Azure Digital Twin updates. 

# COMMAND ----------

# In the subsequent cells, we'll be updating our Azure Digital Twin instance with these predictions
display(prediction_df.select("station_id", "prediction", "*")) # healthPrediction supplied by the ML model we developed earlier

# COMMAND ----------

adt_url = "battery-plant-digital-twin.api.eus2.digitaltwins.azure.net" # replace this with your own Azure Digital Twin URL
twin_graph_path = "https://raw.githubusercontent.com/PawaritL/databricks-azure-digital-twin/main/twins/TwinGraph.json"

credential = DefaultAzureCredential()
service_client = DigitalTwinsClient(adt_url, credential)

twin_graph_json = requests.get(twin_graph_path).json()
twin_graph = twin_graph_json["digitalTwinsGraph"]
twins = twin_graph["digitalTwins"]
  
twin_dict = {twin["$dtId"]: twin for twin in twins}
twin_dict_b = sc.broadcast(twin_dict)

def publish_mixer_health(batch_df, batch_id):
  batch_pdf = batch_df.toPandas()

  for idx, row in batch_pdf.iterrows():
    temporary_twin = twin_dict_b.value.get(row["station_id"])
    patch = {
      "HealthPrediction": "OK" if (row["prediction"] == "NORMAL") else "FAULT_PREDICTED",
      "BallBearings": {
        "faultPredicted": row["prediction"] != "NORMAL",
        "$metadata": {}
      },
    }
    temporary_twin.update(patch)
    service_client.upsert_digital_twin(row["station_id"], temporary_twin)
  return

# COMMAND ----------

prediction_df.writeStream.foreachBatch(publish_mixer_health).trigger(processingTime="10 seconds").start()

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC ## Improving Root Cause Analysis and Troubleshooting
# MAGIC 
# MAGIC While predictive maintenance is an extremely popular use case, there are many instances where it might not be feasible.  
# MAGIC Nevertheless, even troubleshooting or understanding *when, how, or why* things failed can provide substantial business value.
# MAGIC 
# MAGIC For example:
# MAGIC - Diagnosing the correct subsystem, equipment, or sensor at fault minimizes downtime, maintenance costs
# MAGIC - Avoiding No Fault Found (NFF) errors
# MAGIC   - NFF is thought to cost the United States Department of Defense in excess of US$2 billion per year [[Reference]](https://en.wikipedia.org/wiki/No_fault_found#cite_note-5)
# MAGIC - Understanding the underlying behaviour can help inform appropriate design or operating conditions in the future
# MAGIC 
# MAGIC This is where quick self-serve visualizations and ad-hoc queries can come in extremely handy.  
# MAGIC [See some quick examples with **Databricks SQL**!](https://docs.microsoft.com/en-gb/azure/databricks/sql/get-started/sample-dashboards)
# MAGIC 
# MAGIC ***Databricks staff only:***  
# MAGIC [Here's](https://eastus2.azuredatabricks.net/sql/dashboards/a5f9d0bd-60cb-4130-b21e-4330010a14d3?o=5206439413157315) one built for this specific use case

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Open ecosystem & APIs
# MAGIC 
# MAGIC The insights we've generated can be immediately used downstream for live decision-making.  
# MAGIC We can use either managed Spark connectors or work with arbitrary SDKs and APIs in Python, Java, Scala, R.
# MAGIC 
# MAGIC <img src="https://pawaritstorageaccount.blob.core.windows.net/public/digital-twin-gtm/databricks-ecosystem.png" width=69%>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Closing the loop - Recap
# MAGIC 
# MAGIC Databricks enables advanced analytics use cases such as custom logic, predictions, virtual (aka soft) sensing, etc.
# MAGIC   - Enriches & brings intelligence to raw data and knowledge graphs on Azure Digital Twins
# MAGIC     - Demo w/ Azure Digital Twins 3D Scenes Studio **coming soon!**
# MAGIC   - Accommodates DevOps and MLOps best practices
# MAGIC   
# MAGIC Databricks unlocks a wide ecosystem through flexible, open programmatic capabilities
# MAGIC   - Orchestrate workflows either as real-time streams or scheduled jobs
# MAGIC   - This allows you to integrate insights directly into your live production environment
# MAGIC   
# MAGIC <img src="https://pawaritstorageaccount.blob.core.windows.net/public/digital-twin-gtm/digital-twins-reference-architecture.png" width=88%>
