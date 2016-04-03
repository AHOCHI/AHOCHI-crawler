# fixed but doesn't do anything

import json
import os
from pprint import pprint

json_data = open(os.path.join(os.path.dirname(__file__), 'spiders\output3.json')).read()
data = json.loads(json_data)
pprint(data)
