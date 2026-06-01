import pandas as pd
import numpy as np

# Load customer dataset
customers = pd.read_csv("data/Churn_Modelling.csv")

# Number of transactions per customer
transactions_per_customer = 50

records = []

for _, row in customers.iterrows():

    customer_id = row["CustomerId"]

    for _ in range(transactions_per_customer):

        records.append(
            {
                "customer_id": customer_id,
                "transaction_date": pd.Timestamp("2025-01-01")
                + pd.to_timedelta(
                    np.random.randint(0, 365),
                    unit="D"
                ),
                "merchant_category": np.random.choice(
                    [
                        "Grocery",
                        "Restaurant",
                        "Travel",
                        "Retail",
                        "Gas",
                        "Healthcare"
                    ]
                ),
                "transaction_amount": round(
                    np.random.uniform(5, 500),
                    2
                ),
                "payment_method": np.random.choice(
                    [
                        "Credit Card",
                        "Debit Card",
                        "Mobile Wallet"
                    ]
                )
            }
        )

transactions = pd.DataFrame(records)

transactions.to_csv(
    "data/fact_transaction.csv",
    index=False
)

print(
    f"Generated {len(transactions)} transactions"
)