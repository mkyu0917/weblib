from urllib.request import urlopen, Request
from urllib.parse import urlencode

data = urlencode({'a':10, 'b':20,'name':'둘리'}) #겟방식 주소에서 쿼리
#data = 'a=10&b=20&name=둘리'
#data = data.encode('utf-8') #바이트코드로 만듬

request=Request('http://www.example.com',data.encode('utf-8')) #example주소에 data안에 있는 쿼리 주소를 연결해서 바이트코드로 받음
#Request 객체를 사용한 request 헤더 변경
request.add_header('Content-Type','text/html')


f = urlopen(request)
print(f.read())