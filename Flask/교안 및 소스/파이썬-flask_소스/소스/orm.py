# 데이터베이스 연동

# 관계형 데이터베이스(RDBMS) : MySQL, Oracle, PostgreSQL
# NoSQL : MongoDB, Cassandra, Redis..

# ORM(Object-relational mapping) : SQL의 의존적인 코딩에서 벗어난 새로운 코딩 방법(유지보수가 편리)
# ORM : iBatis, Hibernate, SQLAlchemy(Flask)

# SQLAlchemy 설치 : pip install sqlalchemy(anaconda 배포판에서는 기본으로 설치 되어 있음)

# SQLAlchemy 구성요소
##   +------------------------------------------------------------------------------------+
##    | SQLAlchemy ORM                                                                                   | 
##    | Object Relational Mapper(ORM)                                                            |     
##   +------------------------------------------------------------------------------------+
##   +------------------------------------------------------------------------------------+
##    | SQLAlchemy Core                                                                                   |    
##    |                                                                                                                 |  
##    | Schema / Types    SQL Expression Language                  Engine             |
##    |                                                                               Connection   Diallect |
##    |                                                                                    Pooling                 |
##   +------------------------------------------------------------------------------------+
##                                                                                            DBAPI

# SQLAlchemy ORM을 사용하기 위해서는 데이터베이스에 접속을 해야한다.
# 데이터베이스에 접속하기 위한 함수는 create_engine() 이다.

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# 세션 객체를 관리하기 위한 클래스와 세션 생성 클래스를 불러온다.
from sqlalchemy.orm import scoped_session, sessionmaker 

engine = create_engine('sqlite:///:memory:', echo = True)

db_session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine))

# app.teardown_appcontext
# def shutdown_session(exception=None):
#   db_session.remove()

Base = declarative_base()


# 데이터베이스 초기화 함수
def init_db():
    Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(10))
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User(id = '%d', name = '%s', email = '%s'>" % (self.id, self.name, self.email)

init_db()

##u = User('test', 'test@test.com')
##db_session.add(u) # 실제로 데이터베이스에 추가된 것이 아니라 pending 상태

# 한번에 많은 객체를 추가할 경우 add_all메소드를 이용한다.
db_session.add_all([
    User(name = 'kim', email = 'kim@naver.com'),
    User(name = 'lee', email = 'lee@naver.com'),
    User(name = 'park', email = 'park@naver.com')
    ])


db_session.commit()

##u = User()
##u.name = 'test'
##u.email = 'test@test.com'

##db_session.commit()# db_session에 pending된 것들을 실제로 데이터베이스에 추가
##db_session.rollback() # DB 변경사항을 취소

# 데이터모델 검색하는 방법
# query 속성에 있는 all, filter, filter_by 메소드를 이용하여 데이터베이스 질의를 한다.

# 예 > session.query(User).filter(User.name =='test').first()

# all : 질의 조건이 없이 데이터베이스에 있는 모든 레코드를 가져옴
# filter : 질의 조건을 인자로 받아서 그 조건에 해당하는 레코드를 데이터모델 인스턴스로 반환
#           질의 조건을 여러개를 사용할 수 있다. 콤마(,)를 이용하면 여러개의 조건을 만족하는 레코드를 얻을 수 있다.

# filter 문법 : filter(<질의클래스.질의컬럼> <비교연산자> <비교값>)
# filter는 비교연산자를 사용시 ==, !=, <=, >= 등의 연산자를 사용한다.

# filter_by : 질의 조건을 사용하여 원하는 레코드를 얻을 수 있다.
# filter_by는 질의 조건에서 == 대신에 = 를 사용한다. 하지만 !=, <=, >= 등은 사용할 수 없다.

# 질의한 결과를 가져올 때 사용하는 메소드
# first, all, one, limit, offset 메소드를 이용한다.

# first : 질의 조건에 해당하는 레코드가 여러개가 있으면 최상위 레코드만 반환, 만일 조건에 해당하는
#           레코드가 없으면 None반환,

# one : 질의 조건에 해당하는 레코드가 없으면 예외(NoResultFound)를 발생시킨다.
#           질의 조건에 해당하는 레코드가 여러 개인 경우에는 예외(MultipleResultsFound) 발생
#           반드시 한건의 레코드가 추출되도록 할 때 사용한다.

# limt : 레코드가 많을 때 몇 개를 가져올 것인지를 지정하는 메소드
# offset : 레코드가 많을 때 어디서 부터 가져올 것인지를 지정하는 메소드 

# User인스턴스를 로드(db_session.query(User)) 한후에 

##u2 = User('kimkim', 'kim@naver.com')
##db_session.add(u2)
##db_session.commit()

##testUser = db_session.query(User).filter(User.name =='kimkim').first()

##testUser = db_session.query(User).filter_by(name = 'lee').first()



u2 = User('test100', 'test100@naver.com')
db_session.add(u2)
db_session.commit()

u3 = User('kim', 'kim2@naver.com')
db_session.add(u3)
db_session.commit()

##db_session.delete(u2)
##db_session.commit()
##db_session.query(User).filter(User.name == 'kim').delete()
##db_session.commit()

testUser = db_session.query(User).all()
print(testUser)

## 쿼리 ##
for instance in db_session.query(User).order_by(User.id):
    print(instance.name, instance.email)

for name, email in db_session.query(User.name, User.email):
    print(name, email)


for row in db_session.query(User, User.name).all():
    print(row.User, row.name)
    
for row in db_session.query(User.name.label('name_label')).all():
    print(row.name_label)

for u in db_session.query(User).order_by(User.id)[0:3]:
    print(u)

for name, in db_session.query(User.name).filter_by(email = 'kim@naver.com'):
    print(name)

for name in db_session.query(User.name).filter(User.email =='lee@naver.com'):
    print(name)

for user in db_session.query(User).filter(User.name =='kim').filter(User.email =='kim2@naver.com'):
    print(user)



