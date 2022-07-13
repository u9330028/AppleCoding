# 프로그래머가 특정 객체로 변환해서 리턴할 때

# 코드 예 > return request.values.get("name", 100, type=int) --> int 객체로 반환

# 위의 예는 프로그래머가 반환타입을 쉽게 int객체로 변환하여 반환하는 예 이다.
# type의 값으로 파이썬에서 제공하는 기본 타입 이외에도 함수나 클래스(인스턴스)를 사용할 수 있다.
# 즉, 사용자 정의 데이터 타입을 사용하는 것이다.

from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

# 사용자 정의 함수 (특정 날짜 형식을 지정하는 함수)
def userDateType(date_format):
    def changeFormat(date_string):
        # strptime(date_string, format) : format 맞는 date_string을 datetime객체로 리턴하는 메소드
        return datetime.strptime(date_string, date_format)
    return changeFormat

@app.route("/ccc",  methods = ["GET", "POST"])
def ccc():
    print(request.values.get("date", default = "2018-05-25", type=userDateType("%Y-%m-%d")))
    return "콘솔을 통해서 확인해보세요"


if __name__ == "__main__":
    app.run()


    
