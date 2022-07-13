from sqlalchemy import Column, Integer, String
from db import Base

class TbTest(Base):
  __tablename__ = 'tbTable'
  id = Column(Integer, primary_key=True)
  name = Column(String(30))
  email = Column(String(50))
  
  def __init__(self, name, email):
    self.name = name
    self.email = email
    
  def __repr__(self):
    return "<TbTest('%d', '%s', '%s'>" %(self.id, self.name, self.email)
