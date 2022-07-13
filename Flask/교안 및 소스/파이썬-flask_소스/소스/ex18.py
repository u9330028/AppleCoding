# WSGI(envrion 사전에서 제공하는) 표준 환경 변수


# REQUEST_METHOD : 웹브라우저가 보낸 요청의 처리 방식에 대한 문자열 포함

# SCRIPT_NAME : 스크립트 파일명을 표현, FLASK에서는 빈값으로 출력

# PATH_INFO :  URL 경로(PATH), 예> http://www.aaa.com/ccc/main ---> /ccc/main

# CONTENT_TYPE : 웹브라우저가 보낸 HTTP 요청 메시지의 바디에 포함되는 콘텐츠 형태 저장
#                              HTTP헤더에 Content-type 헤더 값을 확인한다.

# SERVER_NAME : 서버의 도메인 주소(IP)가 저장, 예> http://www.aaa.com/ccc/main --->www.aaa.com

# SERVER_PORT : 웹 어플리케이션이 동작하고 있는 서버 포트번호가 저장
#       예> http://www.aaa.com/5000/env ---> 5000 저장 , 도메인주소에 포트가 없으면 80 저장

# SERVER_PROTOCOL : 웹 어플리케이션이 동작하는 서버 프로토콜 버전이 표시, HTTP/1.1

# QUERY_STRING : URL 끝에 보면 ?문자 뒤에 오는 문자열을 쿼리 스트링이라고 한다. 키=값의 형태로 지정

# <wsgi 전용 환경 변수 >
# wsgi.version : WSGI 번전을 튜플 형태로 반환  (1.0)
# wsgi.url_scheme : URL 스키마의 종류, 웹서버인 경우에는 http를 반환한다.

#       키값이 두개 이상일 때는 키사이에 &문자로 구분한다.


from flask import Flask, request

app = Flask(__name__)

@app.route("/test/environ", methods=["GET", "POST"])
# request의 environ 속성 : HTTP 통신에 사용하는 환경 변수를 담고 있는 사전(wsgi 전용 환경변수도 포함)
def test():
    strVal = ("REQUEST_METHOD : %(REQUEST_METHOD)s<br/>"
                   "PATH_INFO : %(PATH_INFO)s<br/>"
                   "QUERY_STRING : %(QUERY_STRING)s<br/>"
                   #"CONTENT_TYPE :%(CONTENT_TYPE)s<br/>"
                   "SERVER_NAME : %(SERVER_NAME)s<br/>"
                   "SERVER_PORT : %(SERVER_PORT)s<br/>"
                   "SERVER_PROTOCOL: %(SERVER_PROTOCOL)s<br/>"
                   "wsgi.version : %(wsgi.version)s<br/>"
                   "wsgi.url_scheme : %(wsgi.url_scheme)s") % request.environ


    return strVal


if __name__ == "__main__":
    app.run()

    
    











