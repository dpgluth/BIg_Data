import csv
import json
import pandas as pf


rows = list()
with open("business100ValidForm.json") as json_file:
    file1 = json.load(json_file)
    data = dict(file1)
    rows = data['Business']

df = pf.DataFrame(rows)
print(df)
with open('./file.csv', 'w') as csv_f:
    df.to_csv(csv_f)
