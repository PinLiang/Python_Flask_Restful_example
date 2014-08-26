import httplib, urllib
import simplejson as json

url = "your domain name or IP address"
data = {"name":"PinLiang", "mystery":"Password"}
headers = {"Content-type":"application/json", "Accept":"text/plain"}
conn = httplib.HTTPSConnection("your domain name or IP address ex:pinliang.com.tw")
#conn = httplib.HTTPConnection("your domain name or IP address")
print json.dumps(data)
conn.request("POST", '/PinLiang/', json.dumps(data), headers)
response = conn.getresponse()
print response.status, response.reason
print response.read()
