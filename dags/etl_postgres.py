from datetime import datetime, timedelta
import requests
import json
import csv
import psycopg2
import os
from dotenv import dotenv_values

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

CONFIG = dotenv_values(".env")
if not CONFIG:
    CONFIG = os.environ

url = "https://data.cityofnewyork.us/resource/ia2d-e54m.json"
path = "/home/airflow/water_consumption.csv"

def dwh_data():
    conn = psycopg2.connect(host=CONFIG["POSTGRES_HOST"],
                            port=CONFIG["POSTGRES_PORT"],
                            database=CONFIG["POSTGRES_DB"],
                            user=CONFIG["POSTGRES_USER"],
                            password=CONFIG["POSTGRES_PASSWORD"])
    return conn
    
def down_load_data():  
    r = requests.get(url)
    data = json.loads(r.text)
    csv_data = []
    column_names = list(data[0].keys())
    for row in data[:3]:
        row_data = [row[column_names[0]], row[column_names[1]], row[column_names[2]], row[column_names[3]]]
        row_data = [eval(i) for i in row_data]
        csv_data.append(row_data)
    with open(path, "w") as f:
        wr = csv.writer(f)
        wr.writerows(csv_data)

def insert_data():
    connection = dwh_data()
    cursor = connection.cursor()
    with open(path, 'r') as f:  
        for row in f:

            cursor.execute("""
                INSERT INTO public.water_consumption
                VALUES ('{}', '{}', '{}', '{}', '{}')""".format(row.split(",")[0],
                                                                row.split(",")[1],
                                                                row.split(",")[2],
                                                                row.split(",")[3],
                                                                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                )
            )
    connection.commit()
    
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 4, 15),
    'email': ['user@mail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG('etl_postgres', schedule_interval="@once", default_args=default_args) as dag:

    down_load_data = PythonOperator(task_id='down_load_data', 
                                    python_callable=down_load_data)

    insert_data = PythonOperator(task_id='insert_data', 
                                   python_callable=insert_data)
    
down_load_data>>insert_data