CREATE OR REPLACE TABLE dim_customer (
    customer_id BIGINT,
    surname STRING,
    geography STRING,
    gender STRING,
    age INTEGER,
    tenure INTEGER,
    estimated_salary DECIMAL(18,2),
    customer_status STRING,
    created_at TIMESTAMP
);

CREATE OR REPLACE TABLE fact_account_behavior (
    behavior_id BIGINT,
    customer_id BIGINT,
    credit_score INTEGER,
    balance DECIMAL(18,2),
    num_of_products INTEGER,
    has_credit_card BOOLEAN,
    is_active_member BOOLEAN,
    record_date DATE
);

CREATE OR REPLACE TABLE fact_transaction (
    transaction_id BIGINT,
    customer_id BIGINT,
    transaction_date DATE,
    merchant_category STRING,
    transaction_amount DECIMAL(18,2),
    payment_method STRING
);
