import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime, timezone

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    # Here we define columns for the table 'estudiantes'
    # Each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    created = Column(Date, default=lambda: datetime.now(timezone.utc).date())

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    student_id = Column(Integer, ForeignKey('student.id'))
    person = relationship(Student)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
