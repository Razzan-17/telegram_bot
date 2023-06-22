from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from init import engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    name: str = Column(String(100), nullable=False)
    id: int = Column(Integer, primary_key=True)
    date_start: DateTime = Column(DateTime(), default=datetime.now)
    date_update: DateTime = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    expense = relationship('Expense')
    income = relationship('Income')


class Expense(Base):
    __tablename__ = 'expenses'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    id_person: int = Column(Integer, ForeignKey('persons.id'))
    spending_type: str = Column(String(30), nullable=False)
    summ: int = Column(Integer, nullable=False)
    comment: str = Column(String(100), nullable=True)
    date: DateTime = Column(DateTime(), default=datetime.now)


class Income(Base):
    __tablename__ = 'incomes'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    id_person: int = Column(Integer, ForeignKey('persons.id'))
    summ: int = Column(Integer, nullable=False)
    comment: str = Column(String(100), nullable=True)
    date: datetime = Column(DateTime(), default=datetime.now)


def create_table():
    Base.metadata.create_all(engine)
    print('Создание таблиц завершено!')
