from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World!!</h1>'

# String타입의 username 파라미터 (String 타입은 기본값이다.)
@app.route('/user/<username>')
def show_user(username):
    return 'User %s' % username

# int 타입의 post_id 파라미터
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

#float 타입의 pi 파라미터
@app.route('/circle/<float:pi>')
def show_pi(pi):
    return 'PI %f' % pi

if __name__=="__main__":
    app.run()
    






