# 라우팅 : 복잡한 URI를 쉽게 처리하도록 하는 기능
# Flask에서는 route() 데코레이터(@)를 사용한다.


from flask import Flask

app = Flask(__name__)

@app.route("/hello/")
def hello_flask():
    return "Hello Flask!!"


if __name__ =="__main__":
    app.run()

    
