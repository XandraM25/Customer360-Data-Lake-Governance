import pandas as pd
import numpy as np

customers = pd.read_csv("data/Churn_Modelling.csv")

campaign_types = ["Email", "SMS", "Mobile App", "Call Center"]
offer_types = ["Cashback", "Credit Limit Increase", "Balance Transfer", "Loan Offer"]

records = []
campaign_id = 1

for _, row in customers.iterrows():
    customer_id = row["CustomerId"]
    is_active = row["IsActiveMember"]
    exited = row["Exited"]

    campaign_count = np.random.randint(1, 5)

    for _ in range(campaign_count):
        response_probability = 0.45 if is_active == 1 else 0.20
        response_flag = np.random.choice([1, 0], p=[response_probability, 1 - response_probability])

        conversion_probability = 0.35 if response_flag == 1 and exited == 0 else 0.08
        conversion_flag = np.random.choice([1, 0], p=[conversion_probability, 1 - conversion_probability])

        records.append({
            "campaign_id": campaign_id,
            "customer_id": customer_id,
            "campaign_type": np.random.choice(campaign_types),
            "offer_type": np.random.choice(offer_types),
            "response_flag": response_flag,
            "conversion_flag": conversion_flag,
            "campaign_date": pd.Timestamp("2025-01-01") + pd.to_timedelta(np.random.randint(0, 365), unit="D")
        })

        campaign_id += 1

campaigns = pd.DataFrame(records)
campaigns.to_csv("data/fact_marketing_campaign.csv", index=False)

print(f"Generated {len(campaigns)} marketing campaign records")