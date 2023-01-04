import pandas as pd
import json
import time
import pymongo
from google.cloud import storage

# Initialise a client
#storage_client = storage.Client("multi-k8s-369008")
# Create a bucket object for our bucket
#bucket = storage_client.get_bucket("data-ims")
# Create a blob object from the filepath
#blob = bucket.blob("raw-parquets/userdata1.parquet")
# Download the file to a destination
#blob.download_to_filename("userdata1.parquet")
# The ID of your GCS bucket
# bucket_name = "your-bucket-name"
# The ID of your new GCS object
# blob_name = "storage-object-name"

#storage_client = storage.Client()
#bucket = storage_client.bucket("data-ims")
#blob = bucket.blob("userdata1.parquet")

# Mode can be specified as wb/rb for bytes mode.
# See: https://docs.python.org/3/library/io.html
#parquet_path = "./parquet_files/"
#parquet_file = "raw-parquets_userdata1.parquet"

timestamp = str(time.time())

try:
  print(pd.read_parquet("gs://data-ims/raw-parquets/userdata1.parquet", engine='auto'))
  state = {"filename": parquet_file, "stage": "completed", "time": timestamp}
except:
  state = {"filename": parquet_file, "stage": "failed", "time": timestamp}
  print("An exception occurred")


json_object = json.dumps(state, indent=4)
with open("state" + timestamp + ".json", "w") as outfile:
    outfile.write(json_object)

myclient = pymongo.MongoClient("mongodb://mongodb-cluster-ip-service:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["run_instances"]
x = mycol.insert_one(state)
print(x.inserted_id)