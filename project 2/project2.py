import csv
import json


json_file = open("business100ValidForm.json", "r")
data = dict(json.load(json_file))

outfile = open("Cjson.csv", "w")
headers = "business_id, full_address, category, name,\n"
val = {}
for i in data.keys():
	#print("Keys:------------------",i)
	#print ("Values:-------------------",data[i])
	for a in data[i]:
		one = dict(a)
		print("Header for CSV---------------------",one.keys())
		for two in one.keys():
			print("two------------",two)
			print("three----------",one[two])
			break;

#if isinstance( b[i], dict ):
         #   get = flattenjson( b[i], delim )
          #  for j in get.keys():
           #     val[ i + delim + j ] = get[j]
        #else:
         #   val[i] = b[i]

    #return val

writer = csv.writer(outfile)

for row in json.loads(json_file.read()):
	writer.writerow(row)
