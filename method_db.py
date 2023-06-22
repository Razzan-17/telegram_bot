from init import engine, Session
from models import Person, Income, Expense


class MethodOnDateBase:
    @staticmethod
    def register(id_person: int, name: str) -> None:
        '''Регистрация нового пользователя бота!'''
        with Session(autoflush=False, bind=engine) as db:
            if not db.query(Person).filter(Person.id == id_person).first():
                person = Person(name=name,
                                id=id_person)
                db.add(person)
                db.commit()

    @staticmethod
    def add_expense(id_person: int, data: dict) -> None:
        '''Добавление расходов в БД'''
        with Session(autoflush=False, bind=engine) as db:
            expense = Expense(id_person=id_person,
                              spending_type=data['type'],
                              summ=data['summ'],
                              comment=data['comment'])
            db.add(expense)
            db.commit()

    @staticmethod
    def add_income(id_person: int, data: dict) -> None:
        '''Добавление доходов в БД'''
        with Session(autoflush=False, bind=engine) as db:
            income = Income(id_person=id_person,
                            summ=data['summ'],
                            comment=data['comment'])
            db.add(income)
            db.commit()

    @staticmethod
    def query_expense(id_person: int):
        '''Запрос всех расходов'''
        with Session(autoflush=False, bind=engine) as db:
            expense = db.query(Expense).filter(Expense.id_person == id_person).all()
            return expense
