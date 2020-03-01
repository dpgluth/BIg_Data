import csv
import json
import pandas as pf
from pandas.io.json import json_normalize

rows = list()

with open("business100ValidForm.json") as json_file:
    file1 = json.load(json_file)
    data = dict(file1)
    rows = data['Business']


df = json_normalize(rows)
# df = df.astype(str)

print(df)

with open('./file.tsv', 'w') as csv_f:
    df.to_csv(csv_f, sep='\t', index=False)



#use pandas to normalize data

