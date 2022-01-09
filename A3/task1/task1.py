import pyspark
import sys
spark = pyspark.SparkContext()
spark_session = pyspark.sql.SparkSession(spark)
from pyspark.sql import functions as F


df = spark_session.read.csv(sys.argv[2],inferSchema=True,header=True)
#df=spark.SparkContext.parallelize(df)
country_rdd=df.filter(df.Country==sys.argv[1]).sort('City')
#print(country_df)
avrg_rdd=country_rdd.groupBy("City").agg(F.avg('AverageTemperature').alias('avg'))
r=country_rdd.join(avrg_rdd,on=["City"],how="inner").sort("City")
#r.show()
r=r.filter(r.AverageTemperature > r.avg).groupBy("City").agg(F.count("City")).sort("City")
for row in r.collect():
	print(row[0]+"\t"+str(row[1]))
	
