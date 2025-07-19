# 📊 Real-Time Product Sales Analytics Pipeline

## ✅ Project Overview

This project demonstrates a real-time and batch processing pipeline for product sales data using AWS services.

### 🔍 Goal
To stream, store, process, and analyze product sales data in near real-time.

## 🛠 AWS Services Used

- **Amazon Kinesis** – Real-time data ingestion.
- **AWS Lambda** – Data transformation and forwarding to S3.
- **Amazon S3** – Raw and processed data storage.
- **AWS Glue (PySpark)** – Batch ETL processing.
- **Amazon Athena / Redshift** – Query and analyze processed data.

## 🧱 Folder Structure

```
real-time-product-sales-analytics/
│
├── simulate_sales.py
├── lambda/
│   └── stream_processor.py
├── glue/
│   └── etl_script.py
├── data/
│   └── sample_data.json
└── README.md
```

## 🚀 Setup Instructions

1. Create a Kinesis stream: `product-sales-stream`
2. Deploy Lambda using `stream_processor.py`, triggered by Kinesis
3. Create S3 buckets:
   - `product-sales-raw-data`
   - `product-sales-processed-data`
4. Create a Glue job with `etl_script.py`
5. Use Athena to run queries on the `product-sales-processed-data` bucket

## 📎 Sample Athena Query

```sql
SELECT product_name, SUM(quantity) AS total_quantity
FROM sales_data
GROUP BY product_name;
```

---

Created with ❤️ by Sai Sindhu Subbisetty