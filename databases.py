from model import *


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session

def create_session():
    engine = create_engine('sqlite:///database.db')
    Base.metadata.create_all(engine)
    DBSession = scoped_session(sessionmaker(bind=engine,autoflush=False))
    session = DBSession()
    return session


def add_feedback(name, email, subject,message):
    session = create_session()
    feedback_object = Feedback(
        name=name,
        email = email,
        subject = subject,
        message = message,
        response = "" )
    session.add(feedback_object)
    session.commit()

def query_all():
    session = create_session()
    feedbacks = session.query(
      Feedback).all()
    return feedbacks


def query_by_name(its_name):
    session = create_session() 
    feedback = session.query(
       Feedback).filter_by(
       name=its_name).first()
    return feedback


def query_by_id(id):
    session = create_session()
    feedback = session.query(
       Feedback).filter_by(
       id=id).first()
    return feedback

def delete_feedback(its_id):
   session = create_session()
   session.query(Feedback).filter_by(
       id=its_id).delete()
   session.commit()

def editresponse(its_id, the_response):
  session = create_session()
  comment = session.query(Feedback).filter_by(id = its_id).first()
  comment.response = the_response
  session.commit()

