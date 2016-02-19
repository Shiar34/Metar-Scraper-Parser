# http://www.aviationweather.gov/adds/metars/?station_ids=NZCH&std_trans=standard&chk_metars=on&hoursStr=most+recent+only&submitmet=Submit

import urllib.request
import urllib.parse
import re

#url = urllib.request.urlopen("http://www.aviationweather.gov/adds/metars/?station_ids=NZCH&std_trans=standard&chk_metars=on&hoursStr=most+recent+only&submitmet=Submit")

url = 'http://www.aviationweather.gov/adds/metars/'
values = {'station_ids':'NZCH',
          'std_trans':'standard',
          'chk_metars':'on',
          'hoursStr':'most+recent+only',
          'submitmet':'Submit'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respdata = resp.read()

print(respdata)
print(req.geturl())