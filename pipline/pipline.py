import sys
import pandas as pd
from datetime import datetime

print("Arguments:", sys.argv)

month = int(sys.argv[1]) if len(sys.argv) > 1 else datetime.now().month
print(f"Running pipeline for day {month}")

df = pd.DataFrame({"day": [1, 2], "number_of_passengers": [3, 4]})
df["month"] = month
print(df.head())

df.to_parquet(f"output_month_{month}.parquet")
print("Pipeline finished!")