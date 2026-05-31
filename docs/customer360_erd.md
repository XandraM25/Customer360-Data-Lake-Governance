# Customer360 Data Model

## Overview
This document describes the logical data model for the Customer360 Data Lake & Governance Platform.

## Core Tables

### dim_customer

Master customer profile table containing demographic, account, and customer status information.

### fact_transaction

Customer transaction activity and spending behavior.

### fact_marketing_campaign

Marketing campaign interactions and conversion tracking.

### fact_data_quality_log

Data quality monitoring results including completeness, uniqueness, validity, and freshness checks

## Data Flow
Raw Customer Data
→ AWS S3 Raw Layer
→ AWS Glue Catalog
→ PySpark ETL
→ Snowflake
→ Power BI Dashboard
