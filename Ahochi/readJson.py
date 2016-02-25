import json
from pprint import pprint

json_data=open('C:\Users\Austin\Documents\Scrapy\dirbot-master\Ahochi\spiders\output3.json').read()
data = json.loads(json_data)


keywords = data["keywords"][0]
print keywords

pprint(data)

