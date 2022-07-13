from db import init_db
from db import db_session
from models import TbTest

def show_tables():
  queries = db_session.query(TbTest)
  entries = [dict(id=q.id, name=q.name, string=q.email) for q in queries]
  print (entires)
  
def add_entry(name, email):
  t = TbTest(name, email)
  db_session.add(t)
  db_session.commit()

def query_entry(name):
    for e in db_session.query(TbTest.name).filter_by(name = name):
        print(e)
def query_entry_all():
    u = db_session.query(TbTest.email).all()
    print(u)
  
def delete_entry(name, email):
  db_session.query(TbTest).filter(TbTest.name == name, TbTest.email==email).delete()
  db_session.commit()
  
def main():
  init_db()  
  add_entry("김말똥", "test@naver.com")
  add_entry("test2", "test2@naver.com")
  query_entry("김말똥")
  delete_entry("test", "test@naver.com")
  query_entry_all()
  db_session.close()
  
if __name__ == "__main__" :
  main()
