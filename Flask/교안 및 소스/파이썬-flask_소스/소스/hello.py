# PyPI(python Package Index) : 파이썬 패키지를 설치하는 프로그램(주로, 커맨드 차이나 쉘에서 사용)
# 명령어는 pip

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

if __name__ == "__main__":
    app.run()
