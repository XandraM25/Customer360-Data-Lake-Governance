# Customer360 Schema Design

## dim_customer

Customer master dimension table containing demographic and profile information.

| Column Name | Data Type | Source Column | Business Definition |
|---|---|---|---|
| customer_id | BIGINT | CustomerId | Unique customer identifier |
| surname | STRING | Surname | Customer last name |
| geography | STRING | Geography | Customer geographic region |
| gender | STRING | Gender | Customer gender |
| age | INTEGER | Age | Customer age |
| tenure | INTEGER | Tenure | Number of years as customer |
| estimated_salary | DECIMAL(18,2) | EstimatedSalary | Estimated annual salary |
| customer_status | STRING | Exited | Active or Churned customer |
| created_at | TIMESTAMP | System Generated | ETL load timestamp |

## fact_account_behavior

Customer account and product relationship information.

| Column Name | Data Type | Source Column | Business Definition |
|---|---|---|---|
| behavior_id | BIGINT | Generated | Unique behavior record identifier |
| customer_id | BIGINT | CustomerId | Customer identifier |
| credit_score | INTEGER | CreditScore | Customer credit score |
| balance | DECIMAL(18,2) | Balance | Current account balance |
| num_of_products | INTEGER | NumOfProducts | Number of products owned |
| has_credit_card | BOOLEAN | HasCrCard | Whether customer owns a credit card |
| is_active_member | BOOLEAN | IsActiveMember | Whether customer is active |
| record_date | DATE | Generated | Snapshot date |

## fact_transaction

Customer transaction activity.

| Column Name | Data Type | Source Column | Business Definition |
|---|---|---|---|
| transaction_id | BIGINT | Generated | Unique transaction identifier |
| customer_id | BIGINT | CustomerId | Customer identifier |
| transaction_date | DATE | Generated | Transaction date |
| merchant_category | STRING | Generated | Merchant category |
| transaction_amount | DECIMAL(18,2) | Generated | Transaction amount |
| payment_method | STRING | Generated | Payment method |

## fact_marketing_campaign

Customer marketing campaign interactions.

| Column Name | Data Type | Source Column | Business Definition |
|---|---|---|---|
| campaign_id | BIGINT | Generated | Unique campaign identifier |
| customer_id | BIGINT | CustomerId | Customer identifier |
| campaign_type | STRING | Generated | Marketing channel |
| offer_type | STRING | Generated | Offer type |
| response_flag | BOOLEAN | Generated | Whether customer responded to the campaign |
| conversion_flag | BOOLEAN | Generated | Whether customer converted after response |
| campaign_date | DATE | Generated | Campaign date |

## fact_data_quality_log

Data quality monitoring results.

| Column Name | Data Type | Source Column | Business Definition |
|---|---|---|---|
| dq_check_id | BIGINT | Generated | Unique data quality check identifier |
| table_name | STRING | Generated | Name of the table being checked |
| check_type | STRING | Generated | Type of quality check |
| total_records | INTEGER | Generated | Total number of records checked |
| failed_records | INTEGER | Generated | Number of records that failed the check |
| pass_rate | FLOAT | Generated | Percentage of records that passed the check |
| check_timestamp | TIMESTAMP | Generated | Time when the data quality check was executed |
