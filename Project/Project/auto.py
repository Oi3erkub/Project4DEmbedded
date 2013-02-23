__author__ = 'ober'
import urllib2 ,urllib
username ="s2011212"
password="diwvmg7e"
url='https://161.246.254.213/dana-na/auth/url_default/login.cgi'
params = urllib.urlencode({'tz_offset': '420', 'realm': 'Users','username':username,'password':password})
print params
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip,deflate,sdch',
'Accept-Language':'en-US,en;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'79',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'lastRealm=Users; DSSIGNIN=url_default; DSSignInURL=/; DSID=edf3e3719488ac5e8ad91205f0a56596; DSFirstAccess=1360779513; DSLastAccess=1360779527',
'Host':'161.246.254.213',
'Origin':'https://161.246.254.213',
'Referer':'https://161.246.254.213/dana-na/auth/url_default/welcome.cgi',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17'}
print headers
response = urllib2.urlopen(url, params).read()
print response