# 🧊 Cloud-Based ETL Pipeline: Apple Regional Sales Data

This project demonstrates a complete **end-to-end ETL pipeline** using **AWS S3**, **EC2**, **PostgreSQL**, and **Python**. It pulls Apple’s regional product sales data from S3, performs transformations (like calculating total units sold), and loads it into a structured PostgreSQL database for analysis.

---

## 🚀 Technologies Used

- **Amazon S3** – File storage for the raw CSV dataset  
- **Amazon EC2** – Cloud compute instance for ETL execution  
- **Python 3** – Core programming language  
- **pandas** – For data manipulation  
- **boto3** – For accessing S3 from Python  
- **psycopg2** – PostgreSQL database connection  
- **PostgreSQL** – Destination for cleaned and transformed data  

---

## 📊 Sample Dataset(https://www.kaggle.com/datasets/akshitachauhan123/apple-sales-dataset2024)

| State      | Region        | iPhone Sales | iPad Sales | Mac Sales | Wearables | Services Revenue |
|------------|----------------|--------------|------------|-----------|-----------|------------------|
| UK         | Europe         | 25.47        | 7.41       | 7.18      | 7.56      | 17.20            |
| New York   | North America  | 22.37        | 6.74       | 4.39      | 3.22      | 16.07            |
| Thailand   | Rest of Asia   | 16.70        | 8.13       | 6.46      | 3.48      | 13.29            |

---

## ⚙️ How to Run (Local or EC2)

1. **Create a virtual environment**  (Since i used ubuntu for my ec2 and it was not supporting the installation of python packages on local env)
   `python3 -m venv etl-env && source etl-env/bin/activate`

2. **Install required packages**  
   `pip install pandas boto3 psycopg2-binary`

3. **Set up PostgreSQL**  
   - Create DB: `apple_sales`  
   - Create table `regional_sales` with proper schema

4. **Upload dataset** to your S3 bucket

5. **Configure AWS CLI**  
   `aws configure` → add keys, region, format

6. **Run the script**  
   `python3 etl_script.py`

---

## 🔄 Data Transformations(Basic Data Processing for sample)

- Renamed messy column names  
- Calculated `total_units_sold` = sum of iPhone, iPad, Mac, and Wearables

---


## 🧹 Cleanup Reminder (For AWS Users)

- Terminate EC2 instances when not in use  
- Delete S3 bucket or files if no longer needed  
- Deactivate IAM access keys (for security)

---

## 🙌 Author

Built with caffeine & curiosity by **Abhishakth** ☕  
Reach out for collabs, data problems!

