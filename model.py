from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()



class Feedback(Base):
   __tablename__ = 'feedbacks'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   email = Column(String)
   subject = Column(String)
   message = Column(String)
   response = Column(String)

