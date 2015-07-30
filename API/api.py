import requests
import 




r = requests.get('http://9897_bo2.kh.futurum.bintime.com/api/v3/orders', auth=('admin', 'q1w2e3r4'))
print(r.text)
