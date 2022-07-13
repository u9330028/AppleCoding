# Response 객체를 이용한 웹브라우저에 응답하기

# from flask import Flask, Response
# 플라스크에서 웹 브라우저에 응답을 할 때  모든 데이터는 Response 객체를 이용한다.
# Response 객체를 이용하여 사용자 정보를 유지하기 위하여 쿠키를 설정하기도 한다.

# Response 객체를 생성할 때 사용하는 인자
# response : 웹브라우저에게 응답할 데이터
# status : HTTP 상태코드,  200 OK
# headers : 웹브라우저에 응답할 헤더
# mimetype : image/jpeg, text/html 과 같이 HTTP 메세지 바디가 어떤 MIME Type 데이터인지를 지정
# content_type : 웹 브라우저에 응답하는 콘텐츠 타입을 지정, mimetype과 같은 역할을 한다.
# direct_passthrough : True/ False 설정

# Response 클래스의 속성
# headers : 웹 브라우저에 응답할 헤더의 데이터가 들어있음. 이속성의 데이터 타입은 headers 타입으로
#           headers의 메소드를 이용해서 응답할 헤더를 변경할 수 있다.
# status : 웹 브라우저가 수신할  HTTP 상태 코드와 상태 메세지 값을 합친 문자열 데이터, 이데이터는 웹 브라우저에
#           보내기전에 변경 가능하다.
# status_code : 웹 브라우저가 받을 HTTP 상태 코드 값을 반환한다.  정확한 상태 메세지를 모를 경우 상태 코드 값만
#           지정하면 플라스크에서 자동으로 상태메세지를 만들어 준다.
# data : 웹 브라우저가 표시할 데이터를 포함한다. get_data, set_data 메소드를 이용하여 데이터를 변경한다.
# mimetype : 웹 브라우저에 응답할 때는 일반적으로 text/html을 설정한다.


from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def res():
    res = Response("응답 테스트 하기")
    #res.headers.add("webApp-Name", "Flask-Test")
    
    return res

if __name__ == "__main__":
    app.run()








