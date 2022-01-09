import pyspark
import sys
from pyspark.sql.types import FloatType
spark = pyspark.SparkContext.getOrCreate()
spark_session = pyspark.sql.SparkSession(spark)
from pyspark.sql import functions as F
country_data = spark_session.read.csv(sys.argv[1],inferSchema=True,header=True)
global_data = spark_session.read.csv(sys.argv[2],inferSchema=True,header=True)
global_data=global_data.select(F.col('dt'),F.col('LandAverageTemperature'))
country_data=country_data.withColumn('AverageTemperature',country_data['AverageTemperature'].cast(FloatType()))
global_data=global_data.withColumn('LandAverageTemperature',global_data['LandAverageTemperature'].cast(FloatType()))
#country_data.AverageTemperature=country_data.AverageTemperature.cast(FloatType())
#global_data.LandAverageTemperature=global_data.LandAverageTemperature.cast(FloatType())
country_maxtemp_rdd=country_data.groupBy("Country",'dt').agg(F.max("AverageTemperature").alias('MaxTemp'))
final_data=country_maxtemp_rdd.join(global_data,on=['dt'],how='inner').sort('Country')
output_data=final_data.filter(final_data['MaxTemp']>final_data['LandAverageTemperature']).groupBy('Country').agg(F.count('Country')).sort('Country').collect()
for i in output_data:
    print('%s\t%s'%(i[0],str(i[1])))