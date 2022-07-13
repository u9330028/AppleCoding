## 필터(filter) 연산자

"""
 equals : ==
 not equals : !=
 LIKE(대소문자를 구분함)
 ILIKE(대소문자를 구분하지 않음)
 IN 
 NOT IN
 IS NULL
 IS NOT NULL
 AND
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

Session = sessionmaker(bind = engine)
Session.configure(bind = engine)
session = Session()

def init_db():
    Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ ='users'

    id = Column(Integer, primary_key = True)
    name = Column(String(10))
    full_name = Column(String(50))
    password = Column(String(30))

    def __init__(self, name, full_name, password):
        self.name = name
        self.full_name = full_name
        self.password = password

    def __repr__(self):
        return "<User('%s', '%s', '%s')>" % (self.name, self.full_name, self.password)

init_db()

session.add_all([
    User('kim', 'kim kil dong', 'test123'),
    User('lee', 'lee kil dong', 'test333'),
    User('hong', 'hong kil dong', 'test4444'),
    User('kim', 'kim mal dong', 'test4443')
    ])

session.commit()

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.full_name)

for name in session.query(User.name).filter(User.name != 'kim'):
    print(name)

for name in session.query(User.full_name).filter(User.full_name.like('%k%')):
    print(name)


ss = session.query(User).filter(User.name.in_(['kim', 'park'])).all()
print(ss)

for user in session.query(User).filter(User.name =='kim').filter(User.full_name == 'kim mal dong'):
    print(user)
    
from sqlalchemy import and_
for user in session.query(User).filter(and_(User.name == 'kim', User.full_name =='kim kil dong')):
    print(user)



    
