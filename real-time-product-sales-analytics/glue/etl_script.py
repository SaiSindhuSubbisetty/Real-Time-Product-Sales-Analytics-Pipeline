import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Load raw data from S3
datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": ["s3://product-sales-raw-data/"]},
    format="json"
)

# Transform data
transformed = datasource.resolveChoice(make_cols_consistent=True)
transformed = transformed.map(lambda record: {
    "product_id": record["product_id"],
    "product_name": record["product_name"],
    "quantity": record["quantity"],
    "price_per_unit": record["unit_price"],
    "total_price": record["quantity"] * record["unit_price"]
})

# Write transformed data to S3
glueContext.write_dynamic_frame.from_options(
    frame=transformed,
    connection_type="s3",
    connection_options={"path": "s3://product-sales-processed-data/"},
    format="json"
)

job.commit()