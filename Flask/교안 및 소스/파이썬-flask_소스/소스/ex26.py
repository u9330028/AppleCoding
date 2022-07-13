# Session : 쿠키가 클라이언트에 저장되다보니 보안상 위험하다. 따라서, 서버에 데이터를 저장하는 방식인 세션이 많이 사용되는 추세다.

# flask 모듈에 session 객체를 이용하여 세션을 설정한다.

# Flask 세션 관련키
# SECRET_KEY : 비밀키
# SESSION_COOKIE_NAME : 세션 쿠키 이름, 기본값은 session
# SESSION_COOKIE_DOMAIN : 세션 쿠키가 동작할 도메인 주소, 설정하지 않았을 경우 SERVER_NAME에 있는 도메인에서 동작
# SESSION_COOKIE_PATH : 세션 쿠키가 동작할 URL 경로, 기본값은 /
# SESSION_COOKIE_HTTPONLY : 웹어플리케이션이 HTTP 프로토콜로 동작할 때만 세션 쿠키를 웹어플리케이션에 전송
#                                                   기본 설정값은 True
# SESSION_COOKIE_SECURE : 웹어플리케이션이 HTTPS프로토콜로 동작할 때만 세션 쿠키를 웹어플리케이션에 전송
#                                               기본 설정값은 False
# PERMANENT_SESSION_LIFETIME : 세션의 유효시간을 지정한다. 기본값은 31일

from flask import Flask, request, session

app = Flask(__name__)

app.secret_key = "Kkk1234&"

@app.route("/session")
def session_set():
    session['ID'] = "Flask Test"
    return "세션을 설정하였습니다"

@app.route("/session_out")
def session_out():
    del session['ID']
    return "세션을 제거하였습니다."


##app.config.update(
##        SECRET_KEY ='jJJ1234'
##        SESSION_COOKIE_NAME = ""
##        PERMANENT_SESSION_LIFETIME = ""
##    )

if __name__ == "__main__":
    app.run()





