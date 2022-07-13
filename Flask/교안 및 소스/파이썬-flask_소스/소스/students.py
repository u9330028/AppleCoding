from sqlalchemy import Column, Integer, String
from database import Base

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key = True)
    name = Column(String(30))
    gender = Column(String(10))
    age = Column(Integer)

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __repr__(self):
        return "<Students('%d', '%s', '%s', '%d'>" %(self.id, self.name, self.gender,self.email)
    
