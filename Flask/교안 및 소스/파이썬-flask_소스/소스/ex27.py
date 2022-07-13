# add_url_rule 메소드 : route데코레이터 대신에 사용하는 메소드

from flask import Flask

app = Flask(__name__)

def index():
    return "Hello, Flask !!!"

app.add_url_rule('/', 'index', index)

##@app.route('/index')
##def index():
##    return "Hello, Flask!!!"

if __name__ =="__main__":
    app.run()
