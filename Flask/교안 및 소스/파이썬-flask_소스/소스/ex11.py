# redirect_to 옵션에 다른 url이 아닌 함수를 전달하는 방법

# 함수를 전달하기 위해서는 미리 함수를 정의 해둬야 한다.
# 정의된 함수의 첫번째 인자는 필수적으로 adapter 이어야 한다.

from flask import Flask

app = Flask(__name__)

def redirect_new_aaa(adapter, p1, p2):
    return "/new_aaa/{0}/{1}".format(p1, p2)

@app.route("/aaa/<p1>/<p2>", redirect_to = redirect_new_aaa)
def aaa(p1, p2):
    return "/aaa/p1/p2로 호출되는 페이지 입니다."

@app.route("/new_aaa/<p1>/<p2>")
def new_aaa(p1, p2):
    return "/new_aaa/{0}/{1}로 호출되는 페이지 입니다.".format(p1, p2)

if __name__ == '__main__':
    app.run()
