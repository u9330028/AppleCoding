from database import init_db
from database import db_session
from model import Students

def show_table():
    queries = db_session.query(Students)
    entries = [dict(id = q.id, name = q.name, gender = q.gender, age = q.age) for q in queries ]
    print(entries)

def add_entry(name, gender, age):
    student = Students(name, gender, age)
    db_session.add(student)
    db_session.commit()

def query_entry(name):
    for student in db_session.query(Students.gender).filter_by(name = name):
        print(student)

def delete_entry(name, gender):
    db_session.query(Students).filter(Students.name == name, Students.gender == gender).delete()
    db_session.commit()

def main():
    init_db()
    add_entry("홍길동", "남", 22)
    add_entry("고길동", "남", 20)
    add_entry("홍길동", "여", 19)
    add_entry("홍길순", "여", 18)
    show_table()
    query_entry("고길동")
    delete_entry("홍길동", "여")
    show_table()
    db_session.commit()

if __name__ == "__main__":
    main()
