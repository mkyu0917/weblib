from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

PORT = 9999 # 포트번호9999

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):

        qindex = self.path.find('?') #'?'가 있는 스트링의 인덱스 위치반환
        #print(qindex)
        #print(self.path)#매개변수 self를 통해 받은 변수

        req_url = req_url = self.path[:len(self.path)] if qindex == -1 else self.path[:qindex]
        print(req_url)

        if req_url != '/graph': # 만약 req_url이 '/graph'가 아니면 에러출력
            self.send_error(404, 'FileNot Found')
            return

        handler_name = 'ex' + self.get_parameter('ex') #
        if handler_name not in MyHTTPRequestHandler.__dict__:
            self.send_error(404, 'FileNot Found')
            return

        MyHTTPRequestHandler.__dict__[handler_name](self)

    def get_parameter(self, name):
        qindex = self.path.find('?') # '?'있는 위치의 인덱스 반환
        #print('qindex:',qindex)
        qs= '' if qindex == -1 else self.path[qindex] #qindex가 -1이면 qs는 '' 아니라면 인덱스+1
        #print('else:',self.path[qindex+1])
        params = parse_qs(qs) #지정된 쿼리스트링을 해석하여 dict()으로 반환
        valuse = params.get(name) #파람스에서 네임을 받아 valuse에 할당

        return None if valuse is None else valuse.pop()#values가 none이면 none반환 아니면 valuse꺼내고 출력

    def ex1(self):
        self.send_response(200)#연결됬을때 디폴트값
        self.send_header('Content-Type','test/html; charset=utf-8')#페이지에 대한 정보
        self.end_header()#페이지에 대한 정보 닫기
        self.wfile.write('<h1>Hello Word</h1>'.encode('utf-8'))#ex의 값이 1일때 hello world출력

    def ex2(self):
        arr = np.random.normal(5, 3, 500)
        print('arr:',arr)
        fig, subpots = plt.subplots(2,1) #
        subpots[0].plot(arr, color='red', linestyle='solid')
        subpots[1].hist(arr, bins=20, edgecolor='black', linewidth=1.2)

        buffer = BytesIO()
        plt.savefig(buffer, dpi=80, bbox_inches='tight')
        plt.clf()

        self.send_response(200)
        self.send_heander('Content-Type', 'image/png')
        self.end_headers()
        self.wfile.write(buffer.getvaluse())


#서버구동
httpd = HTTPServer(('',PORT),MyHTTPRequestHandler)
print('HTTP Server Runs on Port(%d)' % (PORT))
httpd.serve_forever()