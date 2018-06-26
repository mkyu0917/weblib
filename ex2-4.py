#http.client.httpConnectio을 사용한 GET방식 호출

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')
conn.request('HEAD','/')

result = conn.getresponse()
print(result.status,result.reason)


data = result.read()
print(len(data))