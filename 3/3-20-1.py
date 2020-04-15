import json
import gzip

file = "../jawiki-country.json.gz"

f = open(file, "r")

with gzip.open(file, mode='rt') as fp:
    for line in fp:
        data_json = json.loads(line)
        #print(data_json)
        if data_json["title"] == "イギリス":
            print(data_json["text"])