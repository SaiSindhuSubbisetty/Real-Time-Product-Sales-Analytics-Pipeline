# 📊 Real-Time Product Sales Analytics Pipeline

A complete real-time + batch data processing project using AWS services such as Kinesis, Lambda, Glue (PySpark), S3, Athena, and Redshift.

---

## 🚀 Project Goal

To simulate a real-time analytics pipeline that:
- Streams live sales data using AWS Kinesis.
- Processes it using Lambda and AWS Glue (PySpark).
- Stores data in S3 (raw + processed).
- Queries processed data via Athena / Redshift.

---

## 📌 Architecture

![Architecture Diagram](real_time_analytics_architecture.png)

---

## 🛠️ Tech Stack

| Component | Purpose |
|----------|---------|
| `Python` | Data generator and Lambda |
| `Kinesis` | Real-time ingestion |
| `Lambda` | Stream transformation |
| `AWS Glue` | ETL using PySpark |
| `S3` | Data lake |
| `Athena` | SQL analytics |
| `Redshift` | Optional warehouse |

---

## 📂 Folder Structure

```

.
├── lambda\_function/
│   └── lambda\_handler.py
├── glue\_jobs/
│   └── process\_sales\_glue.py
├── data\_generator/
│   └── producer.py
├── screenshots/
│   ├── sample\_data.json
│   ├── s3\_structure.png
│   ├── athena\_query\_result.png
├── real\_time\_analytics\_architecture.png
└── README.md

````

---

## ⚙️ Setup Instructions

1. **Start Kinesis stream:**
   - Create a stream with name `sales-stream`.

2. **Deploy Lambda Function:**
   - Runtime: Python 3.9
   - Trigger: Kinesis stream
   - Logic: Validate and push to raw S3

3. **Run Producer Script:**
   ```bash
   python producer.py
````

4. **Configure AWS Glue:**

   * Source: raw S3
   * Destination: processed S3
   * Format: Parquet/CSV

5. **Query with Athena:**

   * Connect to `processed/` folder
   * Sample query:

     ```sql
     SELECT product_id, SUM(quantity) AS total_sales
     FROM sales_data
     GROUP BY product_id;
     ```

---

## 📷 Sample Screenshots

| Type            | Screenshot                |
| --------------- | ------------------------- |
| 🎯 Sample Input | `sample_data.json`        |
| 🗂️ S3 Folder   | `s3_structure.png`        |
| 📈 Query Output | `athena_query_result.png` |

---

## 🧠 Learnings

* Real-time ingestion with Kinesis.
* Data lake formation with S3.
* Transformations with PySpark on Glue.
* SQL analytics on semi-structured data with Athena.

---

## 📝 License

MIT License

---

## 🙋‍♂️ Author

**Sai Sindhu Subbisetty**
GitHub: [SaiSindhuSubbisetty](https://github.com/SaiSindhuSubbisetty)

