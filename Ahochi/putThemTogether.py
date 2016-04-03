# broken

import json
import os

json_data = open(os.path.join(os.path.dirname(__file__), 'TriStateFileIntAlt')).read()
data = json.loads(json_data)

print(data)
