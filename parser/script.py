#from google.cloud import storage
import pandas as pd
import json
import time
import pymongo as pm

# Initialise a client
#storage_client = storage.Client("multi-k8s-369008")
# Create a bucket object for our bucket
#bucket = storage_client.get_bucket("data-ims")
# Create a blob object from the filepath
#blob = bucket.blob("raw-parquets/userdata1.parquet")
# Download the file to a destination
#blob.download_to_filename("userdata1.parquet")

parquet_path = "./parquet_files/"
parquet_file = "raw-parquets_userdata1.parquet"
try:
  print(pd.read_parquet(parquet_path + parquet_file, engine='auto'))
  state = {"filename": parquet_file, "stage": "completed"}
except:
  state = {"filename": parquet_file, "stage": "failed"}
  print("An exception occurred")

json_object = json.dumps(state, indent=4)
with open("state" + str(time.time()) + ".json", "w") as outfile:
    outfile.write(json_object)