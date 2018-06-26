#urlparse

from urllib.parse import urlparse

url = 'http://www.python.org:80/guido/python.html:philosophy?a=10&b=20#here'
# a는 파라미터 또는 쿼리스트림이라함
result = urlparse(url)
print(result)
#urlparse는  스키마 , 넷록=주소, 패스, 파라미터, 쿼리등을 나타냄

