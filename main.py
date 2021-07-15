import pandas as pd
import json
from datetime import datetime

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)

ts = int("1284101485")

# if you encounter a "year is out of range" error the timestamp
# may be in milliseconds, try `ts /= 1000` in that case
print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

with open('./uniV2Datatest.json', 'r') as f:
    data = json.loads(f.read())
    
# df = pd.DataFrame(data)

# df = pd.read_json("./uniV2Data")
df = pd.json_normalize(data)

def returnDateTime(x):
    return(datetime.utcfromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    
df['date'] = df['date'].apply(returnDateTime)


df.to_csv('out.csv',index=False)
print(df)
