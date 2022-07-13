# HTTP 요청 전후에 대한 핸들러

# Flask에서는 HTTP 요청 전후에 사용할 수 있는 데코레이터를 제공하고 있다.

# before_first_request : 웹프로그램이 실행된 이후 가장 처음에 들어오는 HTTP 요청에서만 실행
# before_request : 매번 HTTP 요청(request)이 들어올 때마다 실행
# after_request : 매번 HTTP 요청이 끝나고 브라우저에 응답하기전에 실행
# teardown_request : HTTP 요청의 결과가 브라우저에 보내진 다음에 실행
# teardown_appcontext : HTTP 요청이 완전히 완료되면 실행(애플리케이션 컨텍스트 내에서 실행)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def res():
    return "/"

@app.before_first_request
def before_first_request():
    print("앱이 실행되고 나서 첫번재 HTTP 요청에만 응답한다.")

@app.before_request
def before_request():
    print("매번 HTTP 요청이 처리되기전에 실행된다.")

@app.after_request
def after_request(response):
    print("매번 HTTP요청이 처리되고 나서 실행된다.")
    return response

@app.teardown_request
def teardown_request(exception):
    print("매번 HTTP 요청의 결과가 브라우저에 보내진 다음에 호출된다")

@app.teardown_appcontext
def teardown_appcontext(exception):
    print("HTTP 요청의 애플리케이션 컨텍스트가 종료될 때 실행된다")

if __name__ == "__main__":
    app.run()


    

    





    

    
