import pandas as pd
import psycopg2
import boto3
from io import StringIO

bucket_name = '..Your Bucket Name...'
file_key = '...Your File Name...'

s3 = boto3.client('s3', region_name = 'ap-south-1')
csv_obj =  s3.get_object(Bucket = bucket_name ,Key = file_key)
body = csv_obj['Body'].read().decode('utf-8')
df = pd.read_csv(StringIO(body))


df['Total_sold_units']= (
			df['iPhone Sales (in million units)']+
                        df['iPad Sales (in million units)']+
			df['Mac Sales (in million units)']+
			df['Wearables (in million units)']
			)
df.columns = ['State' , 'Region' , 'Iphone_Sales' , 'IPad_Sales' , 'Mac_Sales' , 'Wearables_Sales' , 'Total_Revenue_Billions' ,'Total_sold_units']

conn = psycopg2.connect(
			dbname = 'apple_sales',
			user = 'postgres',
			password = '***',
			host = 'localhost'
			)
cursor = conn.cursor()

for  _,row in df.iterrows():
	cursor.execute("""INSERT INTO regional_sales(State, Region, Iphone_Sales,Ipad_Sales,Mac_Sales,Wearables_Sales,Total_Revenue_Billions,Total_sold_units)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",tuple(row))

conn.commit()
cursor.close()
conn.close()
print("ETL Completed Successfully")
