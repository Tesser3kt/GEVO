import requests
import json
import sys
from datetime import date


room_id = sys.argv[1]
today = date.today().strftime('%Y-%m-%d')
r = requests.get(('https://gevo.edookit.net/api/lesson/v1/list-room-lessons?'
                  f'room_id={room_id}&date={today}'),
                 auth=('inkplate',
                       'h0ggz4sd1tsz2ww7n6yxzbbxiqgz6z6spazvocxi'))
if r.status_code != 200:
    print('Error: ', r.status_code)
    sys.exit(1)

r.encoding = r.apparent_encoding
with open(f'room_{room_id}.json', 'w', encoding='utf-8') as f:
    json.dump(r.json(), f, ensure_ascii=False, indent=2)
