#app.config.from_object 메소드를 이용한 sqlite config 설정하기

from flask import *
import sqlite3

#sqlite 환경 설정

DATABASE = 'my.db' # 여기에는 경로 설정이 가능하며 경로가 없을 경우에는 현재 실행되고 있는 어플리케이션의 위치에 생성
SECERET_KEY = 'development key'
USERNAME = 'root'
PASSWORD = '1234'

app = Flask(__name__)

# sqlite 환경 설정값을 읽어 오기
app.config.from_object(__name__)

# Request Hooking(HTTP 요청 전후의 처리)
# request 처리전에 데이터베이스 접속 및 테이블 생성이 필요하고,
# request 처리 후에는 데이터베이스 접속을 종료해야한다.

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def createTable(g):
    try:
        sql = "create table if not exists student(name text, count int)"
        g.db.execute( sql )
        g.db.commit()        
    except Exception as err:
        print('error : ', err)


@app.before_request
def before_request():
       g.db = connect_db()
       createTable(g)
       print("before request")
       
@app.teardown_request
def teardown_request(exception):
    g.db.close()
    print("end request")

@app.route('/stu_insert')
def stu_insert():
    return render_template('stu_form.html')

@app.route('/ins', methods = ["POST"])
def insertData():
    result = "insert success"
    if request.method == "POST" :
        name = request.form["name"]
        age = request.form["age"]
        try:
            sql = "INSERT INTO student(name, count) VALUES(?, ?)"
            #data =("LeeLee", 21)
            data = (name, int(age))
            g.db.execute( sql, data)
            g.db.commit()
        except Exception as err:
            result = err
    return result

@app.route('/select')
def select_stuData():
    try:
        sql = "SELECT * FROM student"
        cur = g.db.execute(sql)
        data = cur.fetchall() #이때 stuData는 list[tuple]
        stuData = [dict(name = n, count = cnt) for n, cnt in data]        
    except Exception as err:
        print('error : ', err)

    return render_template('view_stuData.html', stuData = stuData)     

@app.route('/')
def myTest():
    return "hello flask!!!!!"    

if __name__ == "__main__":
    app.run()








    

