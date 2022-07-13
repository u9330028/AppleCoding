# HTTP 메시지 (request 메시지, response 메시지)
# HTTP 메시지는 평문 형태로 되어 있으며, 헤더와 바디로 구성된다.
# 이때 헤더와 바디의 구분은 빈줄로 구분한다.

# Flask에서 HTTP 요청과 응답을 처리하기 위해서는 Request객체와 Response객체를 사용한다.

# flask모듈에서 reqeust 클래스를 가져온다.

from flask import Flask, request

app = Flask(__name__)

# Get방식에서 넘어온 변수값 가져오기
@app.route('/aaa')
def aaa():
    return "request 객체를 이용하여 얻어온 변수 name 값은 {} 입니다.".format(request.args.get('name'))

if __name__ == "__main__":
    app.run()

# request.args에서 args는 Get 방식으로 전달된 데이터만 접근할 수 있다.
