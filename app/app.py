import pandas as pd
import datetime as dt
import dtale
import yaml

with open("config.yaml", "r") as f:
  config = yaml.load(f, Loader=yaml.FullLoader)

# read the business records into a dataframe
try:
  df = pd.read_csv(config["business_record_filename"])
  dtale.show(df, subprocess=False)  
except Exception as err:
  print(f"trouble creating dataframe from {config['business_record_filename']}")
  print(f"err: {err}")

