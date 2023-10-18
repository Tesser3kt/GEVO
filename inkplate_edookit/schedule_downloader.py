import requests
import json
import sys


room_id = sys.argv[1]
r = requests.get(('https://inkplate:h0ggz4sd1tsz2ww7n6yxzbbxiqgz6z6spazvocxi'
                  '@gevo.edookit.net/api/lesson/v1/list-room-lessons?'
                  f'room_id={room_id}&date=2023-09-06'))
if r.status_code != 200:
    print('Error: ', r.status_code)
    sys.exit(1)

r.encoding = r.apparent_encoding
with open(f'schedule_{room_id}.json', 'w', encoding='utf-8') as f:
    json.dump(r.json(), f, ensure_ascii=False, indent=4)
