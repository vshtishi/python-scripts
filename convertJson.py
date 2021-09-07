import json
import dateutil.parser

import os
path = os.environ['path']

jsList = []
with open(path, 'r') as f:
    for line in f:
        data = json.loads(line)
        data['_source']['created_at'] = dateutil.parser.isoparse(data['_source']['created_at']).isoformat()
        data['_source']['updated_at'] = dateutil.parser.isoparse(data['_source']['updated_at']).isoformat()
        a_dictionary = data['_source']
        dictionary_copy = a_dictionary.copy()
        jsList.append(dictionary_copy)


import json

with open(path, 'w') as fp:
    fp.write(
        '\n'.join(json.dumps(i) for i in jsList) +
        '\n')

