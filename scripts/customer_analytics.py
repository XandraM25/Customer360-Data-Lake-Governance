import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

customer360_path = base_dir / "data" / "customer360_master"

csv_files = list(customer360_path.glob("part-*.csv"))

if not csv_files:
    raise FileNotFoundError("No Customer360 master CSV file found.")

df = pd.read_csv(csv_files[0])

total_customers = len(df)

churn_rate = round(df["Exited"].mean() * 100, 2)

avg_total_spend = round(df["total_spend"].mean(), 2)

avg_transactions = round(df["total_transactions"].mean(), 2)

campaign_response_rate = round(
    df["responses"].sum() / df["campaigns_received"].sum() * 100,
    2
)

campaign_conversion_rate = round(
    df["conversions"].sum() / df["campaigns_received"].sum() * 100,
    2
)

summary = pd.DataFrame({
    "metric": [
        "total_customers",
        "churn_rate_percent",
        "avg_total_spend",
        "avg_transactions",
        "campaign_response_rate_percent",
        "campaign_conversion_rate_percent"
    ],
    "value": [
        total_customers,
        churn_rate,
        avg_total_spend,
        avg_transactions,
        campaign_response_rate,
        campaign_conversion_rate
    ]
})

output_path = base_dir / "data" / "customer_summary_dashboard.csv"

summary.to_csv(output_path, index=False)

print(summary)
print("Customer analytics summary generated successfully.")