import requests
import sys
import json

r = requests.get('https://gevo.edookit.net/api/dochazka/v2/klas-skupiny',
                 auth=('inkplate', 'h0ggz4sd1tsz2ww7n6yxzbbxiqgz6z6spazvocxi'))
if r.status_code != 200:
    print('Error: ', r.status_code)
    sys.exit(1)

r.encoding = r.apparent_encoding
with open('dochazka.json', 'w', encoding='utf-8') as f:
    json.dump(r.json(), f, ensure_ascii=False, indent=2)
