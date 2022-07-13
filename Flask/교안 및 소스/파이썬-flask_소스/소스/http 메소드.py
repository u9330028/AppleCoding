# HTTP 메서드 중 GET, POST가 대표적이다.
# GET, POST 이외에도 PUT, DELETE, HED, OPTIONS 메서드가 있는데, 이러한 타입들은 REST API개발
# 시에 주로 사용된다.

# 웹 프로그램에 자원을 요청하는 대표적인 방법은 GET 방식이다. GET방식은 웹브라우저의
# 주소 입력란에 전달하고자 하는 정보가 노출되기 때문에 중요한 정보 전달을 할 때는 사용하지 않는다.

# POST방식은 HTTP 메시지의 BODY에 데이터를 포함해서 전달한다. 따라서, 많은 양의 데이터를 전달
# 할 때 사용하며, HTTPS를 사용하는 웹서버는 전달하는 데이터가 중요하기 때문에 암호화 처리되어 전달

@app.route('/aurl', methods = ['GET']) 일반적으로 GET방식은 생략된다.
def aaa():
    pass
@app.route('aurl', methods = ['POST'])
def bbb():
    pass

#위의 코드는 HTTP메서드 타입에 따라 뷰함수가 다른 경우

# 아래의 코드는 HTPP메서드 타입이 달라도 하나의 뷰함수 사용

@app.route('burl', methods=['GET', 'POST'])
def ccc():
    pass


# route 데코레이터에 methods 인자가 없으면 뷰함수는 GET요청만을 처리하게된다.


# URL 변수에 기본값 할당하기

@app.route('/aaa', defaults={'page' : 'index'})
@app.route('/aaa/<page>')

#브라우저에서 /aaa/를 호출한 경우에는 /aaa/index형태의 주소를 호출한 것과 같다.






