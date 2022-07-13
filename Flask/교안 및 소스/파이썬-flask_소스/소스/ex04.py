# test_request_context() : Flask에 있는 메소드이며, HTTP 요청을 테스트할 수 있는 메소드
# url_for() 메소드 활용

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/hello/')
def hello():
    return '<h1>hello world!!</h1>'

@app.route('/user/<username>')
def get_user(username):
    return 'user : '+username

if __name__ =='__main__':
    with app.test_request_context():
        print (url_for('hello'))
        print (url_for('get_user', username = 'kimkim'))
