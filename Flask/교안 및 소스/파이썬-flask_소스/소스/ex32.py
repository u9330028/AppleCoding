from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    #Get 방식으로 요청이 들어왔을 때
    if request.method == 'GET':
        return render_template('test_login.html')
    else:
        userEmail = request.form['email']
        userPw = request.form['pw']
        # 실전에서는 userEmail, userPw에 대한 유효성 검사가 필요하다. 여기서는 생략
        return " 이메일 : " + userEmail + " 비밀번호 : " + str(userPw)

if __name__ == "__main__":    
    app.run()
    
