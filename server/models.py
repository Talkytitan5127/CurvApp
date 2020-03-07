from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship


Base = declarative_base()


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    middle_name = Column(String(32))
    department = Column(String(32), default='Main office')
    rank = Column(String(32), default='Employee')
    uuid = Column(String(128), nullable=False, unique=True)
    time_table = relationship('TimeTable', backref='employees', lazy=True)

    def fio(self):
        return "{} {}".format(self.first_name, self.last_name)


class TimeTable(Base):
    __tablename__ = 'timetable'
    id = Column(Integer, primary_key=True)
    person_time = Column(DateTime, nullable=False, default=datetime.now())
    is_exit = Column(Boolean, nullable=False, default=False)
    employee_id = Column(Integer, ForeignKey('employees.id'))
