# request URL 관련 속성
# path: url 경로 (환경 변수 PATH_INFO와 같음)
# url : 전체 URL 모두 표시
# base_url : 쿼리 스트링을 제외한 URL 표시
# url_root : 환경변수 SERVER_NAME과 같음

from flask import Flask, request

app = Flask(__name__)

@app.route("/example/environ", methods = ["GET", "POST"])
def example():
    return("path : %s<br/>"
               "url : %s<br/>"
               "base_url : %s<br/>"
               "url_root : %s<br/>") % (request.path, request.url, request.base_url, request.url_root)

if __name__ == "__main__":
    app.run()
    
           
