import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////db/sample1.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id   = Column(Integer(), primary_key=True)
    name = Column(String())
    age  = Column(Integer())

    def fetch_all():
        users = session.query(User)
        for user in users:
            print(user.name, user.age)

    def fetch_by_age(age):
        users = session.query(User).filter(User.age > age)
        for user in users:
            print(user.name, user.age)

    def fetch_by_name(name):
        search = '%{}%'.format(name)
        users = session.query(User).filter(User.name.like(search))
        # おなじ
        #users = session.query(User).filter(User.name.like('%%%s%%' % name))
        for user in users:
            print(user.name, user.age)

def main():
    User.fetch_all()
    print('===============')
    User.fetch_by_age(20)
    print('===============')
    User.fetch_by_name('とも')

if __name__ == "__main__":
    main()