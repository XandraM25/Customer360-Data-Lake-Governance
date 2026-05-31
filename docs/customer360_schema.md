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
