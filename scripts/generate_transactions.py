import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Load customer dataset

customers = pd.read_csv("data/Churn_Modelling.csv")

# Merchant categories

merchant_categories = [
"Groceries",
"Dining",
"Travel",
"Gas",
"Retail",
"Healthcare",
"Entertainment"
]

# Payment methods

payment_methods = [
"Credit Card",
"Debit Card",
"Mobile Wallet"
]

transactions = []

transaction_id = 1

for customer_id in customers["CustomerId"]:

```
transaction_count = np.random.randint(20, 100)

for _ in range(transaction_count):

    transaction_date = (
        datetime.now()
        - timedelta(days=np.random.randint(1, 365))
    ).date()

    transaction_amount = round(
        np.random.uniform(5, 1000),
        2
    )

    merchant_category = np.random.choice(
        merchant_categories
    )

    payment_method = np.random.choice(
        payment_methods
    )

    transactions.append([
        transaction_id,
        customer_id,
        transaction_date,
        merchant_category,
        transaction_amount,
        payment_method
    ])

    transaction_id += 1
```

transaction_df = pd.DataFrame(
transactions,
columns=[
"transaction_id",
"customer_id",
"transaction_date",
"merchant_category",
"transaction_amount",
"payment_method"
]
)

transaction_df.to_csv(
"data/fact_transaction.csv",
index=False
)

print(transaction_df.shape)
print("Transaction file generated successfully.")
