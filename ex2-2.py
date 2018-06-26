#GET방식으로 웹서버에 요청보내기
from urllib.request import urlopen

f = urlopen("http://example.com?a=10&b=20")
print(f.read())
