import pandas as pd

transactions = pd.read_csv("data/fact_transaction.csv")
campaigns = pd.read_csv("data/fact_marketing_campaign.csv")

results = []

# Transaction Checks
results.append({
    "table_name": "fact_transaction",
    "check_type": "row_count",
    "total_records": len(transactions),
    "failed_records": 0,
    "pass_rate": 100
})

results.append({
    "table_name": "fact_transaction",
    "check_type": "null_customer_id",
    "total_records": len(transactions),
    "failed_records": transactions["customer_id"].isnull().sum(),
    "pass_rate": round(
        (
            1 -
            transactions["customer_id"].isnull().sum()
            / len(transactions)
        ) * 100,
        2
    )
})

# Campaign Checks
results.append({
    "table_name": "fact_marketing_campaign",
    "check_type": "row_count",
    "total_records": len(campaigns),
    "failed_records": 0,
    "pass_rate": 100
})

results.append({
    "table_name": "fact_marketing_campaign",
    "check_type": "null_customer_id",
    "total_records": len(campaigns),
    "failed_records": campaigns["customer_id"].isnull().sum(),
    "pass_rate": round(
        (
            1 -
            campaigns["customer_id"].isnull().sum()
            / len(campaigns)
        ) * 100,
        2
    )
})

dq_results = pd.DataFrame(results)

dq_results.to_csv(
    "data/fact_data_quality_log.csv",
    index=False
)

print(dq_results)
print("Data quality checks completed.")