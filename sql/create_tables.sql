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
