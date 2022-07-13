# 라우팅을 할 때 많이 사용하는 옵션 중에 하나 redirect_to

from flask import Flask

app = Flask(__name__)

@app.route('/aaa', redirect_to='/new_aaa')
def aaa():
    return "/aaa로 호출한 페이지 입니다"

@app.route('/new_aaa')
def new_aaa():
    return '/new_aaa로 호출한 페이지 입니다'


if __name__ =='__main__':
    app.run()
