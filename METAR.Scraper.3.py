# http://www.aviationweather.gov/adds/metars/?station_ids=NZCH&std_trans=standard&chk_metars=on&hoursStr=most+recent+only&submitmet=Submit
import time
import re
import requests
from bs4 import BeautifulSoup

def get_html():
    payload = {'station_ids':'NZCH',
           'std_trans':'standard',
           'chk_metars':'on',
           'hoursStr':'most recent only',
           'submitmet':'Submit'}
    r = requests.get("http://www.aviationweather.gov/adds/metars/", params=payload)
    soup = BeautifulSoup(r.content, "html.parser")
    td = soup.find_all('font')
    return td

def html_stripper(td):
    str_td = str(td)
    short_td = re.sub('<[^<]+?>', '', str_td)
    td_list = short_td.split()
    return td_list

def metar_prettify(metar):
    
    def stringsplit(list,item,start,end):
        list_item = str(list[item])
        return(list_item[start:end])  
    
    def visibility(data):
        vis = int(data)
        if vis == 9999:
            return(">9.5km")
        else:
            return(vis,"m")
    def clouds(data):
        clouds = {'NCD':'No Cloud Detected',
                  'FEW':'Few Clouds',
                  'SCT':'Scattered Clouds',
                  'BKN':'Broken Clouds',
                  'OVC':'Overcast'}
        return(clouds[data])
     
    print("METAR report for", stringsplit(metar,0,1,5))
    print('Date:',stringsplit(metar,1,0,2 ),time.strftime("%B"), "|",
          'Report Issued:',stringsplit(metar,1,2,6),"GMT","|",
          'Wind:', stringsplit(metar,3,3,8), 'at Heading', stringsplit(metar,3,0,3), "|",
          'Visibility:', visibility(metar[4]), "|",
          'Cloud Cover:', clouds(metar[5]), "|",
          'Temperature:', stringsplit(metar,6,0,2),chr(176),"C", "|",
          )

def main():
    td = get_html()
    metar = html_stripper(td)
    raw_metar = (',' .join(metar))
    print('===================')
    print('Raw METAR Data:', raw_metar)
    print()
    print(metar_prettify(metar))
    print('===================')
    input("Press any key to exit: ")

main()
exit
# ===============================================================================
