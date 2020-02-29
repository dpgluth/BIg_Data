import csv
import json


# json_file = open("business100ValidForm.json", "r")
# data = dict(json.load(json_file))

with open("business100ValidForm.json") as json_file:
    file1 = json.load(json_file)
    data = dict(file1)

    print(data)

    rows = data['Business'];
    headers = list(rows.keys());

    sep_csv = dict()  # contains lists of (dictionaires, lists) to make into csvs
    val_csv = list()  # contains lists of values pertainint ot each primitive row
    for i in rows:
         print("here is the row: ", i)
         for header in headers:
             cell_val = i[header]
             if(type(cell_val) == dict or type(cell_val) == list):
                 # create new csv file for this header
                 # # this dict to the headers list.
                 if(header not in list(sep_csv.keys())):
                     sep_csv[header]  = list()
                 else:
                    sep_csv[header].append(cell_val)
             else:
                if(header not in list(val_csv.keys())):
                    val_csv[header] = list()
                val_csv[header].append(cell_val)

    print(val_csv)
    print(sep_csv)



# outfile = open("Cjson.csv", "w")
# headers = "business_id, full_address, category, name,\n"
# val = {}
# for i in data.keys():
#   #print("Keys:------------------",i)
#   #print ("Values:-------------------",data[i])
#   for a in data[i]:
#       one = dict(a)
#       print("Header for CSV---------------------",one.keys())
#       for two in one.keys():
#           print("two------------",two)
#           print("three----------",one[two])
#           break;

# if isinstance( b[i], dict ):
         #   get = flattenjson( b[i], delim )
          #  for j in get.keys():
           #     val[ i + delim + j ] = get[j]
        # else:
         #   val[i] = b[i]

    # return val

# writer = csv.writer(outfile)

# for row in json.loads(json_file.read()):
#   writer.writerow(row)
