# Flask context 전역변수

"""
 [ request를 처리하기 위해 제공되는 객체 ]

  - 어플리케이션 Context
    1. current_app : 활성화된 어플리케이션의 인스턴스
    2. g : request를 처리하는 동안 어플리케이션 임시 저장정보를 사용할 수 있는 객체(글로벌 객체)

  - Request  Context
    3. request :Client에 의해 송신된 HTTP request의 contents를 관리하는 객체
    4. session : 사용자 session, 어플리케이션 request 사이의 정보를 저장에서 사용하는 dict타입 객체

"""

# g는 Flask 인스턴스 객체의 app_ctx_globals_class의 인스턴스 변수이다.
# from flask import g

from flask import Flask, render_template, current_app, g

app = Flask(__name__)

@app.route('/')
def hello():
    aa = dir(current_app)
    return "Hello Flask !!!! <br/>"+"<br/>".join(aa)

@app.route('/hi')
def hi():
    return "Hi !!!!"+g.test

@app.before_request
def before_request():
    g.test = "before_request"
    print("before request")

@app.teardown_request
def teardown_request(exception):
    print(app.app_context()) # app_context()메소드는 application context를 반환하는 메소드 
    print('end request')

if __name__ == "__main__":
    app.run()
