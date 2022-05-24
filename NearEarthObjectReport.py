###PYTHON 3.9####


import requests
import json
from tabulate import tabulate

class nearMiss:
    def __init__(self, object):
        self.name = object['name']
        self.referenceID = object['neo_reference_id']
        self.diameterMetric = object['estimated_diameter']['meters']
        self.diameterImperial = object['estimated_diameter']['feet']
        self.hazardous = object['is_potentially_hazardous_asteroid']
        self.passoverDate = object['close_approach_data'][0]['close_approach_date']
        self.velocity = object['close_approach_data'][0]['relative_velocity']['miles_per_hour']
        self.missDistanceMetric = object['close_approach_data'][0]['miss_distance']['kilometers']
        self.missDistanceImperial = object['close_approach_data'][0]['miss_distance']['miles']
    
    def getItems(obj):
        attr = {}
        attr['name'] = obj.name,
        attr['referenceID'] = obj.referenceID,
        attr['diameterMetric'] = obj.diameterMetric,
        attr['diameterImperial'] = obj.diameterImperial,
        attr['hazardous'] = obj.hazardous,
        attr['passoverDate'] = obj.passoverDate,
        attr['velocity(MPH)'] = obj.velocity,
        attr['missDistanceMetric'] = obj.missDistanceMetric,
        attr['missDistanceImperial'] = obj.missDistanceImperial
        
        for (key, value) in attr.items():
            print(key, value)
            
            
        
apiKey = "EmaGdEqNUEvqQsJiHgvKbmh3uhk2BsMCgXJdSPCY"
#exoplanet end point
#APIendpoint = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=cumulative&where=koi_dispositon like '{}'and koi_period".format


a = input("what year were you born?: ")
b = input("what month?: ")
c = input("and what day?: ")
birthday = "{}-{}-{}".format(a, b, c)
endDate = "{}-{}-{}".format(a, b, (int(c) + 1))
print(birthday, endDate)
APIendpoint2 = "https://api.nasa.gov/neo/rest/v1/feed?start_date={}&end_date={}&api_key={}".format(birthday, endDate, apiKey)

dailyMisses = []
req = requests.get(APIendpoint2)
reqJson = req.json()
for obj in reqJson['near_earth_objects']['{}'.format(birthday)]:
    dailyMisses.append(nearMiss(obj))

for obj in dailyMisses:
    nearMiss.getItems(obj)
