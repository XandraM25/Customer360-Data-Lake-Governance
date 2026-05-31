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
