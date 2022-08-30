import json

# Opening JSON file
f = open('channel_messages0.json')
# returns JSON object as 
# a dictionary
data = json.loads(f.read())
dictObj = []
dictObj1 = []
# Iterating through the json
# list

for i in range(0,len(data)-1):
    dictObj.append(data[i]['message'])

for i in range(0,len(data)-1):
    dictObj1.append(data[i]['date'])

with open('sample1.json', 'w') as json_file:
    json.dump(dictObj, json_file, 
                    indent=4,  
                    separators=(',',': '))
with open('sample2.json', 'w') as json_file:
    json.dump(dictObj1, json_file, 
                    indent=4,  
                    separators=(',',': '))
  
# Closing file
f.close()