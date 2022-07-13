#make_response 메소드 : Response를 만들기위한 메소드

from flask import Flask, session, request, redirect, make_response, url_for

print(" name :  ", __name__)

app = Flask(__name__)

app.secret_key ='Kimkim1234?'

def index():
    response = make_response("<h1>Hello, Flask!!!</h1>")    
    return response

app.add_url_rule('/', 'index', index)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
                <h2>로그인</h2>
                <form method = "post">
                    <p><input type = text name = username></p>
                    <p><input type = submit value = 로그인></p>
                </form>
                '''
if __name__ =="__main__":
    app.run()
