from pyspark.sql import SparkSession

# สร้าง Spark Session
spark = SparkSession.builder \
    .appName("CSVtoCassandra") \
    .config("spark.cassandra.connection.host", "127.0.0.1") \
    .config("spark.cassandra.connection.port", "9042") \
    .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.4.0") \
    .getOrCreate()

# อ่าน CSV เข้า DataFrame
df = spark.read.csv("/Users/punchpnp/dsde-project/data_storage/raw_data/testData.csv", header=True, inferSchema=True)

# แสดงข้อมูลใน DataFrame
df.show()

# ยัดข้อมูลลง Cassandra
def save_to_cassandra(df, keyspace, table):
    try:
        df.show(5)
        df.write \
            .format("org.apache.spark.sql.cassandra") \
            .option("keyspace", keyspace) \
            .option("table", table) \
            .mode("append") \
            .save()
    except Exception as e:
        print(f"Error saving data to Cassandra: {e}")

# บันทึกข้อมูลลงใน Cassandra
save_to_cassandra(df, "testspace1", "table1")
