from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import json
import os
from datetime import datetime

# 1. สร้าง Spark session พร้อมเชื่อมต่อ Cassandra
spark = SparkSession.builder \
    .appName("DataProcessingWithCassandra") \
    .config("spark.cassandra.connection.host", "192.168.100.8") \
    .config("spark.cassandra.connection.port", "9042") \
    .getOrCreate()

# 2. อ่านไฟล์ config สำหรับการตั้งค่าต่างๆ
def load_config(config_path):
    with open(config_path) as config_file:
        config = json.load(config_file)
    return config

config = load_config("data_storage/config/storage_config.json")
input_directory = config["input_directory"]  # /data_storage/raw_data
output_directory = config["output_directory"]  # /data_storage/processed_data
log_file = config["logs_path"]  # /data_storage/logs/processing_log.txt

# 3. อ่านไฟล์ CSV จาก raw_data
def read_csv_files(directory):
    df = spark.read.option("header", "true").csv("/Users/punchpnp/dsde-project/data_storage/raw_data/real_data.csv")
    df.head(5)
    return df

raw_data_df = read_csv_files(input_directory)
raw_data_df.show()

raw_data_df.printSchema()

# 4. ประมวลผลข้อมูล (ตัวอย่าง: การแปลงข้อมูล)
processed_data_df = raw_data_df.withColumn("processed_time", current_timestamp())

# 5. เชื่อมต่อและบันทึกข้อมูลไปยัง Cassandra
def save_to_cassandra(df, keyspace, table):
    df.show(5)
    df.write \
        .format("org.apache.spark.sql.cassandra") \
        .option("keyspace", keyspace) \
        .option("table", table) \
        .mode("overwrite") \
        .save()

# ตัวอย่างการบันทึกข้อมูลลงใน Cassandra
save_to_cassandra(processed_data_df, "space1", "table1")

# 8. หยุด Spark session เมื่อเสร็จ
spark.stop()
