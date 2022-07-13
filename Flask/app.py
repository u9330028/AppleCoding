from flask import Flask, render_template
import numpy as np

app = Flask(__name__)


@app.route('/user/<userName>')
def getUrlName(userName):
    return 'user : %s' % userName


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/cicle/<float:pi>')
def show_pi(pi):
    return 'Pi %f' % pi


@app.route('/show_html/')
def html():
    return render_template('index.html')


@app.route('/super/<list>')
def displayList(list):
    return render_template('super.html', arrL=list.split(','))


@app.route('/myname/<username>')
def myname(username):
    return render_template('myname.html', name=username)

@app.route('/condition/<FF>')
def def_if(FF):
    return render_template('myname.html', ff=FF)
# 모든 웹프로그램은 사용자가 웹 브라우저을 이용해서 웹프로그램이 가지고 있는 자원(영상,강좌,기타)을 요청하면
# 이해 할 수있는 형태로 재가공 하거나, 있는 자원그대로 웹브라우저에게 반환해준다.
# 웹서버와 웹브라이저간의 발생하는 자원 반환 단계에서는 웹서버가 컨텐츠 협상이라는 단계를거처 웹브라워저에
# 반환한다.

# 1.서버기반의 협상
# 2.에이전트 기반의 협상
# 3.투명한 협상(1,2를 혼합산 협상)
# 서버기반의 협상: 웹서버가 웹브라우저에 반환할 데이터의 형태를 직접 결정
# 에이전트(캐시서버) 기반의 협상: 웹서버가 응답할데이터 처리형태를 결정하기 위한 첫 번째 수신을 처리한
# 수신을 처리한 에이전트에 의한 형태 결정


# 협상에 필요한 HTTP 메시지 헤더
# Accept: 부라우저가 처리할 수 있는 데이터의 형태 선호도 text/html
# Accept: Language 부라우저가 수용할 수 있는 응답결과의 언어와 선호도
# Accept: 브라우저가 수용할 수 있는 등답 인코딩 형태와 선호도
#request / response
if __name__ == "__main__":
    app.run()
