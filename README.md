# Customer360 Analytics Platform

## Overview

Customer360 Analytics Platform is an end-to-end customer analytics project designed to demonstrate modern data engineering, data warehousing, and business intelligence workflows.

The project focuses on customer churn analysis, customer behavior analytics, and marketing campaign performance monitoring using:

- PySpark
- Snowflake
- SQL
- Power BI

The solution processes customer-level data, creates analytical tables in Snowflake, and delivers executive dashboards for business decision-making.

---

## Architecture

```text
Customer360 Dataset
        │
        ▼
   PySpark ETL
        │
        ▼
Snowflake Data Warehouse
        │
        ▼
Analytics Tables
 ├── CUSTOMER_CHURN_ANALYTICS
 └── CUSTOMER_MARKETING_ANALYTICS
        │
        ▼
 Power BI Dashboards
```

---

## Business Objectives

This project was built to answer the following business questions.

### Customer Churn Analysis

- Which customer segments have the highest churn rates?
- Which geographies experience the highest customer attrition?
- Are high-value customers more likely to churn?

### Marketing Performance Analysis

- How many campaigns are customers receiving?
- How often do customers respond?
- What is the conversion rate?
- What is the average customer spend?

---

## Dataset

The project uses a Customer360 dataset containing:

- 10,000 Customers

### Key Attributes

- Customer ID
- Geography
- Age
- Credit Score
- Balance
- Tenure
- Product Count
- Active Membership Status
- Estimated Salary
- Churn Indicator

### Marketing Attributes

- Campaigns Received
- Responses
- Conversions
- Total Spend

---

## PySpark ETL Pipeline

PySpark was used to perform data cleaning, transformation, and aggregation.

### Data Cleaning

- Null handling
- Schema validation
- Data quality checks

### Data Transformation

- Customer-level aggregation
- Marketing campaign metrics
- Customer spending calculations

### Feature Engineering

- Total Transactions
- Total Spend
- Campaign Response Metrics
- Conversion Metrics

### Output Datasets

```text
customer360_master.csv
customer_summary_dashboard.csv
```

---

## Snowflake Data Warehouse

### Database

```sql
CUSTOMER360_DB
```

### Schema

```sql
CUSTOMER360_SCHEMA
```

### Warehouse

```sql
CUSTOMER360_WH
```

### Core Table

```sql
CUSTOMER360_MASTER
```

### Loaded Records

- 10,000 Rows
- 19 Columns

---

## Analytics Tables

### CUSTOMER_CHURN_ANALYTICS

Purpose:

Analyze customer churn behavior by geography.

Metrics:

- Churn Rate
- Average Age
- Average Balance
- Average Credit Score
- Customer Count

#### Sample Results

| Geography | Churn Rate |
|------------|------------|
| Germany | 32.44% |
| Spain | 16.67% |
| France | 16.15% |

---

### CUSTOMER_MARKETING_ANALYTICS

Purpose:

Evaluate marketing campaign effectiveness.

Metrics:

- Average Campaigns Received
- Average Responses
- Average Conversions
- Average Spend

#### Sample Results

| Metric | Value |
|----------|----------:|
| Avg Campaigns | 2.52 |
| Avg Responses | 0.83 |
| Avg Conversions | 0.39 |
| Avg Spend | $12,631 |

---

## Power BI Dashboards

### Executive Dashboard

#### KPIs

- Total Customers
- Churn Rate
- Campaign Response Rate
- Campaign Conversion Rate
- Average Spend

#### Visualizations

- Customers by Geography
- Churn Rate by Geography
- Average Credit Score by Churn Status
- Average Balance by Churn Status
- Average Age by Churn Status
- Churn Rate by Tenure

---

### Snowflake Analytics Dashboard

#### Data Source

```text
Snowflake Analytics Tables
```

#### Visualizations

- Customer Count by Geography
- Churn Rate by Geography
- Average Balance by Geography
- Average Customer Spend
- Average Campaigns Received
- Average Campaign Responses
- Average Campaign Conversions

---

## Key Business Insights

### Geography Analysis

Germany has the highest churn rate:

**32.44%**

Compared with:

- France: 16.15%
- Spain: 16.67%

---

### Customer Value Analysis

Customers in Germany maintain significantly higher balances:

**$119K**

Compared with:

- France: ~$62K
- Spain: ~$62K

This indicates a concentration of high-value customers at risk of attrition.

---

### Age Analysis

Churned customers are older on average:

**44.84 years**

Compared with:

**37.41 years**

for retained customers.

---

## Technologies

### Data Engineering

- Python
- PySpark
- Pandas

### Data Warehouse

- Snowflake
- SQL

### Business Intelligence

- Power BI

### Version Control

- Git
- GitHub

---

## Future Enhancements

- AWS S3 Integration
- Automated Snowflake Data Loading
- Data Lineage Documentation
- Metadata Management
- Customer Segmentation Modeling
- Predictive Churn Modeling