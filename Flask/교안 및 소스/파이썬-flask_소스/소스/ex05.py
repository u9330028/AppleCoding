# Jinja2 템플릿 엔진

# Flask 설치할 때 같이 설치되기 때문에 추가 설치 할 필요가 없다.
# 플라스크의 템플릿 파일들은 기본적으로 /templates/ 폴더에 저장한다.

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello world!!</h1>'

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', name = username)

if __name__ == '__main__':
    app.run()
