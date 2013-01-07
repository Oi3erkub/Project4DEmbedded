__author__ = 'ober'
import json
import urllib2
url="http://alpha2.mrteera.com/aqua-api/v1/fishmeasurement/?format=json&username=aquatest2&api_key=4fd311b3f496049552eaf22dce7c5798600951b2"
#data = json.dumps([1, 2, 3])
data = '{"rfid": "000001", "weight": "7.3", "imageid": "000001", "standardLength": "20.0", "totalLength": "21.0", "bodyWidth": "0.0", "BodyDepth": "15.0", "headLength": "5.0", "timestamp": "2013-01-05T00:46:38"}'
req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
f = urllib2.urlopen(req)
response = f.read()
f.close()
