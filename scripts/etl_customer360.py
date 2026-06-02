from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder \
    .appName("Customer360") \
    .getOrCreate()

# Customer Master
customers = spark.read.csv(
    "data/Churn_Modelling.csv",
    header=True,
    inferSchema=True
)

# Transactions
transactions = spark.read.csv(
    "data/fact_transaction.csv",
    header=True,
    inferSchema=True
)

# Marketing
campaigns = spark.read.csv(
    "data/fact_marketing_campaign.csv",
    header=True,
    inferSchema=True
)

# Transaction Summary
transaction_summary = transactions.groupBy(
    "customer_id"
).agg(
    count("*").alias("total_transactions"),
    round(sum("transaction_amount"), 2).alias("total_spend")
)

# Marketing Summary
campaign_summary = campaigns.groupBy(
    "customer_id"
).agg(
    count("*").alias("campaigns_received"),
    sum("response_flag").alias("responses"),
    sum("conversion_flag").alias("conversions")
)

# Customer360 Master
customer360 = customers \
    .join(
        transaction_summary,
        customers.CustomerId == transaction_summary.customer_id,
        "left"
    ) \
    .join(
        campaign_summary,
        customers.CustomerId == campaign_summary.customer_id,
        "left"
    )

customer360.show(10)

customer360.coalesce(1).write.mode("overwrite").csv(
    "data/customer360_master",
    header=True
)

print("Customer360 ETL completed.")