import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'my_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)

    
class Follower(Base):
    __tablename__ = 'follower' 
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('my_user.id'))
    user_to_id = Column(Integer, ForeignKey('my_user.id'))
    
class Post(Base): 
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_id'))
    
class Media (Base):   
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column('myenum', Enum("Post", "Story", "Reel", "Live"))
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post_id'))

class Comment (Base):   
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    auther_id = Column(Integer, ForeignKey('my_user.id'))
    post_id = Column(Integer, ForeignKey('post_id'))
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
