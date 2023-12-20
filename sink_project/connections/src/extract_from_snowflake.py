from pyspark.sql import SparkSession
from utilities import *


spark = SparkSession.builder.appName("Sf Read").getOrCreate()

print(spark)

creds = read_credentials()


