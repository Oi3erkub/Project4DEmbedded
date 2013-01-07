__author__ = 'ober'
#>>> import simplejson
# simplejson.loads('[%s]' % js[:-1])
import json
import httplib
conn = httplib.HTTPConnection("alpha2.mrteera.com")
conn.request("GET", "/aqua-api/v1/fishmeasurement/?format=json&username=aquatest2&api_key=4fd311b3f496049552eaf22dce7c5798600951b2")
r1 = conn.getresponse()
print r1.status, r1.reason
data1 = r1.read()
print data1
d= json.loads(data1)
print d['meta']
print d['meta']['limit']
conn.close()